from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setup(self, MainWindow):
        MainWindow.setWindowTitle("Second_task")
        MainWindow.resize(750, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 60, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.text=QtWidgets.QLabel(self)
        self.text.setText("Добавьте напоминание")
        self.text.setGeometry(10,10,300,10)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(420, 30, 291, 266))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 310, 500, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Добавить напоминание")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(10, 310, 151, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 391, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



