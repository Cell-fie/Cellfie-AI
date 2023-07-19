import typing
from PyQt6 import QtCore
import PySimpleGUIQt as sg
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main")

        button = QPushButton("Ok")

        self.setCentralWidget(button)
        self.show()

app = QApplication([])
window = MainWindow()
app.exec()