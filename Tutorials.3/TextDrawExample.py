import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QWidget,  QPushButton, QMenu, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QPainter, QPen, QBrush, QTextDocument
from PyQt6.QtCore import QSize, Qt, QRect, QRectF

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawText(100,100, "Cellfie AI")

        rect = QRect(100,150,250,25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "Welcome")

        document = QTextDocument()
        rect2 =  QRectF(0,0,250,250)
        document.setTextWidth(rect2.width())
        document.setHtml("<b>Welcome to Cellfie AI Software</b><i> Enjoy!</i> \n <font size = '15' color = '#008813'>Please leave good review</font>")
        document.drawContents(painter, rect2)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())