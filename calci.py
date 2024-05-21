from tkinter import *
root=Tk()
root.title("Sahil's Calculator")
e=Entry(root,width=35,fg="green", borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10,pady=10)
def button_click(number):
    #e.delete(0, END)
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    c=e.get()
    e.delete(0, END)   
def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0, END)
def button_equal():
    second_number= e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0, END)
def button_multi():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0, END)
def button_div():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0, END)




#define the BUTTONS
b1=Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), fg="red", bg="yellow")
b2=Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), fg="red", bg="yellow")
b3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), fg="red", bg="yellow")
b3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), fg="red", bg="yellow")
b3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), fg="red", bg="yellow")
b4=Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), fg="red", bg="yellow")
b5=Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), fg="red", bg="yellow")
b6=Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), fg="red", bg="yellow")
b7=Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), fg="red", bg="yellow")
b8=Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), fg="red", bg="yellow")
b9=Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), fg="red", bg="yellow")
b0=Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), fg="red", bg="yellow")
badd=Button(root, text="+", padx=39, pady=20, command=button_add,fg="red", bg="yellow")
bequal=Button(root, text="=", padx=91, pady=20, command=button_equal,fg="red", bg="yellow")
bclear=Button(root, text="CLEAR", padx=79, pady=20, command=button_clear,fg="red", bg="yellow")
bsub=Button(root, text="-", padx=41, pady=20, command=button_subtract,fg="red", bg="yellow")
bdivide=Button(root, text="/", padx=41, pady=20, command=button_div,fg="red", bg="yellow")
bmu=Button(root, text="*", padx=40, pady=20, command=button_multi,fg="red", bg="yellow")


#PUT BUTTONS ON THE SCREEN
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)

badd.grid(row=5, column=0)
bequal.grid(row=5, column=1, columnspan=2)
bclear.grid(row=4, column=1, columnspan=2)
bsub.grid(row=6, column=0)
bdivide.grid(row=6, column=1)
bmu.grid(row=6, column=2)
root.mainloop()