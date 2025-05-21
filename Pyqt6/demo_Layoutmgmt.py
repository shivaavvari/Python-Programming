from PyQt6.QtWidgets  import   QVBoxLayout, QHBoxLayout, QMainWindow, QMessageBox,QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QPixmap
import sys
import math
class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,150)
        
        label = QLabel("Name")
        name = QLineEdit()
        button = QPushButton("Add ")
        layout = QVBoxLayout()
        #layout = QHBoxLayout()
        layout.addWidget(label) 
        layout.addWidget(name)
        layout.addWidget(button)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
