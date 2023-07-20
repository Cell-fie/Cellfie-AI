import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication([])
window = QMainWindow()
window.statusBar().showMessage("Welcome to Cellfie AI!")
window.menuBar().addMenu("File")

window.show()

sys.exit(app.exec())