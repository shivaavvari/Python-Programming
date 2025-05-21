from PyQt6.QtWidgets  import  QTextEdit,QComboBox,QFormLayout, QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("Form Layout")
        self.setGeometry(100,100,400,300)
       
        form_layout = QFormLayout()
        self.setLayout(form_layout)
        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.subject_combo = QComboBox()
        self.subject_combo.addItems(["Select Subject","Personal","Business"])
        #multilpe line text edit 
        self.message_edit = QTextEdit()

       
       
        submit_button = QPushButton("Submit")
        form_layout.addRow(QLabel("Name: "), self.name_edit)
        form_layout.addRow(QLabel("Email: "), self.email_edit)
        form_layout.addRow(QLabel("Phone number: "), self.phone_edit)
        form_layout.addRow(QLabel("Subject: "), self.subject_combo)
        form_layout.addRow(QLabel("Message: "), self.message_edit)
        form_layout.addRow(submit_button)

        submit_button.clicked.connect(self.submit_click)
    def submit_click(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()
        subject= self.subject_combo.currentText()
        message = self.message_edit.toPlainText()

        print(f"Name: {name} \n email: {email} \n phone: {phone} \n subject: {subject} \n message:  {message}") 
        
app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
