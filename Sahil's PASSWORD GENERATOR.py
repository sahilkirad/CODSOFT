from tkinter import *
import customtkinter
root = Tk()
root.geometry()
r=Label(root, text="Sahil's Password Generator")
r.grid(row=0, column=10)
customtkinter.set_appearance_mode("red")
s = customtkinter.CTkLabel(root, text="Sahil's Password Generator")
s.grid(row=1, column=90)
lt = customtkinter.CTkEntry(root, height=80,width=500, placeholder_text="Enter the number of letters", placeholder_text_color="orange", 
                            font=("Calibri", 16), corner_radius=40, text_color="orange", )
lt.grid(row=2, column=5)

sy = customtkinter.CTkEntry(root, height=80,width=500, placeholder_text="Enter the number of symbols", placeholder_text_color="orange", 
                            font=("Calibri", 16), corner_radius=40, text_color="orange")
sy.grid(row=3, column=5)
nu = customtkinter.CTkEntry(root, height=80,width=500, placeholder_text="Enter the number of numericals", placeholder_text_color="orange", 
                            font=("Calibri", 16), corner_radius=40, text_color="orange")
nu.grid(row=4, column=5)
import random


def password():
    password = " "
    le = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    l1 = lt.get()
    l11 = int(l1)
    
    sy1 = sy.get()
    sy11 = int(sy1)
    nu1 = nu.get()
    nu11 = int(nu1)
    for i in range(l11):
        password += random.choice(le)
    for i in range(sy11):
        password += random.choice(sym)
    for i in range(nu11):
        password += random.choice(n)

    label.configure(text=password, text_color="red")
    return

def clear():
    lt.delete(0, END)
    sy.delete(0, END)
    nu.delete(0, END)


s1 = customtkinter.CTkButton(root, text="Get Generated Password", command=password, font=("Calibri", 16))
s1.grid(row=2, column=30)
s2 = customtkinter.CTkButton(root, text="CLEAR", command=clear, font=("Calibri", 16))
s2.grid(row=4, column=30)
label = customtkinter.CTkLabel(root, text="")
label.grid(row=6, column=30)
root.mainloop()
