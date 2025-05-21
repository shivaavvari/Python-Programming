from PyQt6.QtWidgets  import  QGridLayout, QHBoxLayout,QVBoxLayout,QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QPixmap
import sys
from PyQt6.QtCore import Qt

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    

    def initUI(self):  
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,160)
       
        # adding label
        layout = QGridLayout()
        self.setLayout(layout)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        layout.addWidget(self.display,0,0,1,4)

        buttons = [QPushButton(str(i)) for i in range(10)]
        for i,button in enumerate(buttons):
        
            row , col = divmod(i,3)
            layout.addWidget(button, row+1, col)
        
        # Adding event handlers to buttons 
        for button in buttons:
            button.clicked.connect(self.number_button_click)

        operators = ['+', '-', '*', '/']
        operator_buttons = [QPushButton(op) for op in operators]
        for i,operator_button in enumerate(operator_buttons):
            layout.addWidget(operator_button, i+1, 3)
        for button in operator_buttons:
            button.clicked.connect(self.operator_button_click)
        
        
        
        self.equals_button = QPushButton("=")
        self.equals_button.clicked.connect(self.calculate)

        self.clear_button = QPushButton("C")
        self.clear_button.clicked.connect(self.clear)
    
        layout.addWidget(self.equals_button, 4, 1)
        layout.addWidget(self.clear_button, 4, 2)
    
    def number_button_click(self):
        digit  = self.sender().text()
        if self.current_input=="0":
            self.current_input = digit
        else:
            # not adding but appending as a string
            self.current_input = self.current_input + digit
        self.display.setText(self.current_input)
    
    def operator_button_click(self):
        operator = self.sender().text()
        if self.current_operator=="":
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = "0"
        else:
            #calculate the result 
            self.calculate()
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = "0"
    def calculate(self):
        if self.current_operator == "+":
            result = str(float(self.previous_input) + float(self.current_input))
        elif self.current_operator == "-":
            result = str(float(self.previous_input) - float(self.current_input))
        elif self.current_operator == "*":
            result = str(float(self.previous_input) * float(self.current_input))
        elif self.current_operator == "/":
            if self.current_input == "0":
                result="Erro4"
            else:
                result = str(float(self.previous_input) / float(self.current_input))
        
        else:
            result = str(self.current_input) 
        self.display.setText(str(result)) 
        self.current_input = result
        self.current_operator = ""
    def clear(self):
        self.current_operator = ""
        self.previous_input = ""
        self.current_input = "0"
        self.display.setText(self.current_input)

app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
