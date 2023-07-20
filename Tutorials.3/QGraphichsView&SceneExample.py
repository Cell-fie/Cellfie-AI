import sys
from PyQt6.QtWidgets import QApplication, QWidget,  QPushButton, QMenu, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QPainter, QPen, QBrush, QTextDocument
from PyQt6.QtCore import QSize, Qt, QRect, QRectF

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))

        scene = QGraphicsScene(self)

        greenBrush = QBrush(Qt.GlobalColor.green)
        redBrush = QBrush(Qt.GlobalColor.red)

        yellowPen = QPen(Qt.GlobalColor.yellow)
        yellowPen.setWidth(7)

        ellipse = scene.addEllipse(100,100,200,200,yellowPen, redBrush)
        rect = scene.addRect(-100,-100,200,200,yellowPen,greenBrush)

        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        view = QGraphicsView(scene,self)
        view.setGeometry(0,0,680,400)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())