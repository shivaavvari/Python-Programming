import MySQLdb

def create_table():
  db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
  cursor =db.cursor()
  cursor.execute("create table students(id int primary key AUTO_INCREMENT,name varchar(100),address varchar(500),age int,number int);")
  print("Table created successfully")
  db.commit()
  db.close()

def insert_data():
    name=input("Enter name:")
    address=input("Enter address:")
    age=input("Enter age:")
    number = input("Enter number:")
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    cursor.execute("Insert into   students(name ,address ,age ,number) values(%s,%s,%s,%s)",(name,address,age,number))
    print("data added successfully")
    db.commit()
    db.close()

def update_data():
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    student_id =input("Please enter the student_id to be updated?")
    fields = {
        "1":("name","Please enter the new name?"),
        "2":("address","Please enter the new address"),
        "3":("age","Please enter the new age"),
        "4":("number","Please enter the new number"),

    }

    for keys in fields:
        print(f"{keys} : {fields[keys][0]}")
        
    
    selected_choice = input("Enter the selection to be updated")
    
    if selected_choice in fields:
      field_choice, prompt = fields[selected_choice][0],fields[selected_choice][1]
      new_choice = input(prompt)

      sql =f"update students set {field_choice}=%s where id =%s"
      cursor.execute(sql,(new_choice,student_id))
      print(f"{field_choice} updated successfully")
    else:
      print("invalid field choice ")  
       
    db.commit()
    db.close()

def delete_data():
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    
    student_id = input("Enter id of the student to be deleted:")
    cursor.execute("select *  from  students where id=%s ",(student_id,))
    
    student =cursor.fetchone()
    
    if student:
        print(f"Student to be deleted: ID {student[0]},Name: {student[1]}, Address= {student[2]}, Number ={student[3]} ")
        choice = input("Do you want to delete the student (yes/no)")
        if choice.lower()=="yes":
            cursor.execute("delete from students where id=%s",(student_id,))
            print("Data updated succesfully")
       
            

        else:
            print("Deletion cancelled") 
            
    else:         
        print("data not updated")
    
    db.commit()
    db.close()
    
    

def read_data():
    
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    cursor.execute("select * from students;")
    result = cursor.fetchall()
   

    for student in result:
        print(f" ID {student[0]},Name: {student[1]}, Address= {student[2]}, Number ={student[3]} ")
     
    print("data printed   successfully")
    db.commit()  
    db.close()    
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