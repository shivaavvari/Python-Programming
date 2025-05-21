from PyQt6.QtWidgets  import  QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,160)
       
        # adding label
        sugar_checkbox  = QCheckBox(self)    
        sugar_checkbox.setText("Sugar")
        sugar_checkbox.move(20,40)
        sugar_checkbox.toggled.connect(self.sugar_checked)

        self.label = QLabel(self)
        self.label.setText("")
        self.label.resize(200,20)
        self.label.move(20,90)


    def sugar_checked(self,checked):
        if checked:
            print("Sugar is added")
            self.label.setText("Sugar is Added")
        else:
            print("Sugar is notadded")
            self.label.setText("Sugar is not Added")




app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
