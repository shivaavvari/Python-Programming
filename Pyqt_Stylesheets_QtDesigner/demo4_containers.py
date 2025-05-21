from PyQt6.QtWidgets  import QHBoxLayout,QGroupBox, QPushButton,QWidget,QMainWindow,QApplication, QStyleFactory, QLabel,QVBoxLayout
import sys
# id selector by using #
# container - Qgroupbox
    
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setGeometry(100,100,700,500)
        # create a containers
        box = QGroupBox()
        # create widgets to be added to container
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        # add buttons to a layout
        layout = QVBoxLayout(self)
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Add the above layout for the containers
        box.setLayout(layout)

        # create box
        # create button 
        # create layout
        # add buttons to layout
        # add layout to box
        # add box to mainlayout       

        box2 = QGroupBox()
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
    
        layout2 = QHBoxLayout(self)
        
        layout2.addWidget(button3)
        layout2.addWidget(button4)
    
        box2.setLayout(layout2)

        # Add the above layout for the Qwidget class
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(box)
        main_layout.addWidget(box2)


app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())
