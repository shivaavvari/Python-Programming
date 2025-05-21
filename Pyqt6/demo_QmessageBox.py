from PyQt6.QtWidgets  import  QMainWindow,QMessageBox,QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QPixmap
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,150)
        button = QPushButton("show message",self)
        button.setGeometry(150,80,200,40)
        button.clicked.connect(self.show_message_box)
    
    def show_message_box(self):
        msg= QMessageBox()
        msg.setWindowTitle("Message Box title")
        msg.setText("This is a message box")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons( QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Ok:
            print("OK button clicked")
        else:
            print("Cancel button clicked")
app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
