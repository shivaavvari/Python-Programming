from PyQt6.QtWidgets  import  QWidget, QApplication,QLabel
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,300)
        label = QLabel(self)
        label.setText("Hello World")
        label.move(180,110)

        with open("car.png"):
            image_label = QLabel(self)
            pixmap = QPixmap("car.png")
            image_label.setPixmap(pixmap)
            image_label.move(180,130)

app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())
