import pyodbc

def create_table():
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    cursor.execute("create table students(id int identity(1,1) primary key,name varchar(100),address varchar(500),age int,number int);")
    print("Table created  successfully")
    cursor.commit()  
    conn.close()    

def insert_data():
    name=   input("Enter name:")
    address=input("Enter address:")
    age=    input("Enter age:")
    number= input("Enter number:")

    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    cursor.execute("Insert into   students(name ,address ,age ,number) values(?,?,?,?)",(name,address,age,number))
    print("data added   successfully")
    cursor.commit()  
    conn.close()    

def read_data():
    
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    cursor.execute("select * from students;")
    result = cursor.fetchall()
   

    for student in result:
        print(f" ID {student[0]},Name: {student[1]}, Address= {student[2]}, Number ={student[3]} ")
     
    print("data printed   successfully")
    cursor.commit()  
    conn.close()    


def update_data():
    
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    
    student_id = input("Enter id of the student to be updated:")
    fields = {

        "1":['name','Please enter the new name'],
        "2":['address','Please enter the new address'],
        "3":['age','Please enter the new age'],
        "4":['number','Please enter the new number'],
    }
    
    print("Enter the field you want to update")
    for key in fields:
        print(f" {key}:{fields[key][0]}")

    field_choice = input("Enter the field you want to update:")
    if field_choice in fields:
        field_name,prompt = fields[field_choice]
        new_value = input(prompt)
        sql = f"update students set {field_name}=? where id=? "
        cursor.execute(sql,(new_value,student_id))
        print(f"{field_name} update successfully")
    else:
        print("Invalid field choice")    
    cursor.commit()  
    conn.close()    

def delete_data():
   
    
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    student_id = input("Enter id of the student to be deleted:")
    cursor.execute("select *  from  students where id=? ",(student_id,))
    
    student =cursor.fetchone()
    
    if student:
        print(f"Student to be deleted: ID {student[0]},Name: {student[1]}, Address= {student[2]}, Number ={student[3]} ")
        choice = input("Do you want to delete the student (yes/no)")
        if choice.lower()=="yes":
            cursor.execute("delete from students where id=?",(student_id,))
            print("Data updated succesfully")
            cursor.commit()  
            conn.close()    

        else:
            print("Deletion cancelled")
            conn.close()    
   
    else:         
        print("data not updated")
        conn.close()
    
   
while True:
    print("welcome to the Student database management system")
    print("1. Create a Table") 
    print("2. Insert the data")
    print("3. Read the data")
    print("4. Update the data")   
    print("5. Delete the data")
    print("6. Exit the system")

    choice = input("Enter your choice (1-6)")
    if choice =="1":
        create_table()
    elif choice =="2":
        insert_data()
    elif choice =="3":
        read_data()
    elif choice =="4":
        update_data()
    elif choice =="5":
        delete_data()
    elif choice =="6":
        break
    else:
        print("Enter a valid choice")    