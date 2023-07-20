import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(200,200, 500,400)
        self.setWindowIcon(QIcon("Images/microscope-solid copy.svg"))

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Times", 14))
        # line_edit.setText("Default Text")
        line_edit.setPlaceholderText("Write Here...")
        # line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())