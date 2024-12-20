# Form implementation generated from reading ui file 'GeneratorWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GeneratorWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("GeneratorWindow")
        MainWindow.setFixedSize(550, 300)
        MainWindow.setWindowIcon(QtGui.QIcon('resources/icon.png'))
        buttonStyle = open("styles/commonButtonStyle.css").read()
        editStyle = open("styles/Entry.css").read()
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.bg_label.setGeometry(QtCore.QRect(0, 0, 550, 300))
        self.bg_label.setStyleSheet("background-image: url(resources/second_bg.jpg);")
        self.bg_label.setText("")
        self.bg_label.setObjectName("bg_label")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, 25, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.tasksAmountEntry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tasksAmountEntry.setGeometry(QtCore.QRect(10, 110, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.tasksAmountEntry.setFont(font)
        self.tasksAmountEntry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tasksAmountEntry.setStyleSheet(editStyle)
        self.tasksAmountEntry.setText("")
        self.tasksAmountEntry.setObjectName("tasksAmountEntry")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 90, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.repeatRadio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.repeatRadio.setGeometry(QtCore.QRect(10, 180, 321, 31))
        self.repeatRadio.toggle()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.repeatRadio.setFont(font)
        self.repeatRadio.setStyleSheet("color: white")
        self.repeatRadio.setObjectName("repeatRadio")
        self.generatatorTypeChoice = QtWidgets.QButtonGroup(MainWindow)
        self.generatatorTypeChoice.setObjectName("generatatorTypeChoice")
        self.generatatorTypeChoice.addButton(self.repeatRadio)
        self.withoutRepeatRadio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.withoutRepeatRadio.setGeometry(QtCore.QRect(10, 210, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.withoutRepeatRadio.setFont(font)
        self.withoutRepeatRadio.setStyleSheet("color: white")
        self.withoutRepeatRadio.setObjectName("withoutRepeatRadio")
        self.generatatorTypeChoice.addButton(self.withoutRepeatRadio)
        self.acceptButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.acceptButton.setGeometry(QtCore.QRect(330, 190, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.acceptButton.setFont(font)
        self.acceptButton.setStyleSheet(buttonStyle)
        self.acceptButton.setObjectName("acceptButton")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Генерация заданий в файл word"))
        self.label_3.setText(_translate("MainWindow", "Количество заданий\n"
"(по 5 слов)"))
        self.repeatRadio.setText(_translate("MainWindow", "Задания с повторениями"))
        self.withoutRepeatRadio.setText(_translate("MainWindow", "Задания без повторений"))
        self.acceptButton.setText(_translate("MainWindow", "Сгенерировать"))
