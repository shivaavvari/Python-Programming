from tkinter import *
from fpdf import FPDF
invoice_item = []


def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = int(quantity_entry.get())
    price = medicines[selected_medicine]
    total_amount = price * quantity
    invoice_item.append((selected_medicine, quantity, price, total_amount))
    update_invoice_text()

def calculate_total():
    total = 0.0
    for item  in invoice_item:
        total += item[3]
    return total

def update_invoice_text():
    invoice_text.delete(1.0, END) # line 1, column 0    
    for item in invoice_item:
        invoice_text.insert(END,f"Medicine{item[0]},Quanity{item[1]},Price{item[2]},Total {item[3]}\n")
    total_amount_entry.delete(0, END)
    total_amount_entry.insert(END,str(calculate_total()))

def generate_invoice():
    customer_name = customer_entry.get()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica",size=12)
    pdf.cell(0,10,text="Invoice",new_x='LMARGIN',new_y="NEXT", align='C')   

    pdf.cell(0, 10, text=f"Customer {customer_name}",new_x='LMARGIN',new_y="NEXT", align='L')
    pdf.cell(0,10,text="",new_x='LMARGIN',new_y="NEXT")
   
    for item in invoice_item:
        medicine_name ,quantity, price, total = item

        pdf.cell(0, 10, text=f"Medicine : {medicine_name} , Quantity : { quantity}, Amount : {total}",new_x='LMARGIN',new_y="NEXT",align='L')
    pdf.cell(0,10,text="Total Amount :"+str(calculate_total()),new_x='LMARGIN',new_y="NEXT",align='L')
    pdf.cell(0,10,text="",new_x='LMARGIN',new_y="NEXT")
    
    pdf.output("invoice.pdf")

window =Tk()
window.title("Invoice Generator")

medicines= {
    "Medicine A": 10.0,
    "Medicine B": 20.0,
    "Medicine C": 30.0,
    "Medicine D": 40.0,    
}

medicine_label = Label(window, text="Medicine Name  ")
medicine_label.pack()
medicine_listbox = Listbox(window,selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.pack()



quantity_label=Label(window,text="Quantity")
quantity_entry= Entry(window)
quantity_label.pack()   
quantity_entry.pack()

add_button = Button(window, text="Add Medicine: ", command=add_medicine)
add_button.pack()

total_amount_label = Label(window,text="Total amount")
total_amount_label.pack()   


total_amount_entry = Entry(window)  
total_amount_entry.pack()


customer_label = Label(window, text="Customer Name")
customer_label.pack()   
customer_entry = Entry(window)
customer_entry.pack()   

generate_button = Button(window, text="Generate Invoice",command=generate_invoice)   
generate_button.pack()

invoice_text = Text(window, height=10, width=50)
invoice_text.pack() 


window.mainloop()



