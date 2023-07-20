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

        vbox = QVBoxLayout()

        btn = QPushButton("Change!")
        btn.clicked.connect(self.change_text)

        self.label = QLabel("Hello")

        vbox.addWidget(btn)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def change_text(self):
        self.label.setText("Welcome to Cellfie AI")
        self.label.setFont(QFont("Times", 50))
        self.label.setStyleSheet("color:#008813")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())