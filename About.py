from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def close(self):
        self.Dialog.close()

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 344)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(self.close)

        self.verticalLayout.addWidget(self.ok_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About Media Manager"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">The ultimate goal of this software is to act as a media tool for the user. </p><p align=\"center\"><br/></p><p align=\"center\">This had been made so that the user can access all his media files efficiently and                                 smoothly.</p><p align=\"center\"><br/></p><p align=\"center\">     Created by Arnab Chanda  © 2019</p></body></html>"))
        self.ok_button.setText(_translate("Dialog", "Ok"))


