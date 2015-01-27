# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sits_viewer
                                 A QGIS plugin
 Plugin for Satellite Image Time Series visualization

                              -------------------
        begin                : 2014-10-27
        copyright            : (C) 2014 by Victor Maus/INPE
        email                : victor.maus@inpe.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
import qgis
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os.path
import numpy as np
import matplotlib.pyplot as plt
import urllib2
import json 
import datetime
import time
import unicodedata
import scipy
from scipy.signal import savgol_coeffs, savgol_filter
from scipy.signal._savitzky_golay import _polyder

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from sits_viewerdialog import sits_viewerDialog


class sits_viewer:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # refernce to map canvas
        self.canvas = self.iface.mapCanvas()
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # create our GUI dialog
        self.dlg = sits_viewerDialog()
        # creat a list to hold our selected features ids
        self.selectList = []
        # current layer ref (set in handleLayerChange)
        self.cLayer = None #self.canvas.currentLayer()
        # current layer dataProvider ref (set in handleLayerChange)
        self.provider = None

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/sits_viewer/icon.png"), \
            "SITS Viewer", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&some text that appears in the menu", self.action)
        
        # Add filters
        filtersList = ["Savitzky-Golay","Wavelet"]
        nProducts = len(filtersList)
        for i in range(nProducts):
           self.dlg.addFilters(str(filtersList[i]))
        
        chronosURL = str("http://www.dpi.inpe.br/mds/mds/product_list?&output_format=json")
        if not(self.url_exists(chronosURL)):
            # update TextBrowser
            self.dlg.setTextBrowser(  str("The server does not respond. Connection timed out "+chronosURL)  ) 
            QMessageBox.information( self.iface.mainWindow(),"Info", "The server does not respond. Connection timed out!" )
        else:
            response = urllib2.urlopen(chronosURL)
            data = json.load(response)
            nProducts = len(data["products"])
            for i in range(nProducts):
                product = unicodedata.normalize('NFKD', data["products"][i]).encode('ascii','ignore')
                self.dlg.addProducts(str(product))
        
        # How to use
        self.dlg.setTextBrowser(str("The time period is not implemented yet, but it is possible to zoom in the plot window.\nTo start using the tool select one product.\nThen select one or more datasets and either click in the map or tipe the coordinates."))
               
        # connect our custom function to a clickTool signal that the canvas was clicked
        #QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.getCoordinatesMouseDown)
        
        # Update dataset list
        QObject.connect(self.dlg.ui.listWidget_products, SIGNAL("itemClicked(QListWidgetItem *)"), self.update_datasetList)
        
        # Update dataset list
        #QObject.connect(self.dlg.ui.pushButton_list_datasets, SIGNAL("clicked()"), self.update_datasetList)
        
        # Update plot
        QObject.connect(self.dlg.ui.pushButton_plot, SIGNAL("clicked()"), self.plotTimeSeries)
        
        # Save CSV
        QObject.connect(self.dlg.ui.pushButton_save, SIGNAL("clicked()"), self.saveCSV)

    def timeSeriesFilter(self, x, filterType):
        if   filterType == "Savitzky-Golay":
            x = np.array(x)
            x = savgol_filter(x, 7, 4)
            return x
          
        elif filterType == "Wavelet":
            x = np.array(x)
            x = savgol_filter(x, 7, 4)
            return x
          
        elif filterType == "Wavelet":
            x = np.array(x)
            x = medfilt(x, 7, 4)
            return x
          
        #else:
            #x = np.array(x)
            #x = medfilt(x, 7, 4)
            #return x

    
    def saveCSV(self):
        className = self.dlg.ui.lineEdit_classname.displayText()
        if className=="":
           QMessageBox.information( self.iface.mainWindow(),"Info", "Missing class name. \nPlease type a class name." )
           return None
        
        
        # Get selected dataset list
        items = self.dlg.ui.listWidget_datasets.selectedItems()
        if not(items):
           #self.dlg.setTextBrowser(  str("Missing a dataset. Please select one or more datasets.")  ) 
           QMessageBox.information( self.iface.mainWindow(),"Info", "Missing dataset. \nPlease select one or more datasets." )
           return None
        
        datasetsList = []
        filesList = []
        for i in list(items):
            datasetsList.append(str(i.text()))
            filesList.append( str(  className+"."+i.text()+"."+sampleNumber+".csv" ) )

    def getCoordinatesMouseDown(self, point, button):
        iface = qgis.utils.iface
        mc = iface.mapCanvas()
        mr = mc.mapRenderer()
        canvasCrs = mr.destinationCrs()
        LLCrs = QgsCoordinateReferenceSystem()
        LLCrs.createFromProj4("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
        CoordinateTransform = qgis.core.QgsCoordinateTransform
        point = CoordinateTransform(canvasCrs, LLCrs).transform(point)
        self.dlg.clearTextCoordinates()
        self.dlg.setTextCoordinates(str(point.x())+","+str(point.y()))
        self.plotTimeSeries()
      
    def handleLayerChange(self, layer):
            self.cLayer = self.canvas.currentLayer()
            if self.cLayer:
                self.provider = self.cLayer.dataProvider()
    
    def update_datasetList(self):
        self.dlg.clearDatasets()
        
        # Check MODIS produc selection
        product = self.dlg.ui.listWidget_products.currentItem()
        if not(product):
            #self.dlg.setTextBrowser(  str("Missing the product. Please select one MODIS product.")  ) 
            QMessageBox.information( self.iface.mainWindow(),"Info", "Missing the product. \nPlease select one MODIS product." )
            return None
        # Check server connection 
        chronosURL = str("http://www.dpi.inpe.br/mds/mds/dataset_list?product="+str(product.text())+"&output_format=json")
        if not(self.url_exists(chronosURL)):
            self.dlg.setTextBrowser(  str("The server does not respond. Connection timed out "+chronosURL)  ) 
            return None
        # Get datasets list and add to QlistWidget
        response = urllib2.urlopen(chronosURL)
        data = json.load(response)
        datasetsList = data["datasets"]
        nDatasets = len(datasetsList)
        for i in range(nDatasets):
            datasetName = unicodedata.normalize('NFKD', datasetsList[i]).encode('ascii','ignore')
            if datasetName!="day2" and datasetName!="day" and datasetName!="day2" and datasetName!="quality" and datasetName!="reliability" and datasetName!="viewangle":
              self.dlg.ui.listWidget_datasets.addItem(datasetName)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&some text that appears in the menu",self.action)
        self.iface.removeToolBarIcon(self.action)

    def url_exists(self, location):
        request = urllib2.Request(location)
        request.get_method = lambda : 'HEAD'
        try:
            response = urllib2.urlopen(request)
            return True
        except urllib2.HTTPError:
            return False

    def transform_dates(self, timeline):
         M = len(timeline)
         for i in range(M):
            timeline[i] = unicodedata.normalize('NFKD', timeline[i]).encode('ascii','ignore')
            timeline[i] = datetime.datetime.strptime(timeline[i], "%Y-%m-%d") 
         return timeline

    def compute_pre_processing(self, data):
        scale_factor = float(data["scale_factor"])
        missing_value = data["missing_value"]
        values = data["values"]
        N = len(values)
        for i in range(N):
           if values[i]==missing_value:
              values[i] = float('NaN')
           else:
              values[i] = values[i] / float(scale_factor)
        return values

    #def handleMouseDown(self, point, button):
    def plotTimeSeries(self):
        self.dlg.clearTextBrowser()
        # Close existent plot window and clear datasets
        plt.close()
 
        # Get selected product
        product = self.dlg.ui.listWidget_products.currentItem().text()

        # Get selected dataset list
        items = self.dlg.ui.listWidget_datasets.selectedItems()
        if not(items):
           #self.dlg.setTextBrowser(  str("Missing a dataset. Please select one or more datasets.")  ) 
           QMessageBox.information( self.iface.mainWindow(),"Info", "Missing dataset. \nPlease select one or more datasets." )
           return None
        
        datasetsList = []
        for i in list(items):
            datasetsList.append(str(i.text()))
       
        coordinatesString = self.dlg.ui.lineEdit_coordinates.displayText()
        #self.dlg.setTextBrowser(str(coordinatesString))
        
        if coordinatesString=="":
           #self.dlg.setTextBrowser(  str("Missing a dataset. Please select one or more datasets.")  ) 
           QMessageBox.information( self.iface.mainWindow(),"Info", "Missing coordinates. \nPlease either type longitude,latitude or click on the map!" )
           return None
        
        x = float(coordinatesString.split(',', 1 )[0])
        y = float(coordinatesString.split(',', 1 )[1])
        
        #self.dlg.setTextBrowser(str(coordinatesString))
        # create URL with click point
        point = QgsPoint(x,y)
        chronosURL = str("http://www.dpi.inpe.br/mds/mds/query?product="+str(product)+"&datasets="+str(",".join(datasetsList))+
                         "&longitude="+str(point.x())+"&latitude="+str(point.y())+"&output_format=json")

        # Check server connection 
        if not(self.url_exists(chronosURL)):
            self.dlg.setTextBrowser(  str("The server does not respond. Connection timed out for: "+chronosURL)  )
            QMessageBox.information( self.iface.mainWindow(),"Info", "The server does not respond. \nConnection timed out!\n"+chronosURL )
            return None
  
        # get datasets from Chronos
        response = urllib2.urlopen(chronosURL)
        data = json.load(response)
        
        # Check if dataset is valid to plot
        if data["result"]["datasets"][0]["values"]==None:
           QMessageBox.information( self.iface.mainWindow(),"Info", "There are no datasets for this coordinates!\n\nLongitude = "+str(point.x())+", Latitude: "+str(point.y()))
           return None
        
        # Get selected filter
        item = self.dlg.ui.listWidget_filters.currentItem()
        filterType = False
        if item:
           filterType = item.text()
           
        self.dlg.setTextBrowser( "Filter: "+str(filterType) )
        
        # process dates 
        timeline = self.transform_dates(data["result"]["timeline"])

        # Create plot for each dataset
        nDatasets = len(data["result"]["datasets"])
        for j in range(nDatasets):
           datasetName = str(data["result"]["datasets"][j]["dataset"])
           # Check if dataset is valid to plot
           if datasetName!="day2" and datasetName!="day" and datasetName!="day2" and datasetName!="quality" and datasetName!="reliability" and datasetName!="viewangle":
              values = self.compute_pre_processing(data["result"]["datasets"][j])
              plt.plot(timeline, values, '-', linewidth=1, label=str(datasetName))
              if filterType:
                svalues = self.timeSeriesFilter(values, filterType)
                plt.plot(timeline, svalues, '-', linewidth=1, label=str(str(datasetName)+"-"+str(filterType)))

        # Make plot visible
        plt.xlabel("time")
        plt.ylabel("Value")
        plt.ylim(0, 1)
        plt.title("Center coordinates: "+
                  str(data["result"]["center_coordinates"]["longitude"])+
                  ", "+str(data["result"]["center_coordinates"]["latitude"]))
        plt.legend()
        plt.grid(True)
                
        # Maximize window plot
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        plt.show()
        
                
        #self.dlg.setTextBrowser( str("The plot button allows to plot the the time series for the same coordinates selecting a different product and datasets.") )
        #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

    # run method that performs all the real work
    def run(self):
        # set the current layer immediately if it exists, otherwise it will be set on user selection
        self.cLayer = self.iface.mapCanvas().currentLayer()
        if self.cLayer: self.provider = self.cLayer.dataProvider()
        # make our clickTool the tool that we'll use for now
        self.canvas.setMapTool(self.clickTool)

        # show the dialog
        self.dlg.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass