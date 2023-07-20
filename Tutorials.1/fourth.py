import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))
        self.setStyleSheet('background-color:#008813')
        self.setWindowOpacity(0.75)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())