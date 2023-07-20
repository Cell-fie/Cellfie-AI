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
        painter.setPen(QPen(Qt.GlobalColor.darkRed, 5, Qt.PenStyle.DashLine))
        painter.setBrush(QBrush(Qt.GlobalColor.red, Qt.BrushStyle.HorPattern))
        painter.drawEllipse(100,100,400,200)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())