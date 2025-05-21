from PyQt6.QtWidgets  import  QWidget, QApplication,QLabel, QListWidget,QHBoxLayout, QListWidgetItem
from PyQt6.QtGui import QPixmap
import sys

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,700,500)
        fruits =['Apple','Mango','Orange','Banana','Pineapple']
        self.listwidget = QListWidget()
        self.listwidget.setAlternatingRowColors(True)
        
        for fruit in fruits:
            listitem = QListWidgetItem()
            listitem.setText(fruit)
            self.listwidget.addItem(listitem)


        self.layout =QHBoxLayout()
        self.layout.addWidget(self.listwidget)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
