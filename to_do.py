import tkinter as tk
import customtkinter
from tkinter import messagebox

root=customtkinter.CTk()
root.resizable(False,False)
root.geometry('500x500')
list_box=tk.Listbox(root, height=50, width=100, bg="black", borderwidth=10, foreground="white")
list_box.place(x=150,y=200)

def add_task():
    if (len(entry.get())==0):
        messagebox.showerror("Error","Error,please add a task")
    else:
        list_box.insert(0, entry.get())
        entry.delete(0,"end")

def remove_task():
    y=list_box.curselection()
    if y:
        list_box.delete(y[0])
    else:
        messagebox.showerror("Error","Error,you have not selected task to remove")

def remove_all():
    list_box.delete(0, "end")
    
entry=customtkinter.CTkEntry(root, placeholder_text="What do you want to do?", width=250)
entry.place(relx=0.2,rely=0.1)
b1=customtkinter.CTkButton(root, text="Add task", command=add_task, height=50, width=100, text_color="blue", fg_color="green", 
                           hover_color="yellow")
b1.place(relx=0.05,rely=0.2)
b2=customtkinter.CTkButton(root, text="Remove task", command=remove_task, height=50, width=100, text_color="blue", fg_color="green", 
                           hover_color="yellow")
b2.place(relx=0.35,rely=0.2)
b3=customtkinter.CTkButton(root, text="Clear all", command=remove_all, height=50, width=100, text_color="blue", fg_color="green", 
                           hover_color="yellow")
b3.place(relx=0.65,rely=0.2)
root.mainloop()