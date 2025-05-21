from tkinter import * 
import bcrypt



def validate(password):
    hash = b'$2b$12$XvLQGsorO07xxiOk54dpbeApVZ9Om/uJTu/qXwgcNhu8uamESalIi'
    password =bytes(password,encoding='utf-8')

    if bcrypt.checkpw(password,hash):
        print("Login successful")
    else:
        print("invalid password")
root = Tk()
root.geometry("300x300")



password_entry = Entry(root)
password_entry.pack()

button = Button(root,text="Validate",command=lambda: validate(password_entry.get()))
button.pack()
root.mainloop()