# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sits_viewerDialog
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

from PyQt4 import QtCore, QtGui
from ui_sits_viewer import Ui_sits_viewer
# create the dialog for zoom to point


class sits_viewerDialog(QtGui.QDialog, Ui_sits_viewer):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_sits_viewer()
        self.ui.setupUi(self)

    def setTextBrowser(self, output):
        self.ui.txtFeedback.setText(output)

    def clearTextBrowser(self):
        self.ui.txtFeedback.clear()

    def setTextCoordinates(self, output):
        self.ui.lineEdit_coordinates.setText(output)
            
    def clearTextCoordinates(self):
        self.ui.lineEdit_coordinates.clear()

    def setTextClassname(self, output):
        self.ui.lineEdit_classname.setText(output)
            
    def clearTextClassname(self):
        self.ui.lineEdit_classname.clear()
        
    def addProducts(self, output):
        self.ui.listWidget_products.addItem(output)
    
    def clearProducts(self):
        self.ui.listWidget_products.clear()
        
    def addDatasets(self, output):
        self.ui.listWidget_datasets.addItem(output)
    
    def clearDatasets(self):
        self.ui.listWidget_datasets.clear()
        
    def addFilters(self, output):
        self.ui.listWidget_filters.addItem(output)
    
    def clearFilters(self):
        self.ui.listWidget_filters.clear()
    

    