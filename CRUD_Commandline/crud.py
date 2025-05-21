import json 
import os 

def create_user():
    while True:
        
        if  os.path.exists("data.json"):
            add_user = input("Do you want to add a user? (yes/no): ")
            if add_user.lower() == "yes":
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                city = input("Enter your city: ")
                data = {"name": name,   
                        "age": age,
                        "city": city}
                
                with open("data.json", 'r') as file:
                        present_data = json.load(file)
                present_data.append(data)
                with open("data.json", "w") as file:
                    json.dump(present_data, file)

                print("User created successfully")
                print("The updated data is: ")  
                print(present_data)
            else:
                print("User not created")
                with open("data.json", 'r') as file:
                        present_data = json.load(file)
                print(present_data)
                break
        else:
            print("File does not exist")    
def update_user():
    while True:
        if os.path.exists("data.json"):
            with open("data.json", 'r') as file:
                present_data = json.load(file)
            print("The present data is: ")
            print(present_data)
            update_user = input("Do you want to update a user? (yes/no): ")
            if update_user.lower() == "yes":
                name = input("Enter the name of the user you want to update: ")
                for i in present_data:
                    if i["name"] == name:
                        i["age"] = int(input("Enter the new age: "))
                        i["city"] = input("Enter the new city: ")
                        with open("data.json", "w") as file:
                            json.dump(present_data, file)
                        print("User updated successfully")
                        print("The updated data is: ")  
                        print(present_data)
                        break
               
            else:
                print("User not found")
                break
        else:
            print("File does not exist")
            break

def delete_user():
    while True:
        if os.path.exists("data.json"):
            with open("data.json", 'r') as file:
                present_data = json.load(file)
            print("The present data is: ")
            print(present_data)
            delete_user = input("Do you want to delete a user? (yes/no): ")
            if delete_user.lower() == "yes":
                name = input("Enter the name of the user you want to delete: ")
                for i in present_data:
                    if i["name"] == name:
                        present_data.remove(i)
                        with open("data.json", "w") as file:
                            json.dump(present_data, file)
                        print("User deleted successfully")
                        print("The updated data is: ")  
                        print(present_data)
                        break
            else:
                print("User not found")
                break
        else:
            print("File does not exist")
            break

def read_user():
    while True:
        if os.path.exists("data.json"):
            with open("data.json", 'r') as file:
                present_data = json.load(file)  
            print("The present data is: ")
            print(present_data) 
            break
        else:    
            print("File does not exist")
            break

def user_management():
    try:
        while True:
            print("1. Create user")
            print("2. Update user")
            print("3. Delete user")
            print("4. Read user")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_user()
            elif choice == 2:
                update_user()
            elif choice == 3:
                delete_user()
            elif choice == 4:
                read_user()
            elif choice == 5:
                break
            else:
                print("Invalid choice") 
    except ValueError:
        print("Invalid input")

user_management()



