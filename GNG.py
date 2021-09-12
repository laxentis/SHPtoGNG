# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GNG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from SHP import readGEO, readRegion
import os


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 295)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 260, 391, 31))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ICAO = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ICAO.setObjectName("ICAO")
        self.verticalLayout.addWidget(self.ICAO)
        self.selectRegionButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.selectRegionButton.setObjectName("selectRegionButton")
        self.selectRegionButton.clicked.connect(self.getSHPRegion)
        self.verticalLayout.addWidget(self.selectRegionButton)
        self.regionPath = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.regionPath.setEnabled(False)
        self.regionPath.setObjectName("regionPath")
        self.verticalLayout.addWidget(self.regionPath)
        self.selectGeoButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.selectGeoButton.setObjectName("selectGeoButton")
        self.selectGeoButton.clicked.connect(self.getSHPgeo)
        self.verticalLayout.addWidget(self.selectGeoButton)
        self.geoPath = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.geoPath.setEnabled(False)
        self.geoPath.setObjectName("geoPath")
        self.verticalLayout.addWidget(self.geoPath)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.generateGNG)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.resetForm)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Shapefile converter"))
        self.ICAO.setPlaceholderText(_translate("Dialog", "ICAO code of the airfield"))
        self.selectRegionButton.setText(_translate("Dialog", "Select Region SHP"))
        self.regionPath.setPlaceholderText(_translate("Dialog", "Path to region shapefile"))
        self.selectGeoButton.setText(_translate("Dialog", "Select GEO SHP"))
        self.geoPath.setPlaceholderText(_translate("Dialog", "Path to GEO shapefile"))

    def getSHPRegion(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            caption='Select SHP file:',
            filter='ESRI Shapefile (*.shp)',
            )
        self.regionPath.setText(filename)

    def getSHPgeo(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            caption='Select SHP file:',
            filter='ESRI Shapefile (*.shp)',
            )
        self.geoPath.setText(filename)

    def resetForm(self):
        self.ICAO.setText("")
        self.regionPath.setText("")
        self.geoPath.setText("")
        self.progressBar.setValue(0)

    def generateGNG(self):
        if self.regionPath.text() != "":
            readRegion(self.regionPath.text(), self.ICAO.text())
        if self.geoPath.text() != "":
            readGEO(self.geoPath.text(), self.ICAO.text())
        self.progressBar.setValue(100)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
