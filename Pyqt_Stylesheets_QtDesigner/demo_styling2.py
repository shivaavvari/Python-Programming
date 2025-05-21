from PyQt6.QtWidgets  import QPushButton,QWidget,QMainWindow,QApplication, QStyleFactory, QLabel,QVBoxLayout
import sys
# id selector by using #
stylesheet = """
        QPushButton#My_Button{
            background-color:grey;
            padding:5px;
                }
        QPushButton#My_Button:pressed{
            background-color:blue;
            padding:5px;
            }
        QLabel#My_Label{
            background-color:red;
            color:white;
            margin-top:100px;
            margin-bottom:100px;
            margin-left:100px;
            margin-right:100px;
            margin:100px;
        
        }
        """

    
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setGeometry(100,100,700,500)

        label = QLabel("<h1> This is a Label  </h1>",self)
        label.resize(200,50)
        label.setObjectName("My_Label")

        button = QPushButton("Click Here")
        button.setObjectName("My_Button")


        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)     

        
      

app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = Window()
window.show()


sys.exit(app.exec())
