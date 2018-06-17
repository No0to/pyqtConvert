import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Converter - Made by Thou'
        self.left = 10
        self.top = 10
        self.width = 342
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.l1 = QtWidgets.QLabel(self) # Creates a label. The (w) tells the program that we want the label in the window.
        self.l1.setText('Type in the text box what you want to convert') # Tells the program what you want the label to say.
        self.l1.move(20, 20) # How close to the left and top the label is.

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 54)
        self.textbox.resize(280,20)

        # Create a button in the window
        self.button = QPushButton('Convert!', self)
        self.button.move(20,90)

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
