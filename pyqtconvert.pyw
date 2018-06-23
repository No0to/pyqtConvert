import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtCore import pyqtSlot, Qt, QUrl

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Converter'
        self.left = 10
        self.top = 10
        self.width = 342
        self.height = 110
        self.initUI()

    def initUI(self):
        self.setFixedSize(342, 110)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Celsius to Fahrenheit')
        self.l1.move(20, 0)

        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Made by Thou')
        self.l2.setStyleSheet('color: #c1c1c1')
        self.l2.move(273, 88)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 34)
        self.textbox.resize(280,20)

        # Create a button in the window
        self.button = QPushButton('Convert!', self)
        self.button.move(20,70)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        conversion = float(textboxValue)*1.8+32
        self.textbox.setText("")
        self.l1.setText(str(conversion))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
