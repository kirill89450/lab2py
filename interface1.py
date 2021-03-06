from PyQt5 import QtCore, QtWidgets


class MainWindow(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("First_Task")
        MainWindow.resize(550, 500)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Первая полоса")
        self.main_text.move(30, 40)

        self.main_text2 = QtWidgets.QLabel(self)
        self.main_text2.setText("Вторая полоса")
        self.main_text2.move(170, 40)

        self.main_text3 = QtWidgets.QLabel(self)
        self.main_text3.setText("Третья полоса")
        self.main_text3.move(310, 40)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 280, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 101, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.verticalLayout.addWidget(self.radioButton_4)

        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup.addButton(self.radioButton_5)
        self.verticalLayout.addWidget(self.radioButton_5)

        self.radioButton_6 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup.addButton(self.radioButton_6)
        self.verticalLayout.addWidget(self.radioButton_6)


        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 70, 101, 171))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.radioButton_7 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_7.setObjectName("radioButton_7")

        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_7)
        self.verticalLayout_2.addWidget(self.radioButton_7)

        self.radioButton_8 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup_2.addButton(self.radioButton_8)
        self.verticalLayout_2.addWidget(self.radioButton_8)

        self.radioButton_9 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_9.setObjectName("radioButton_9")
        self.buttonGroup_2.addButton(self.radioButton_9)
        self.verticalLayout_2.addWidget(self.radioButton_9)

        self.radioButton_10 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_10.setObjectName("radioButton_10")
        self.buttonGroup_2.addButton(self.radioButton_10)
        self.verticalLayout_2.addWidget(self.radioButton_10)

        self.radioButton_11 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_11.setObjectName("radioButton_11")
        self.buttonGroup_2.addButton(self.radioButton_11)
        self.verticalLayout_2.addWidget(self.radioButton_11)

        self.radioButton_12 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_12.setObjectName("radioButton_12")
        self.buttonGroup_2.addButton(self.radioButton_12)
        self.verticalLayout_2.addWidget(self.radioButton_12)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(310, 70, 101, 171))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_13 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_13.setObjectName("radioButton_13")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_13)
        self.verticalLayout_3.addWidget(self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_14.setObjectName("radioButton_14")
        self.buttonGroup_3.addButton(self.radioButton_14)
        self.verticalLayout_3.addWidget(self.radioButton_14)
        self.radioButton_15 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_15.setObjectName("radioButton_15")
        self.buttonGroup_3.addButton(self.radioButton_15)
        self.verticalLayout_3.addWidget(self.radioButton_15)
        self.radioButton_16 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_16.setObjectName("radioButton_16")
        self.buttonGroup_3.addButton(self.radioButton_16)
        self.verticalLayout_3.addWidget(self.radioButton_16)
        self.radioButton_17 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_17.setObjectName("radioButton_17")
        self.buttonGroup_3.addButton(self.radioButton_17)
        self.verticalLayout_3.addWidget(self.radioButton_17)
        self.radioButton_18 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_18.setObjectName("radioButton_18")
        self.buttonGroup_3.addButton(self.radioButton_18)
        self.verticalLayout_3.addWidget(self.radioButton_18)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 285, 271, 71))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать"))

        self.radioButton.setText(_translate("MainWindow", "Белый"))
        self.radioButton_2.setText(_translate("MainWindow", "Синий"))
        self.radioButton_3.setText(_translate("MainWindow", "Красный"))
        self.radioButton_4.setText(_translate("MainWindow", "Чёрный"))
        self.radioButton_5.setText(_translate("MainWindow", "Зелёный"))
        self.radioButton_6.setText(_translate("MainWindow", "Фиолетовый"))
        self.radioButton_7.setText(_translate("MainWindow", "Белый"))
        self.radioButton_8.setText(_translate("MainWindow", "Синий"))
        self.radioButton_9.setText(_translate("MainWindow", "Красный"))
        self.radioButton_10.setText(_translate("MainWindow", "Чёрный"))
        self.radioButton_11.setText(_translate("MainWindow", "Зелёный"))
        self.radioButton_12.setText(_translate("MainWindow", "Фиолетовый"))
        self.radioButton_13.setText(_translate("MainWindow", "Белый"))
        self.radioButton_14.setText(_translate("MainWindow", "Синий"))
        self.radioButton_15.setText(_translate("MainWindow", "Красный"))
        self.radioButton_16.setText(_translate("MainWindow", "Чёрный"))
        self.radioButton_17.setText(_translate("MainWindow", "Зелёный"))
        self.radioButton_18.setText(_translate("MainWindow", "Фиолетовый"))