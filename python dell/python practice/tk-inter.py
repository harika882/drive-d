# # """tkinter is a library. it is used for creating gui applications."""
# # '''here we must remember three lines code is happend as follows first three lines'''
# # import csv
# # from csv import DictWriter
# # import os
# # import shutil
# # import tkinter as tk#first import tkinter
# # from tkinter import ttk
# win=tk.Tk()#we create the object by calling tk class
# name_label=ttk.Label(win,text="Enter your name :")
# name_label.grid(row=0,column=0,sticky=tk.W)
# name_var=tk.StringVar()
# name_entry=ttk.Entry(win,width=16,textvariable=name_var)
# name_entry.focus()
# name_entry.grid(row=0,column=1)
# age_label=ttk.Label(win,text="Enter Your age :")
# age_label.grid(row=1,column=0,sticky=tk.W)
# age_var=tk.IntVar()
# age_entry=ttk.Entry(win,width=16,textvariable=age_var)
# age_entry.grid(row=1,column=1)
# email_label=ttk.Label(win,text="Enter Your Email ID :")
# email_label.grid(row=2,column=0,sticky=tk.W)
# email_var=tk.StringVar()
# email_entry=ttk.Entry(win,width=16,textvariable=email_var)
# email_entry.grid(row=2,column=1)
# gender_label=ttk.Label(win,text="Select Your Gender :")
# gender_label.grid(row=3,column=0,sticky=tk.W)
# gender_var=tk.StringVar()
# gender=ttk.Combobox(win,width=16,textvariable=gender_var,state="readonly")
# gender.grid(row=3,column=1,)
# gender["values"]=("male","female","other")
# gender.current(0)
# rb_var=tk.StringVar()
# radio_btn=ttk.Radiobutton(win,text="student",value="student",variable=rb_var)
# radio_btn.grid(row=4,column=0)
# radio_btn1=ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=rb_var)
# radio_btn1.grid(row=4,column=1)
# chek_var=tk.IntVar()
# chk_btn=ttk.Checkbutton(win,text="I agree terms & conditions",variable=chek_var)
# chk_btn.grid(row=5,column=0)
# def action():
#     UN=name_var.get()
#     age=age_var.get()
#     email=email_var.get()
#     gender=gender_var.get()
#     rb=rb_var.get()
#     if chek_var.get()==0:
#         chk="No"
#     else:
#         chk="YES"
#     print(f"User Name={UN} AGE={age} EMAIL ID={email},GENDER IS {gender},{rb},{chk}")
#     os.chdir(r"f:\python")
#     # with open("tkinter.txt","a")as f:
#     #     f.write(f"{UN},{age},{email},{gender},{rb},{chk}\n")
#     with open("file3.csv","a",newline="")as f:
#         dict_writer=DictWriter(f,fieldnames=["username","age","emailid","gender","type of subscriber","subsribed or not"])
#         if os.stat("file3.csv").st_size==0:
#             dict_writer.writeheader()
#
#
#         dict_writer.writerow({"username":UN,
#                           "age":age,
#                          "emailid":email,
#                          "gender":gender,
#                          "type of subscriber":rb,
#                          "subsribed or not":chk})
#
#
#     name_label.configure ( foreground="blue" )
#     name_entry.delete ( 0, tk.END )
#     age_entry.delete ( 0, tk.END )
#     email_entry.delete ( 0, tk.END )
#
# ttk.Button(win,text="SUBMIT",command=action).grid(row=6,column=1)
# # win.mainloop()#this function will show the gui application
#
# import csv
# from csv import DictWriter
# import os
# import datetime
# import shutil
# import tkinter as tk#first import tkinter
# from tkinter import ttk
# bk=tk.Tk()
# bk.title("Bank Regestration form")
# ttk.Label(bk,text="Bank Account Regestration Form").grid(row="0",column="0")
# ttk.Label(bk,text="Accoun Type").grid(row="1",column="0",sticky=tk.W)
# ttk.Label(bk,text="Please specify the type of account you want to open.*").grid(row="3",column="0",sticky=tk.W)
# cb_var=tk.StringVar
# cb_box=ttk.Combobox(bk,width="50",state="readonly",textvariable=cb_var)
# cb_box.grid(row=4,column="0",sticky=tk.W)
# cb_box["values"]=("*please select*","checking account","savings account","certificate of deposit(cd)","money market account","ira")
# cb_box.current(0)
# ttk.Label(bk,text="Currency*").grid(row="5",column="0",sticky=tk.W)
# rb_var=tk.StringVar()
# rb=ttk.Radiobutton(bk,text="USD",value="USD",variable=rb_var)
# rb.grid(row="6",column="0",sticky=tk.W)
# rb1=ttk.Radiobutton(bk,text="EUR",value="EUR",variable=rb_var)
# rb1.grid(row="7",column="0",sticky=tk.W)
# ttk.Label(bk,text="Contact Information").grid(row="8",column="0",sticky=tk.W)
# ttk.Label(bk,text="Name*").grid(row="9",column="0",sticky=tk.W)
# cb_var1=tk.StringVar
# cb_box1=ttk.Combobox(bk,width="8",state="readonly",textvariable=cb_var)
# cb_box1.grid(row=10,column="0",sticky=tk.W)
# cb_box1["values"]=("Title","Ms","Miss","Mrs","Mr")
# cb_box1.current(0)
# first_var=tk.StringVar()
# fst_box=ttk.Entry(bk,width=10,textvariable=first_var)
# fst_box.grid(row="10",column="0")
# bk.mainloop()
'''Label frame & pad'''
import tkinter as tk
from tkinter import ttk
import csv
import datetime
from csv import DictWriter
import os

loop=tk.Tk()
loop.title("widjets")
label_frame=ttk.LabelFrame(loop)
label_frame.grid(row=0,column=0)
labels=["Enter ur name :","Enter ur age :","Enter ur mail id:","enter ur city :","entr ur pincode :"]
for i in range(len(labels)):
    new_label="label"+str(i)
    new_label=ttk.Label(label_frame,text=labels[i])
    new_label.grid(row=i,column=0,sticky=tk.W,padx=40,pady=2)
    print(new_label)
user_entry={"name":tk.StringVar(),
           "age":tk.IntVar(),
            "mail id":tk.StringVar(),
            "city":tk.StringVar(),
            "pincode":tk.IntVar()}
# entry=ttk.Entry(loop,width=16,textvvariable=name_var)
# entry.grid(row=1,column=1)
count=0
for i in user_entry:
    entry=i+"entry_box"
    entry=ttk.Entry(label_frame,width=16,textvariable=user_entry[i])
    entry.grid(row=count,column=1)
    count=count+1


def action():
    print(user_entry["name"].get())
    print ( user_entry["age"].get () )
    print ( user_entry["mail id"].get () )
    print ( user_entry["city"].get () )
    print ( user_entry["pincode"].get () )
    os.chdir(f"f:\python")
    with open("file.csv","a")as f:
          dict_writer=DictWriter(f,fieldnames=["name","age","mail id","city","pincode"])
          if os.stat("file.csv").st_size==0:
              dict_writer.writeheader()

          dict_writer.writerow({"name":user_entry["name"].get(),
                                 "age":user_entry["age"].get(),
                                 "mail id":user_entry["mail id"].get(),
                                 "city":user_entry["city"].get(),
                                 "pincode":user_entry["pincode"].get()})

def date():
    x=date()
    return x

submit=ttk.Button(loop,text="submit",command=action).grid(row=6,columnspan=2)


loop.mainloop()
