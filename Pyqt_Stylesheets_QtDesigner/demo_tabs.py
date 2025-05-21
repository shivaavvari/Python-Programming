from PyQt6.QtWidgets  import QTabWidget,QHBoxLayout,QGroupBox, QPushButton,QWidget,QMainWindow,QApplication, QStyleFactory, QLabel,QVBoxLayout
import sys
# id selector by using #
# container - Qgroupbox
# QTab widget    
class Window(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setGeometry(100,100,700,500)
    #creating a tab widget
        tab_widget = QTabWidget()

    #create tab
        tab1 = QWidget()
        tab2 = QWidget()
    #Add above tab 
        tab_widget.addTab(tab1,"tab1")
        tab_widget.addTab(tab2,"tab2")
    #create widgets to add to tabs
        button1 = QPushButton('button1') 

        button2 = QPushButton('button2')

    # create layout to add buttons and add then to the tabs
        layout1 = QVBoxLayout()
        layout1.addWidget(button1)
        layout2 = QVBoxLayout()
        layout2.addWidget(button2)
    # setting the tab layout1 and layout2 
        tab1.setLayout(layout1)
        tab2.setLayout(layout2)



    # add it to the main window after creating a layout
        layout = QVBoxLayout(self)
        
        layout.addWidget(tab_widget)
        self.setLayout(layout)



app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())
