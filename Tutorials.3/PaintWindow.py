import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMenu, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QGraphicsView, QGraphicsScene, QGraphicsItem, QFileDialog
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QPainter, QPen, QBrush, QTextDocument, QImage
from PyQt6.QtCore import QSize, Qt, QRect, QRectF, QPoint
from PyQt6 import QtGui, uic
from Paint_UI import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        self.image.fill(Qt.GlobalColor.white)

        self.drawing = False
        self.brushSize = 3
        self.brushColor = Qt.GlobalColor.black
        self.lastPoint = QPoint()

        # connecting signals
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionClear.triggered.connect(self.clear)
        self.ui.action3px.triggered.connect(self.threePixel)
        self.ui.action5px.triggered.connect(self.fivePixel)
        self.ui.action7px.triggered.connect(self.sevenPixel)
        self.ui.action9px.triggered.connect(self.ninePixel)
        self.ui.actionBlack.triggered.connect(self.blackColor)
        self.ui.actionWhite.triggered.connect(self.whiteColor)
        self.ui.actionRed.triggered.connect(self.redColor)
        self.ui.actionGreen.triggered.connect(self.greenColor)
        self.ui.actionBlue.triggered.connect(self.blueColor)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            selfdrawing = True
            self.lastPoint = event.position()
            
    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.MouseButton.LeftButton):
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.PenStyle.SolidLine))
            painter.drawLine(self.lastPoint, event.position())
            self.lastPoint = event.position()
            self.update()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);; JPEG(*.jpg *.jpeg);; All Files(*.*)")

        if filePath == "":
            return
        self.image.save(filePath)
    
    def clear(self):
        self.image.fill(Qt.GlobalColor.white)
        self.update()

    def threePixel(self):
        self.brushSize = 3
    def fivePixel(self):
        self.brushSize = 5
    def sevenPixel(self):
        self.brushSize = 7
    def ninePixel(self):
        self.brushSize = 9

    def blackColor(self):
        self.brushColor = Qt.GlobalColor.black
    def whiteColor(self):
        self.brushColor = Qt.GlobalColor.white
    def redColor(self):
        self.brushColor = Qt.GlobalColor.red
    def greenColor(self):
        self.brushColor = Qt.GlobalColor.green
    def blueColor(self):
        self.brushColor = Qt.GlobalColor.blue

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()