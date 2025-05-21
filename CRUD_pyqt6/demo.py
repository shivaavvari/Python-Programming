from PyQt6.QtWidgets  import  QVBoxLayout,QMenu,QMessageBox,QToolBar,QPushButton,QSpinBox,QLineEdit,QFormLayout,QMainWindow, QDockWidget,QWidget, QApplication,QLabel,QTableWidget,QTableWidgetItem, QListWidget,QHBoxLayout, QListWidgetItem
from PyQt6.QtGui import QPixmap ,QAction,QIcon 
from PyQt6.QtCore import Qt ,QSize 
import sys
import warnings
import sqlite3
warnings.filterwarnings("ignore", category=DeprecationWarning)
#CRUD, create, read , update , delete
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("products.db")
        self.create_table()
        self.initUI()

    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM  products')
        products = cursor.fetchall()
        self.table_widget.setRowCount(len(products))
        for row, product in enumerate(products):
            for column, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, column,item) 
       
        
        
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS products ( \
                        id INTEGER PRIMARY KEY AUTOINCREMENT,\
                        name TEXT,\
                        price INTEGER,\
                        description TEXT) \
                       """)
        self.conn.commit()        
        
    def initUI(self):
        self.setGeometry(0,0,700,500)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.table_widget = QTableWidget(self)

        layout.addWidget(self.table_widget)

        
        self.table_widget.setColumnCount(4)

        self.table_widget.setHorizontalHeaderLabels(["ID","NAME","PRICE","DESCRIPTION"])


        #
        self.load_data()

        self.name_edit = QLineEdit(self)
        self.price_edit = QLineEdit(self)
        self.description_edit = QLineEdit(self)

        layout.addWidget(QLabel("Name :"))
        layout.addWidget(self.name_edit)

        layout.addWidget(QLabel("Price :"))
        layout.addWidget(self.price_edit)
        
        layout.addWidget(QLabel("Description :"))
        layout.addWidget(self.description_edit)

        
        add_button = QPushButton("Add Product",self)
        layout.addWidget(add_button)
        add_button.clicked.connect(self.add_product)

        delete_button = QPushButton("Delete Product",self)
        layout.addWidget(delete_button)
        delete_button.clicked.connect(self.delete_product)

        update_button = QPushButton("Update Product",self)
        layout.addWidget(update_button)
        update_button.clicked.connect(self.update_product)



    def add_product(self):
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        #new_product = {
        #   'name':name,'price':price,'description':description
        #
        #self.products.append(new_product)
        ##creating the table
        #row_position = len(self.products)-1 
        #self.table_widget.insertRow(row_position)
        #for col,value in enumerate(new_product.values()):
        #    item = QTableWidgetItem(str(value))
        #    self.table_widget.setItem(row_position,col,item)
        # Adding new product to the database 
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO products(name , price , description) VALUES(?,?,?)',(name,price,description))
        self.conn.commit()     
        self.load_data()

        self.name_edit.clear()
        self.price_edit.clear()
        self.description_edit.clear()



    def delete_product(self):
        current_row = self.table_widget.currentRow()
        if current_row<0 or current_row>= self.table_widget.rowCount():
            return QMessageBox.warning("Warning","No row Selected")
        product_id = self.table_widget.item(current_row,0).text()   
        response = QMessageBox.question(self,"Delete Product","Do you want to delete the product",QMessageBox.StandardButton.Yes |QMessageBox.StandardButton.No)
        if response == QMessageBox.StandardButton.Yes:
            #self.table_widget.removeRow(current_row)
            #del self.products[current_row]
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM products where id = ?',(product_id))
            self.conn.commit()     
            self.load_data()


    def update_product(self):
        current_row = self.table_widget.currentRow()
        if current_row<0 or current_row>= self.table_widget.rowCount():
            return QMessageBox.warning("Warning","No row Selected")
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        product_id = self.table_widget.item(current_row,0).text()   
        cursor = self.conn.cursor()
        cursor.execute('UPDATE products  SET name=?, price=?, description=? WHERE id=?',(name,price,description,product_id))
        self.conn.commit()     
        self.load_data()

      # updated_product = {
      #     'name':name,'price':price,'description':description
      # }
      # self.products[current_row] = updated_product
      # for col,value in enumerate(updated_product.values()):
      #     item = QTableWidgetItem(str(value))
      #     self.table_widget.setItem(current_row,col,item)




    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
