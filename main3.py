import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from interface3 import MainWindow


class MyWidget(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setup(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        name = self.lineEdit.text()
        phone = self.lineEdit_2.text()
        self.listWidget.insertItem(1, name + " --- " + phone)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())