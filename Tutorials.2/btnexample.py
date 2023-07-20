import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPushButton")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))

        btn = QPushButton("Click", self)
        btn.setGeometry(200, 150,100,100)
        btn.setFont(QFont("Times", 14))
        btn.setIcon(QIcon("images/microscope-solid copy.svg"))
        btn.setIconSize(QSize(25,25))

        # popup menu
        menu = QMenu()
        menu.setFont(QFont("Times", 14))
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")

        btn.setMenu(menu)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())