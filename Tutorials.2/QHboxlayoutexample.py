import sys
from PyQt6.QtWidgets import QApplication, QWidget,  QPushButton, QMenu, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))

        hbox = QHBoxLayout()

        btn1 = QPushButton("One")
        btn2 = QPushButton("Two")
        btn3 = QPushButton("Three")
        btn4 = QPushButton("Four")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        self.setLayout(hbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())