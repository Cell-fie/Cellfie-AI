import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))
        
        '''
        label = QLabel("Welcome to Cellfie AI", self)
        # label.setText("text here lmao")
        label.move(187, 175)
        label.setFont(QFont("Times", 14))
        '''

        '''
        # adding image to label
        label = QLabel(self)
        pixmap = QPixmap("Images/microscope-solid copy.svg")
        label.setPixmap(pixmap)
        '''

        #add gif to label
        label = QLabel(self)
        movie = QMovie("Images/microscope.gif")
        # movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())