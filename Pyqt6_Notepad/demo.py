from PyQt6.QtWidgets  import QInputDialog,QFileDialog,QMenu,QMenuBar,QMainWindow,QTextEdit, QFormLayout, QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QAction,QIcon,QTextCursor ,QColor 
from PyQt6.QtCore import Qt

import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("Form Layout")
        self.setGeometry(100,100,400,300)
     
        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)
        
        self.current_file = None
        # creating a menu bar
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)
        #create a Menu
        fileMenu = QMenu("File",self)
        menubar.addMenu(fileMenu)
        editmenu = QMenu("Edit",self)
        menubar.addMenu(editmenu)

        #creating an action 
        
        new_action = QAction("New",self)
        fileMenu.addAction(new_action)
        new_action.triggered.connect(self.new_file)
    
        open_action = QAction("Open",self)
        fileMenu.addAction(open_action)
        open_action.triggered.connect(self.open_file)
    
        save_action = QAction("Save",self)
        fileMenu.addAction(save_action)
        save_action.triggered.connect(self.save_file)
    
        save_as_action = QAction("Save as",self)
        fileMenu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_file_as)

        #creating an edit menu
        
        #creating an action
        undo_action = QAction("Undo ",self)
        editmenu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction("Redo ",self)
        editmenu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        cut_action = QAction("Cut ",self)
        editmenu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        copy_action = QAction("Copy ",self)
        editmenu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)
        
        paste_action = QAction("Paste ",self)
        editmenu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        find_action = QAction("Find ",self)
        editmenu.addAction(find_action)
        find_action.triggered.connect(self.find_text)

    
    
    
    def new_file(self):
        print("Creating New File ")
        self.edit_field.clear()
        self.current_file = None


    def open_file(self):
        print("opening New File ")
        filepath,_ = QFileDialog.getOpenFileName(self,"Open file","","All Files (*);; Python Files (*.py)")
        with open(filepath,"r") as f:
            data = f.read()
            self.edit_field.setText(data)


    def save_file_as(self):
        print("saving New File ")
        filepath,_ = QFileDialog.getSaveFileName(self,"Save file","","All Files (*);; Python Files (*.py)")
        print(filepath)
        if filepath:
            with open(filepath,'w') as f:
                f.write(self.edit_field.toPlainText())
            self.current_file = filepath

    def save_file(self):
        print("saving as New File ")
        if self.current_file:

            with open(self.current_file,'w') as f:
                f.write(self.edit_field.toPlainText())

        else:
            self.save_file_as()
    def find_text(self):
        print("Finding Text")  
        text,ok = QInputDialog.getText(self,"Find Text","Search for text:") 
        if ok:
            all_words = []
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
            highlight_color = Qt.GlobalColor.yellow

            while (self.edit_field.find(text)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)


                selection.cursor = self.edit_field.textCursor()
                all_words.append(selection)

            self.edit_field.setExtraSelections(all_words)

app = QApplication(sys.argv)
#app.setStyle('Fusion')

window = Window()

window.show()


sys.exit(app.exec())
