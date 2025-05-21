from PyQt6.QtWidgets  import  QStackedLayout,QTextEdit,QComboBox,QFormLayout, QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("Stacked Form Layout")
        self.setGeometry(100,100,400,300)

        
        combo_box = QComboBox()
        combo_box.addItems(["Label","Form"])
        combo_box.activated.connect(self.change_page)

        #creating page 1
        label = QLabel("this is the label page")

        #creating page 2
        form = QFormLayout()
        form.addRow("",QLabel("This is the form page"))
        page2_container = QWidget()
        page2_container.setLayout(form)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(label)
        self.stacked_layout.addWidget(page2_container)

        main_layout = QFormLayout()
        main_layout.addRow(combo_box)
        main_layout.addRow(self.stacked_layout)

        self.setLayout(main_layout)
    def change_page(self, index):
        self.stacked_layout.setCurrentIndex(index)




app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
