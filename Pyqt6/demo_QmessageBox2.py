from PyQt6.QtWidgets  import  QMainWindow, QMessageBox,QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QPixmap
import sys
import math
class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,150)

        number_label = QLabel('Enter a number:',self)
        number_label.move(20,20)

        self.number_input = QLineEdit(self)
        self.number_input.move(150,20)
      
        calculate_button = QPushButton("Find Root",self)
        calculate_button.move(150,60)

        self.result_label = QLabel("Result:",self)
        self.result_label.move(20,100)

        calculate_button.clicked.connect(self.calculate_square_root)

    def calculate_square_root(self):
        try:
            number = float(self.number_input.text())
            square_root = math.sqrt(number)
            if square_root.is_integer():
                self.result_label.setText(f"square root is: {square_root}")
            else:
                QMessageBox.warning(self,"Not a Perfect Square:","This is not a perfect Square")
        except ValueError:
            QMessageBox.warning(self,"Invalid input","Please enter a valid number")


app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
