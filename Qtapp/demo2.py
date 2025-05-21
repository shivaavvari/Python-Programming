from PyQt6.QtWidgets import QMainWindow, QApplication
#pyuic6 demo.ui -o form.py
from todolist import Ui_Form
import sys
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,400,300)

        self.ui.addButton.clicked.connect(self.add_task)
        self.ui.deleteButton.clicked.connect(self.delete_task)
    def add_task(self):
        task = self.ui.taskEdit.text()
        self.ui.tasklist.addItem(task)
        self.ui.taskEdit.clear()
        
    def delete_task(self):
        selected_task = self.ui.tasklist.currentItem()
        if selected_task:
            self.ui.tasklist.takeItem(self.ui.tasklist.row(selected_task))


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()