# Form implementation generated from reading ui file 'ImportLoading.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ImportLoadingWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(490, 140)
        MainWindow.setWindowTitle("Загрузка")
        MainWindow.setWindowIcon(QtGui.QIcon('resources/icon.png'))
        barStyle = open("styles/progressBar.css").read()
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.bg_label.setGeometry(QtCore.QRect(0, 0, 490, 140))
        self.bg_label.setText("")
        self.bg_label.setObjectName("bg_label")
        self.bg_label.setStyleSheet("background-image: url(resources/loading_bg.jpg);")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(70, 80, 350, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet(barStyle)
        self.progressBar.setFormat(" %v / %m")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(155, 20, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Загрузка слов"))
