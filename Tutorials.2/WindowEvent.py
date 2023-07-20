import sys
from PyQt6.QtWidgets import QApplication, QWidget,  QPushButton, QMenu, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize
from PyQt6 import uic
from UI_Event import Ui_Form

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.on_clicked)

    def on_clicked(self):
        value = self.ui.lineEdit.text()
        self.ui.label.setText(value)

        


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()