import sys
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow, QPushButton, QMenu, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QGraphicsView, QGraphicsScene, QGraphicsItem, QFileDialog
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QPainter, QPen, QBrush, QTextDocument, QImage
from PyQt6.QtCore import QSize, Qt, QRect, QRectF, QPoint

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())