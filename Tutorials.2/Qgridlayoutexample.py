import sys
from PyQt6.QtWidgets import QApplication, QWidget,  QPushButton, QMenu, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6.QtCore import QSize

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))

        grid = QGridLayout()

        btn1 = QPushButton("One")
        btn2 = QPushButton("Two")
        btn3 = QPushButton("Three")
        btn4 = QPushButton("Four")
        btn5 = QPushButton("Five")
        btn6 = QPushButton("Six")
        btn7 = QPushButton("Seven")
        btn8 = QPushButton("Eight")


        # grid.addWidget(widget, row, column)
        grid.addWidget(btn1, 0,0)
        grid.addWidget(btn2, 1,0)
        grid.addWidget(btn3,2,0)
        grid.addWidget(btn4,3,0)
        grid.addWidget(btn5,0,1)
        grid.addWidget(btn6,1,1)
        grid.addWidget(btn7,2,1)
        grid.addWidget(btn8,3,1)

        self.setLayout(grid)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())