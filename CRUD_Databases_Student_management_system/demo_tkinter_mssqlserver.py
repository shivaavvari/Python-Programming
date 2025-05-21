from tkinter import * 
from tkinter import ttk
import pyodbc
from tkinter import messagebox



def run_query(query,parameters=()):
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    query_result = None
    try:
        cursor.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result = cursor.fetchall()
            return query_result
        conn.commit()
    except Exception as e:
        messagebox.showerror("Database Error",str(e))
    finally:
        cursor.close()
        conn.close()    
def refresh_treeview():
    for item in tree.get_children():
        tree.delete(item)
    records = run_query("select * from students",)
    for record in records:
        
        tree.insert('',END,values=list(record))

def insert_data():
    query =   "Insert into   students(name ,address ,age ,number) values(?,?,?,?)"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),phone_entry.get())
    run_query(query,parameters)
    messagebox.showinfo("Information","Data inserted successfuly")
    refresh_treeview()


def delete_data():
    selected_item = tree.selection()[0]
    id = tree.item(selected_item)['values'][0]
    query="delete from students where id =?"
    parameters=(id,)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data deleted successfuly")
    refresh_treeview()

def update_data():
    selected_item = tree.selection()[0]
    id = tree.item(selected_item)['values'][0]
    query = "update students set name=?, address=?, age=?, number=? where id =?"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),phone_entry.get(),id)
    run_query(query,parameters)
     
    messagebox.showinfo("Information","Data updated successfuly")
    refresh_treeview()
def create_table():
    query = "if not exists (select * from sysobjects where name='students' and xtype='U') create table students(id int identity(1,1) primary key,name varchar(100),address varchar(500),age int,number int);"
    run_query(query)
    messagebox.showinfo("information","Table created  successfully")
    refresh_treeview()
root = Tk()
root.title("Student Management system")

frame=LabelFrame(root,text="Student Data")
frame.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

Label(frame,text="Name: ").grid(row=0,column=0,padx=2,sticky="ew")
name_entry = Entry(frame)
name_entry.grid(row=0, column =1 , pady=2,stick="ew")
Label(frame,text="Address: ").grid(row=1,column=0,padx=2,sticky="ew")
address_entry = Entry(frame)
address_entry.grid(row=1, column =1 , pady=2,stick="ew")
Label(frame,text="Age: ").grid(row=2,column=0,padx=2,sticky="ew")
age_entry = Entry(frame)
age_entry.grid(row=2, column =1 , pady=2,stick="ew")
Label(frame,text="Phone number: ").grid(row=3,column=0,padx=2,sticky="ew")
phone_entry = Entry(frame)
phone_entry.grid(row=3, column =1 , pady=2,stick="ew")

button_frame =Frame(root)
button_frame.grid(row=1,column=0,pady=5,sticky="ew")

Button(button_frame, text="Create Table",command=create_table).grid(row=0,column=0,padx=5)
Button(button_frame, text="Add data ",command=insert_data).grid(row=0,column=1,padx=5)

Button(button_frame, text="Update data",command=update_data).grid(row=0,column=2,padx=5)
Button(button_frame, text="Delete data",command=delete_data).grid(row=0,column=3,padx=5)

tree_frame = Frame(root)
tree_frame.grid(row=2,column=0,padx=10,sticky="nsew")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
tree.pack()
tree_scroll.config(command = tree.yview)

tree['columns'] =("id","name","address", "age","number")
tree.column("#0",width=0,stretch=NO)
tree.column("id",anchor=CENTER,width=80)
tree.column("name",anchor=CENTER,width=120)
tree.column("address",anchor=CENTER,width=120)
tree.column("age",anchor=CENTER,width=80)
tree.column("number",anchor=CENTER,width=120)


tree.heading("id",text="ID",anchor=CENTER)
tree.heading("name",text="Name",anchor=CENTER)
tree.heading("address",text="Address",anchor=CENTER)
tree.heading("age",text="Age",anchor=CENTER)
tree.heading("number",text="Phone number",anchor=CENTER)


refresh_treeview()
root.mainloop()
