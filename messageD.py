from PyQt5 import QtCore, QtGui, QtWidgets

class Message_Ui_Dialog(object):

    def close(self):
        self.Dialog.close()

    def message_setupUi(self, Dialog,message):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.532, y1:0, x2:0.538, y2:1, stop:0 rgba(253, 249, 206, 255), stop:1 rgba(255, 255, 255, 255))")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message_ = message
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(self.close)
        self.verticalLayout.addWidget(self.ok_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Message"))
        self.message.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/>"+self.message_+"</p></body></html>"))
        self.ok_button.setText(_translate("Dialog", "Ok"))



