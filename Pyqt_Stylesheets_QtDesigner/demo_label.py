from PyQt6.QtWidgets  import QWidget,QMainWindow,QApplication, QStyleFactory, QLabel,QVBoxLayout
import sys

    
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setGeometry(100,100,700,500)
        label = QLabel("<h1><font color='red'> This is a Label  </h1>",self)
        label.resize(200,50)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)     

        
      

app = QApplication(sys.argv)

window = Window()
window.show()


sys.exit(app.exec())
