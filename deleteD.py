from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Delete_Dialog(object):

    def yes_function(self):
        self.parent.delete_surerity = "YES"
        self.Delete_dialog.close()

    def cancel_function(self):
        self.Delete_dialog.close()

    def setupUi(self, Delete_Dialog,parent_instance):
        self.Delete_dialog = Delete_Dialog
        self.parent = parent_instance
        Delete_Dialog.setObjectName("Delete_Dialog")
        Delete_Dialog.resize(400, 200)
        Delete_Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.532, y1:0, x2:0.538, y2:1, stop:0 rgba(253, 249, 206, 255), stop:1 rgba(255, 255, 255, 255))")
        self.verticalLayout = QtWidgets.QVBoxLayout(Delete_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Delete_Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_button = QtWidgets.QPushButton(Delete_Dialog)
        self.yes_button.setObjectName("yes_button")
        self.yes_button.clicked.connect(self.yes_function)

        self.horizontalLayout.addWidget(self.yes_button)
        self.cancel_button = QtWidgets.QPushButton(Delete_Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(self.cancel_function)

        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Delete_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Delete_Dialog)

    def retranslateUi(self, Delete_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Delete_Dialog.setWindowTitle(_translate("Delete_Dialog", "Delete file"))
        self.label.setText(_translate("Delete_Dialog", "<html><head/><body><p align=\"center\">Are you sure you want to delete this file from the records?</p></body></html>"))
        self.yes_button.setText(_translate("Delete_Dialog", "Yes"))
        self.cancel_button.setText(_translate("Delete_Dialog", "Cancel"))
