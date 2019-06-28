# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Scan.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Scan_Dialog(object):
    def setupUi(self, Scan_Dialog):
        Scan_Dialog.setObjectName("Scan_Dialog")
        Scan_Dialog.resize(515, 142)
        self.verticalLayout = QtWidgets.QVBoxLayout(Scan_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Scan_Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(Scan_Dialog)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Scan_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Scan_Dialog)

    def retranslateUi(self, Scan_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Scan_Dialog.setWindowTitle(_translate("Scan_Dialog", "Scanning"))
        self.label.setText(_translate("Scan_Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Please wait</span><span style=\" font-size:10pt; font-weight:600;\"> while we scan your system for media files.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Scan_Dialog = QtWidgets.QDialog()
    ui = Ui_Scan_Dialog()
    ui.setupUi(Scan_Dialog)
    Scan_Dialog.show()
    sys.exit(app.exec_())

