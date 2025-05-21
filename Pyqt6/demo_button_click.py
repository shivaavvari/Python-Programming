from PyQt6.QtWidgets  import  QWidget, QApplication,QLabel, QPushButton
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        self.count =0  
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,400)
        # adding label to display count
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.move(200,200)
        
        button = QPushButton(self)
        button.setText("Click here")
        button.move(100,200)

        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Button Clicked")
        self.count += 1
        self.label.setText(str(self.count))
        self.label.adjustSize()

app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
