from PyQt6.QtWidgets import QMainWindow, QApplication
#pyuic6 demo.ui -o form.py
from form import Ui_Form
import sys
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,400,300)
        self.ui.lineEdit.setMaxLength(8)
        self.ui.lineEdit_2.setMaxLength(8)

        self.ui.pushButton.clicked.connect(self.check)
    
    def check(self):
        username =  self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username == "admin" and password =="admin123":
            print("Valid username and password"
                  )
        else:
            print("Invalid username and password")



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()