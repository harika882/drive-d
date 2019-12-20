# import tkinter as tk
# from tkinter import ttk
# import time
# win=tk.Tk()
# # win.geometry("500x800+0+0")
# win.title("Menu Bar")
# def func():
#     print("func calling")
# def exit():
#     win.destroy()
#
#
# menu_bar=tk.Menu(win)
# win.config(menu=menu_bar)
# file_menu=tk.Menu(menu_bar,tearoff=0)
# file_menu.add_command(label="new",command=func)
# file_menu.add_command(label="open",command=func)
# file_menu.add_command(label="save",command=func)
# file_menu.add_command(label="save as",command=func)
# file_menu.add_separator()
# file_menu.add_command(label="paze setup",command=func)
# file_menu.add_command(label="print",command=func)
# file_menu.add_command(label="exit",command=exit)
# menu_bar.add_cascade(label="file",menu=file_menu)
# def tdate():
#     print(time.asctime(time.localtime(time.time())))
# edit_menu=tk.Menu(menu_bar,tearoff=0)
# edit_menu.add_command(label="Undo    ctrl+z",command=func)
# edit_menu.add_command(label="cut     ctrl+x",command=func)
# edit_menu.add_command(label="copy    ctrl+c",command=func)
# edit_menu.add_command(label="paste   ctrl+v",command=func)
# edit_menu.add_command(label="delete  del",command=func)
# edit_menu.add_separator()
# edit_menu.add_command(label="find    ctrl+f",command=func)
# edit_menu.add_command(label="find next   f3",command=exit)
# edit_menu.add_command(label="replace ctrl+r",command=exit)
# edit_menu.add_command(label="goto    ctrl+g",command=exit)
# edit_menu.add_separator()
# edit_menu.add_command(label="select all ctrl+A",command=exit)
# edit_menu.add_command(label="time/date    F5 ",command=tdate())
# menu_bar.add_cascade(label="edit",menu=edit_menu)
#
# format_menu=tk.Menu(menu_bar,tearoff=0)
# format_menu.add_command(label="wordwrap")
# format_menu.add_command(label="font")
# menu_bar.add_cascade(label="format",menu=format_menu)
#
#
# view_menu=tk.Menu(menu_bar,tearoff=0)
# view_menu.add_command(label="status bar")
# menu_bar.add_cascade(label="view",menu=view_menu)
#
# help_menu=tk.Menu(menu_bar,tearoff=0)
# help_menu.add_command(label="help center")
# help_menu.add_command(label="about notepad")
# menu_bar.add_cascade(label="help",menu=help_menu)
#
#
# win.mainloop()

#
# '''a small program about dictionary'''
# from tkinter import*
# top=Tk()
# top.title("dictionary")
# top.config(bg="green")
# def click():
#     enteredtext=entry_var.get()
#     text.delete(0.0,END)
#     try:
#         definition=dictionary[enteredtext]
#     except:
#         definition="sorry,we cant found"
#     text.insert(END,definition)
#
#
# lb=Label(top,text="Enter the word which you want meaning",font=("arial",10,"bold"),bg="green",fg="white",anchor="w")
# lb.grid(row=0,column=0)
# entry_var=StringVar()
# entry=Entry(top,width=16,relief="groove",textvariable=entry_var)
# entry.grid(row=1,column=0)
# men=Label(top,text="The Meaning of the word is:",font=("arial",10,"bold"),bg="green",fg="white",anchor="w")
# men.grid(row=3,column=0)
# text=Text(top,width=40,height=5)
# text.grid(row=4,column=0)
# dictionary={"python":"Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. ",
#             "tkinter":"Tkinter is the Python interface to the Tk GUI toolkit shipped with Python. We would look this option in this chapter."}
#
# submit=Button(top,text="submit",command=click).grid(row=2,column=0)
#
# top.mainloop()


''''message box creating'''
from tkinter import*
from tkinter import messagebox

win=Tk()
label1=Label(win,text="Enter your name:")
label2=Label(win,text="Enter your age :")
name_var=StringVar()
entry1=Entry(win,width=16,textvariable=name_var,relief="solid")
age_var=StringVar()
entry2=Entry(win,width=16,textvariable=age_var,relief="solid")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
entry1.grid(row=1,column=0,padx=2,pady=2)
entry2.grid(row=1,column=1)
def submit():
    name=name_var.get()
    age=age_var.get()
    if name=="" and age=="":
        messagebox.showerror("Error",f"you must enter both name and age")
    else :
        try:
            age=int(age)
        except ValueError:
            messagebox.showwarning("title","you must enter digits only")
        else:
            print(f"name :{name}, age:{age}")
            if age<18:
                messagebox.showinfo("message","you r not eligible")
button=Button(win,text="submit",command=submit,relief="groove")
button.grid(row=2,columnspan=2)
win.mainloop()
