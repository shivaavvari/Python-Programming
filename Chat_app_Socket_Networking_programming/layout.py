from tkinter import *
import socket

root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root,text="Send",command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root,text="Receive",command=lambda :receive(listbox))
rbutton.pack(side=BOTTOM)
root.mainloop()

