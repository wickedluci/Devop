# Project: Calculator (1st Iteration)

# Creating A Calculator
from tkinter import *
def button_click(number):
    # e.delete(0,END)
    e.insert(END,number)
def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num + int(second_number))
    if math == "subtraction":
        e.insert(0,f_num - int(second_number))
    if math == "multiplication":
        e.insert(0,f_num * int(second_number))
    if math == "division":
        e.insert(0,f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    return

root = Tk()
root.title("Calculator")
root.configure(bg="black")

e = Entry(root, width=35,borderwidth=5,fg="Cyan",bg="Black")
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

button_1 = Button(root,text="1",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=20,pady=10,fg="Cyan",bg="Black",command=lambda: button_click(0))

button_add = Button(root,text="+",padx=20,pady=10,fg="Cyan",bg="Black",command=button_add)
button_equal = Button(root,text="=",padx=20,pady=10,fg="Cyan",bg="Black",command=button_equal)
button_clear = Button(root,text="Clear",padx=20,pady=10,fg="Cyan",bg="Black",command=button_clear)
button_subtract = Button(root,text="-",padx=20,pady=10,fg="Cyan",bg="Black",command=button_subtract)
button_multiply = Button(root,text="*",padx=20,pady=10,fg="Cyan",bg="Black",command=button_multiply)
button_divide = Button(root,text="/",padx=20,pady=10,fg="Cyan",bg="Black",command=button_divide)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

button_clear.grid(row=4,column=1)
button_add.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=2,column=3)
button_divide.grid(row=1,column=3)

root.mainloop()

