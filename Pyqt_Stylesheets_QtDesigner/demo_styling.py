from PyQt6.QtWidgets  import QMainWindow,QApplication, QStyleFactory
import sys

    
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("styling")
        self.setGeometry(100,100,700,500)
     
      

app = QApplication(sys.argv)
app.setStyle('Fusion')
window = Window()
print(QStyleFactory.keys())
print(app.style)
window.show()


sys.exit(app.exec())
