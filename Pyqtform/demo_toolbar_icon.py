from PyQt6.QtWidgets  import  QMainWindow,QWidget, QApplication,QLabel, QMenuBar, QMenu,  QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QPixmap , QAction ,QIcon
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Menu Bar")
        self.setGeometry(100,100,400,300)
        
        toolbar = self.addToolBar("Main Toolbar ")
        self.new_action = QAction(QIcon("icons/new.png"),"New")
        toolbar.addAction(self.new_action)

        self.open_action = QAction(QIcon("icons/open.png"),"Open")
        toolbar.addAction(self.open_action)

        toolbar.addSeparator()
        self.save_action = QAction(QIcon("icons/save.png"),"Save")
        toolbar.addAction(self.save_action)

        toolbar.addSeparator()

app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())
