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
        
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")   
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")

        hbox1 = QHBoxLayout()
        hbox1.addWidget(button1)
        hbox1.addWidget(button2)
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(button3)
        hbox2.addWidget(button4)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)
app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
