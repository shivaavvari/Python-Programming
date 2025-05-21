from PyQt6.QtWidgets  import  QWidget, QApplication,QLabel
from PyQt6.QtGui import QPixmap  ,QFont
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,500)

        with open("car.png"):
            image_label = QLabel(self)
            pixmap = QPixmap('car.png')
            image_label.setPixmap(pixmap)
            image_label.move(50,0)
        name_label = QLabel(self)
        name_label.setText("My car")
        name_label.setFont(QFont("Arial", 20))
        name_label.move(200,380)        

        engine_label = QLabel(self)
        engine_label.setText("Engine Capacity : 4L TLSI")
        engine_label.setFont(QFont("Arial", 16))
        engine_label.move(20,420)        

        features_label = QLabel(self)
        features_label.setText("Features : ABS, EBD, ADAS")
        features_label.setFont(QFont("Arial", 16))
        features_label.move(20,450)

        models_label = QLabel(self)
        models_label.setText("$80000")
        models_label.setFont(QFont("Arial", 16))
        models_label.move(20,480)
                


app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())
