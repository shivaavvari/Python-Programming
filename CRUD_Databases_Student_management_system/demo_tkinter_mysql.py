from  tkinter  import *
import MySQLdb
from tkinter import ttk # for label frame , treeframe, Tree
from tkinter import messagebox


def run_query(query,parameters=()):
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    cursor.execute(query,parameters)
   
    query_result = []
    try:
        if query.lower().startswith("select"):
            query_result =cursor.fetchall()
            return query_result
            db.commit()        
        else:
            db.commit()    
    except Exception as e:
        messagebox.showerror("Database error",str(e))
    finally:
        cursor.close()
        db.close()


def refresh_treeview():
    
    for item in tree.get_children():
        tree.delete(item)
    records = run_query("select * from students;",)

    for record in records:
        tree.insert("",END,values=record)

def insert_data():
    query ="insert into students(name,address,age,number) values(%s,%s,%s,%s);"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),phone_entry.get())
    run_query(query,parameters)
    messagebox.showinfo("information","the students info is updated")
    refresh_treeview()

def delete_data():
    selected_item = tree.selection()[0]
    id=tree.item(selected_item)['values'][0]
    query ="Delete  from students  where id=%s"
    parameters = (id,)
    run_query(query,parameters)
    messagebox.showinfo("information","the students info is deleted")
    refresh_treeview()

def update_data():
    selected_item = tree.selection()[0]
    id=tree.item(selected_item)['values'][0]
    query ="update students set name=%s, address=%s, age=%s,number=%s where id=%s"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),phone_entry.get(),id)
    
    run_query(query,parameters)
    messagebox.showinfo("information","the students info is Updated")
    refresh_treeview()


def create_table():

    query ="create table if not exists students(id int primary key auto_increment, name varchar(30), address varchar(50),age int, number int);"
    parameters = ()
    run_query(query,parameters)
    messagebox.showinfo("information","the students table exists")
    refresh_treeview()


root = Tk()
root.title("Student Management System")

label_frame = LabelFrame(root,text="Students")
label_frame.grid(row=0, column=0,padx=10,pady=10)
Label(label_frame,text="Name :").grid(row=0,column=0,padx=5,pady=5)

name_entry = Entry(label_frame)
name_entry.grid(row=0,column=1,pady=10)
Label(label_frame,text="address :").grid(row=1,column=0,padx=5,pady=5)

address_entry = Entry(label_frame)
address_entry.grid(row=1,column=1,pady=10)
Label(label_frame,text="Age :").grid(row=2,column=0,padx=5,pady=5)


age_entry = Entry(label_frame)
age_entry.grid(row=2,column=1,pady=10)
Label(label_frame,text="Phone number :").grid(row=3,column=0,padx=5,pady=5)


phone_entry = Entry(label_frame)
phone_entry.grid(row=3,column=1,pady=10)

function_frame= Frame(root)
function_frame.grid(row=1,column=0,pady=5,padx=5)
Button(function_frame,text="Create Table",command=create_table).grid(row=0,column=0,pady=10,padx=5)
Button(function_frame,text="Insert Table",command=insert_data).grid(row=0,column=1,pady=10,padx=5)
Button(function_frame,text="Update Table",command=update_data).grid(row=0,column=2,pady=10,padx=5)
Button(function_frame,text="Delete Table",command=delete_data).grid(row=0,column=3,pady=10,padx=5)

tree_frame =Frame(root)
tree_frame.grid(row=2,column=0,pady=5,padx=5)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)
tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set, selectmode="browse")

tree.pack()
tree_scroll.config(command=tree.yview)

tree['columns'] = ('id','name','address','age','number')
tree.column("#0",width=0,stretch=NO)
tree.column("id",anchor=CENTER,width=80)
tree.column("name",anchor=CENTER,width=120)
tree.column("address",anchor=CENTER,width=80)
tree.column("age",anchor=CENTER,width=80)
tree.column("number",anchor=CENTER,width=120)

tree.heading("id",text="ID",anchor=CENTER)
tree.heading("name",text="Name",anchor=CENTER)
tree.heading("address",text="Address",anchor=CENTER)
tree.heading("age",text="age",anchor=CENTER)
tree.heading("number",text="Phone number",anchor=CENTER)


refresh_treeview()


root.mainloop()



