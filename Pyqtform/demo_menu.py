from PyQt6.QtWidgets  import  QMainWindow,QWidget, QApplication,QLabel, QMenuBar, QMenu,  QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QPixmap , QAction
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Menu Bar")
        self.setGeometry(100,100,400,300)
        
        #step 1 create a menu bar
        menubar = self.menuBar()
        #step 2 create a menu
        file_menu = menubar.addMenu("File")
        
        #creating an Action 
        self.new_action = QAction("New")

        #Add an action to the menu 
        file_menu.addAction(self.new_action)
        
        # add a separator to the menu
        file_menu.addSeparator()

        
        #creating another action 
        self.exit_action = QAction("Exit")
        file_menu.addAction(self.exit_action)

        #step 3 create a menu
        edit_menu = menubar.addMenu("Edit")
        #creating an Action 
        self.cut_action = QAction("Cut")
        self.copy_action = QAction("Copy")
        self.paste_action = QAction("Paste")

        #Add an action to the menu
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())
