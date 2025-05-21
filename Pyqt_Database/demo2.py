from PyQt6.QtWidgets  import  QMenu,QMessageBox,QToolBar,QPushButton,QSpinBox,QLineEdit,QFormLayout,QMainWindow, QDockWidget,QWidget, QApplication,QLabel,QTableWidget,QTableWidgetItem, QListWidget,QHBoxLayout, QListWidgetItem
from PyQt6.QtGui import QPixmap ,QAction,QIcon 
from PyQt6.QtCore import Qt ,QSize 
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,700,500)
        people =[
            {"First Name":"John","Last Name":"Doe","Age":21},
            {"First Name":"Rob","Last Name":"Ford","Age":31},
            {"First Name":"Bob","Last Name":"Tyson","Age":41},
    
            
        ]
        self.table_widget =  QTableWidget()
        self.table_widget.setRowCount(len(people))
        self.table_widget.setColumnCount(3)
        
        self.table_widget.setHorizontalHeaderLabels(people[0].keys())
        row = 0 
        for person in people:
            self.table_widget.setItem(row, 0 , QTableWidgetItem(person['First Name']))
            self.table_widget.setItem(row, 1 , QTableWidgetItem(person['Last Name']))
            self.table_widget.setItem(row, 2 , QTableWidgetItem(str(person['Age'])))


            row +=1

        dock = QDockWidget()
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea,dock)

        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.age = QSpinBox(form,minimum=18,maximum=60)

        layout.addRow("First Name",self.first_name)
        layout.addRow("First Name",self.last_name)
        layout.addRow("First Name",self.age)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_people)
        layout.addRow(add_button)
        


        dock.setWidget(form)

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        self.delete_action = QAction(QIcon("D:\inligntech\icons\delete.png"),"Delete ",self)
        self.delete_action.triggered.connect(self.delete)
        toolbar.addAction(self.delete_action)
        
        self.add_row_above = QAction("Add row above ",self)
        self.add_row_above.triggered.connect(self.addRowAbove)
        
        self.add_row_below = QAction("Add row below ",self)
        self.add_row_below.triggered.connect(self.addRowBelow)
        
        self.copy_action = QAction("Copy  ",self)
        self.copy_action.triggered.connect(self.copy)
        
        self.paste_action = QAction("Paste ",self)
        self.paste_action.triggered.connect(self.paste)
        
        
        
        
        self.setCentralWidget(self.table_widget)
    
    
    def delete(self):
        current_row = self.table_widget.currentRow()
        if current_row <0 :
            QMessageBox.warning(self,"No row Selected")
        
        button = QMessageBox.question(self,"Delete Row","Are you Sure, you want to Delete Row?",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if button  == QMessageBox.StandardButton.Yes:
            self.table_widget.removeRow(current_row)

        

    def add_people(self):
        row = self.table_widget.rowCount()
        self.table_widget.insertRow(row)
        self.table_widget.setItem(row,0,QTableWidgetItem(self.first_name.text().strip()))
        self.table_widget.setItem(row,1,QTableWidgetItem(self.last_name.text().strip()))
        self.table_widget.setItem(row,2,QTableWidgetItem(self.age.text().strip()))

    def contextMenuEvent(self, event):
        context_menu = QMenu()
        context_menu.addAction(self.delete_action)
       
        context_menu.addAction(self.add_row_below)
        context_menu.addAction(self.add_row_above)
        context_menu.addAction(self.copy_action)
        context_menu.addAction(self.paste_action)
        
        
        context_menu.exec(event.globalPos())


    def addRowAbove(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row)

        
        
    def addRowBelow(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row+1)

    def copy(self):
        text     = self.table_widget.currentItem().text()
        self.item_text = text

    def paste(self):
        if self.item_text != None:
            row = self.table_widget.currentRow()
            column = self.table_widget.currentColumn()
            self.table_widget.setItem(row,column,QTableWidgetItem(self.item_text))            
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
