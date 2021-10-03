import sys
import os.path
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface2 import MainWindow


class MyWidget(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setup(self)
        self.open_file()
        self.pushButton.clicked.connect(self.run)




    def run(self):
        f = open('event.txt', 'a')
        date = self.calendarWidget.selectedDate()
        data = date.toString('yyyy.MM.dd') + " " + self.timeEdit.text()  + " " + self.lineEdit.text()
        self.listWidget.insertItem(1, data+"\n")
        self.listWidget.sortItems()
        f.write(data+"\n")
        f.close()

    def open_file(self):
        if os.path.isfile('event.txt'):
            f = open('event.txt', 'r')
            data = f.readlines()
            print(data)
            for i in range(len(data)):
                self.listWidget.insertItem(1, data[i])
            self.listWidget.isSortingEnabled()
            f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
