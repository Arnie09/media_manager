

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_(object):

    def close(self):
        self.Dialog.close()

    def setupUi_(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(592, 373)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.532, y1:0, x2:0.538, y2:1, stop:0 rgba(253, 249, 206, 255), stop:1 rgba(255, 255, 255, 255))")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
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
        Dialog.setWindowTitle(_translate("Dialog", "Scan Complete!"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Scan Complete! </span></p><p align=\"center\"><br/></p><p align=\"center\">We will down download the information on the movies 50 at a time one by one in background. </p><p align=\"center\">DONOT TRY TO DOWNLOAD ALL THE INFORMATION AT ONCE. <br/></p><p align=\"center\">You can close this window and keep using the application.</p></body></html>"))
        self.ok_button.setText(_translate("Dialog", "Ok"))



