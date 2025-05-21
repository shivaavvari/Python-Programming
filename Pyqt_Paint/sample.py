from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent, QPainter ,QPen ,QColor
from PyQt6.QtCore import Qt , QRect
#pyuic6 demo.ui -o form.py
import sys



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        self.setMinimumSize(400,400)
        self.setWindowTitle("Paint App")
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(QColor("#ebe834"),5)
        painter.setPen(pen)
        painter.drawPoint(100,100)
        painter.drawLine(0,0,100,100)
        painter.drawRect(100,100,200,200)
        painter.drawEllipse(100,100,200,200)


        painter.end()

app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()