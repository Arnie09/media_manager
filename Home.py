

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def openFolder(self):
        self.name = QtWidgets.QFileDialog.getExistingDirectory(self.MainWindow, "Select Directory")
        print(self.name)


    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 835)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.532, y1:0, x2:0.538, y2:1, stop:0 rgba(253, 249, 206, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.movie_list_view = QtWidgets.QListView(self.centralwidget)
        self.movie_list_view.setGeometry(QtCore.QRect(10, 150, 371, 621))
        self.movie_list_view.setStyleSheet("background:rgb(255, 255, 255)")
        self.movie_list_view.setObjectName("movie_list_view")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 251, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.label_2.setObjectName("label_2")
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(10, 30, 371, 22))
        self.search_input.setObjectName("search_input")

        '''combo box to put some features by which we will search the movies'''
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 221, 22))
        self.comboBox.setObjectName("comboBox")

        '''search button to search things'''
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(240, 60, 141, 28))
        self.search_button.setObjectName("search_button")

        '''refresh button to refresh looking for changes in files'''
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(290, 110, 93, 28))
        self.refresh_button.setObjectName("refresh_button")

        '''to display pictures of the film'''
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(520, 30, 256, 192))
        self.graphicsView.setStyleSheet("background:rgb(255, 255, 255)")
        self.graphicsView.setObjectName("graphicsView")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 260, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 290, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 320, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 350, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 380, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 450, 55, 16))
        self.label_8.setObjectName("label_7")

        self.name_ = QtWidgets.QLabel(self.centralwidget)
        self.name_.setGeometry(QtCore.QRect(490, 260, 331, 16))
        self.name_.setText("")
        self.name_.setObjectName("name_")

        self.release_date_ = QtWidgets.QLabel(self.centralwidget)
        self.release_date_.setGeometry(QtCore.QRect(520, 290, 351, 16))
        self.release_date_.setText("")
        self.release_date_.setObjectName("release_date_")

        self.language_ = QtWidgets.QLabel(self.centralwidget)
        self.language_.setGeometry(QtCore.QRect(500, 320, 351, 16))
        self.language_.setText("")
        self.language_.setObjectName("language_")

        self.Director_ = QtWidgets.QLabel(self.centralwidget)
        self.Director_.setGeometry(QtCore.QRect(500, 350, 351, 16))
        self.Director_.setText("")
        self.Director_.setObjectName("Director_")

        self.Rating_ = QtWidgets.QLabel(self.centralwidget)
        self.Rating_.setGeometry(QtCore.QRect(500, 380, 351, 16))
        self.Rating_.setText("")
        self.Rating_.setObjectName("Rating_")

        self.Synopsis_ = QtWidgets.QLabel(self.centralwidget)
        self.Synopsis_.setGeometry(QtCore.QRect(490, 410, 371, 171))
        self.Synopsis_.setText("")
        self.Synopsis_.setObjectName("Synopsis_")

        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(600, 710, 93, 28))
        self.play_button.setObjectName("play_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openFolder)

        self.actionAbout_Media_Manager = QtWidgets.QAction(MainWindow)
        self.actionAbout_Media_Manager.setObjectName("actionAbout_Media_Manager")

        self.menuFile.addAction(self.actionOpen)
        self.menuAbout.addAction(self.actionAbout_Media_Manager)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Media Manager"))
        self.label.setText(_translate("MainWindow", "All Media:"))
        self.label_2.setText(_translate("MainWindow", "Search:"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.refresh_button.setText(_translate("MainWindow", "Refresh"))
        self.label_3.setText(_translate("MainWindow", "Name :"))
        self.label_4.setText(_translate("MainWindow", "Release Date:"))
        self.label_5.setText(_translate("MainWindow", "Language:"))
        self.label_6.setText(_translate("MainWindow", "Director/s:"))
        self.label_7.setText(_translate("MainWindow", "Rating:"))
        self.label_8.setText(_translate("MainWindow", "Synopsis:"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionAbout_Media_Manager.setText(_translate("MainWindow", "About Media Manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
