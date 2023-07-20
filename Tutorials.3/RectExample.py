import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QWidget,  QPushButton, QMenu, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QPainter, QPen, QBrush
from PyQt6.QtCore import QSize, Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.darkGreen, 5, Qt.PenStyle.DotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.BDiagPattern))
        painter.drawRect(100,15,300,100)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())