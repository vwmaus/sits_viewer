# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sits_viewer.ui'
#
# Created: Wed Mar 18 17:27:29 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_sits_viewer(object):
    def setupUi(self, sits_viewer):
        sits_viewer.setObjectName(_fromUtf8("sits_viewer"))
        sits_viewer.resize(361, 332)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sits_viewer.sizePolicy().hasHeightForWidth())
        sits_viewer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        sits_viewer.setFont(font)
        self.txtFeedback = QtGui.QTextBrowser(sits_viewer)
        self.txtFeedback.setGeometry(QtCore.QRect(0, 260, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtFeedback.setFont(font)
        self.txtFeedback.setObjectName(_fromUtf8("txtFeedback"))
        self.groupBox_datasets = QtGui.QGroupBox(sits_viewer)
        self.groupBox_datasets.setGeometry(QtCore.QRect(120, 10, 241, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_datasets.setFont(font)
        self.groupBox_datasets.setObjectName(_fromUtf8("groupBox_datasets"))
        self.listWidget_datasets = QtGui.QListWidget(self.groupBox_datasets)
        self.listWidget_datasets.setGeometry(QtCore.QRect(10, 20, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_datasets.setFont(font)
        self.listWidget_datasets.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_datasets.setObjectName(_fromUtf8("listWidget_datasets"))
        self.pushButton_showcoverages = QtGui.QPushButton(self.groupBox_datasets)
        self.pushButton_showcoverages.setGeometry(QtCore.QRect(10, 100, 141, 24))
        self.pushButton_showcoverages.setObjectName(_fromUtf8("pushButton_showcoverages"))
        self.groupBox_products = QtGui.QGroupBox(sits_viewer)
        self.groupBox_products.setGeometry(QtCore.QRect(0, 10, 121, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_products.setFont(font)
        self.groupBox_products.setObjectName(_fromUtf8("groupBox_products"))
        self.listWidget_products = QtGui.QListWidget(self.groupBox_products)
        self.listWidget_products.setGeometry(QtCore.QRect(10, 20, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_products.setFont(font)
        self.listWidget_products.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_products.setObjectName(_fromUtf8("listWidget_products"))
        self.buttonBox = QtGui.QDialogButtonBox(sits_viewer)
        self.buttonBox.setGeometry(QtCore.QRect(190, 310, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit_coordinates = QtGui.QLineEdit(sits_viewer)
        self.lineEdit_coordinates.setGeometry(QtCore.QRect(0, 150, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_coordinates.setFont(font)
        self.lineEdit_coordinates.setObjectName(_fromUtf8("lineEdit_coordinates"))
        self.label = QtGui.QLabel(sits_viewer)
        self.label.setGeometry(QtCore.QRect(6, 133, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_plot = QtGui.QPushButton(sits_viewer)
        self.pushButton_plot.setGeometry(QtCore.QRect(240, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_plot.setFont(font)
        self.pushButton_plot.setObjectName(_fromUtf8("pushButton_plot"))
        self.groupBox_period = QtGui.QGroupBox(sits_viewer)
        self.groupBox_period.setGeometry(QtCore.QRect(0, 180, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_period.setFont(font)
        self.groupBox_period.setObjectName(_fromUtf8("groupBox_period"))
        self.label_3 = QtGui.QLabel(self.groupBox_period)
        self.label_3.setGeometry(QtCore.QRect(10, 45, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dateEdit_startDate = QtGui.QDateEdit(self.groupBox_period)
        self.dateEdit_startDate.setGeometry(QtCore.QRect(75, 20, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_startDate.setFont(font)
        self.dateEdit_startDate.setObjectName(_fromUtf8("dateEdit_startDate"))
        self.dateEdit_endDate = QtGui.QDateEdit(self.groupBox_period)
        self.dateEdit_endDate.setGeometry(QtCore.QRect(75, 44, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_endDate.setFont(font)
        self.dateEdit_endDate.setDate(QtCore.QDate(2014, 6, 1))
        self.dateEdit_endDate.setObjectName(_fromUtf8("dateEdit_endDate"))
        self.label_2 = QtGui.QLabel(self.groupBox_period)
        self.label_2.setGeometry(QtCore.QRect(5, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_save = QtGui.QPushButton(sits_viewer)
        self.pushButton_save.setGeometry(QtCore.QRect(240, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.pushButton_clear_points = QtGui.QPushButton(sits_viewer)
        self.pushButton_clear_points.setGeometry(QtCore.QRect(240, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_clear_points.setFont(font)
        self.pushButton_clear_points.setObjectName(_fromUtf8("pushButton_clear_points"))

        self.retranslateUi(sits_viewer)
        QtCore.QObject.connect(self.pushButton_plot, QtCore.SIGNAL(_fromUtf8("clicked()")), sits_viewer.update)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), sits_viewer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), sits_viewer.reject)
        QtCore.QMetaObject.connectSlotsByName(sits_viewer)

    def retranslateUi(self, sits_viewer):
        sits_viewer.setWindowTitle(_translate("sits_viewer", "sits_viewer", None))
        self.txtFeedback.setHtml(_translate("sits_viewer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_datasets.setTitle(_translate("sits_viewer", "Coverages", None))
        self.pushButton_showcoverages.setText(_translate("sits_viewer", "Show coverages", None))
        self.groupBox_products.setTitle(_translate("sits_viewer", "Products", None))
        self.label.setText(_translate("sits_viewer", "Longitude, Latitude:", None))
        self.pushButton_plot.setText(_translate("sits_viewer", "Plot", None))
        self.groupBox_period.setTitle(_translate("sits_viewer", "Period", None))
        self.label_3.setText(_translate("sits_viewer", "End date:", None))
        self.dateEdit_startDate.setDisplayFormat(_translate("sits_viewer", "MM/dd/yyyy", None))
        self.dateEdit_endDate.setDisplayFormat(_translate("sits_viewer", "MM/dd/yyyy", None))
        self.label_2.setText(_translate("sits_viewer", "Start date:", None))
        self.pushButton_save.setText(_translate("sits_viewer", "Save csv", None))
        self.pushButton_clear_points.setText(_translate("sits_viewer", "Clear points", None))

