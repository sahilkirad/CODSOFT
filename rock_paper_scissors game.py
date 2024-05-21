from tkinter import *
import customtkinter
import random
root=customtkinter.CTk()
customtkinter.set_appearance_mode("green")
root.geometry('500x500')

def out(user):
    option=["rock","scissors","paper"]
    comp_choice=random.choice(option)
    if user==comp_choice:
        label.configure(text="Draw")
    elif user=="rock" and comp_choice=="scissors":
        label.configure(text="user wins")
    elif user=="scissors" and comp_choice=="paper":
        label.configure(text="user wins")
    elif user=="paper" and comp_choice=="rock":
        label.configure(text="user wins")
    else:
        label.configure("computer wins")
        label2.configure(text="{} vs {}".format(user,comp_choice))

b1=customtkinter.CTkButton(root, text="Rock",command=lambda:out("rock"), height=100, width=200, font=("Calibri",15), text_color="yellow", hover_color="green"
 ,corner_radius=40, border_width=10)
b1.place(relx=0.10, rely=0.2)
b2=customtkinter.CTkButton(root, text="Scissors",command=lambda:out("scissors"), height=100, width=200, font=("Calibri",15), text_color="yellow",hover_color="green"
 ,corner_radius=40, border_width=10)
b2.place(relx=0.10, rely=0.5)
b3=customtkinter.CTkButton(root, text="Paper",command=lambda:out("paper"), height=100, width=200, font=("Calibri",15), text_color="yellow", hover_color="green"
 ,corner_radius=40, border_width=10)
b3.place(relx=0.10, rely=0.8)
label=customtkinter.CTkLabel(root, text="", font=("arial", 24))
label.pack(padx=40)
label2=customtkinter.CTkLabel(root, text="", font=("arial", 24))
label2.pack(padx=40)
label3=customtkinter.CTkLabel(root, text="", font=("arial", 24))
label3.pack(padx=40)
root.mainloop()
