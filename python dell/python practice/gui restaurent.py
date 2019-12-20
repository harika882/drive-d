# from tkinter import*
# import time
# import random
#
# root=Tk()
# root.geometry("1600x800+0+0")
# root.title("restaurent managemeent system")
#
#
# top=Frame(root,width=1600,height=50,bg="light blue",relief=SUNKEN)
# top.pack(side=TOP)
# left=Frame(root,width=800,height=700,relief=SUNKEN)
# left.pack(side=LEFT)
# right=Frame(root,width=300,height=700,bg="light blue",relief=SUNKEN)
# right.pack(side=RIGHT)
#
# label1=Label(top,font=("arial","50","bold"),fg="Red",text="Restaurent Management System",bd=10,anchor="w")
# label1.grid(row=0,column=0)
# localtime=time.asctime(time.localtime(time.time()))
# label2=Label(top,font=("arial","30","bold"),fg="Green",text=localtime,bd=10,anchor="w")
# label2.grid(row=1,column=0)
#
# labels_list=["referance :","Large Fries :","Burger Meal :","Filet_o_Meal :","Chicken Meal :","Cheese Meal :","Drinks :","Cost of Meal :","Service Charge :","State Tax :","Sub Total :","Total Cost :"]
# for i in range(0,6):
#     label_name="label"+str(i)
#     label_name=Label(left,font=("arial","16","bold"),text=labels_list[i],fg="green",anchor="w")
#     label_name.grid ( row=i, column=0,padx=40,pady=2 )
#
# count=0
# for i in range(6,len(labels_list)):
#     label_name2="label"+str(i)
#     label_name2=Label(left,font=("arial","16","bold"),text=labels_list[i],fg="green",anchor="w")
#     label_name2.grid ( row=count,column=2,padx=40,pady=2 )
#     count=count+1
#
#
# Entry_list={"referance :":StringVar(),
#             "Large Fries :":StringVar(),
#             "Burger Meal :":StringVar(),
#             "Filet_o_Meal :":StringVar(),
#             "Chicken Meal :":StringVar(),
#             "Cheese Meal :":StringVar()}
# Entry_list2={"Drinks :":StringVar(),
#             "Cost of Meal :":StringVar(),
#             "Service Charge :":StringVar(),
#             "State Tax :":StringVar(),
#             "Sub Total :":StringVar(),
#             "Total Cost :":StringVar()}
# count1=0
# for i in Entry_list:
#     entry=Entry(left,font=("arial","16","bold"),width=15,textvariable=Entry_list[i],insertwidth=4,justify="right")
#     entry.grid(row=count1,column=1,padx=5,pady=2)
#     count1+=1
# count2=0
# for i in Entry_list2 :
#     entry = Entry ( left, font=("arial", "16", "bold"), width=15, textvariable=Entry_list2[i], insertwidth=4,justify="right")
#     entry.grid ( row=count2, column=3,padx=2,pady=2 )
#     count2 += 1
#
# def ref():
#     x=random.randint(1,2000)
#     rand_num=str(x)
#     Entry_list["referance :"].set(rand_num)
#     cof=(float(Entry_list["Large Fries :"].get()))*25
#     cobm=(float(Entry_list["Burger Meal :"].get()))*250
#     cofom=(float(Entry_list["Filet_o_Meal :"].get()))*300
#     cochm=float(Entry_list["Chicken Meal :"].get())*375
#     cochesm=float(Entry_list["Cheese Meal :"].get())*350
#     codr=float(Entry_list2["Drinks :"].get())*200
#     com=(cof+cobm+cofom+cochm+cochesm+codr)
#     ser_char=com/0.99
#     state_tax=com*0.4
#     sub_tot=ser_char+state_tax
#     total_cost=(com+sub_tot)
#     Entry_list2["Cost of Meal :"].set(com)
#     Entry_list2["Service Charge :"].set(ser_char)
#     Entry_list2["State Tax :"].set(state_tax)
#     Entry_list2["Sub Total :"].set(sub_tot)
#     Entry_list2["Total Cost :"].set(total_cost)
#
# def reset():
#     for i in Entry_list:
#         Entry_list[i].set("")
#     for i in Entry_list2:
#         Entry_list2[i].set("")
#
# def exit():
#     root.destroy()
#
#
# total_btn=Button(left,text="Total",command=ref,width=15,bg="light blue",fg="black")
# total_btn.grid(row=6,column=1)
# reset_btn=Button(left,text="Reset",command=reset,width=15,bg="light blue",fg="black")
# reset_btn.grid(row=6,column=2)
# quit_btn=Button(left,text="Quit",command=exit,width=15,bg="light blue",fg="black")
# quit_btn.grid(row=6,column=3)
# root.mainloop()
#




'''tabs creating'''
from tkinter import*
import tkinter as tk
from tkinter import ttk
import os
from csv import DictWriter
import csv
import time
import random
nb=tk.Tk()
nb.geometry("800x800+0+0")
nb.title("Tabs")
nb1=ttk.Notebook()
paze1=ttk.Frame(nb1)
paze2=ttk.Frame(nb1)
paze3=ttk.Frame(nb1)
nb1.add(paze1,text="First Tab")
nb1.add(paze2,text="second tab")
nb1.add(paze3,text="third tab")
nb1.grid(row=0,column=0)
name_label=ttk.Label(paze1,text="Enter your name :")
name_label.grid(row=0,column=0,sticky=tk.W)
name_var=tk.StringVar()
name_entry=ttk.Entry(paze1,width=16,textvariable=name_var)
name_entry.focus()
name_entry.grid(row=0,column=1)
age_label=ttk.Label(paze1,text="Enter Your age :")
age_label.grid(row=1,column=0,sticky=tk.W)
age_var=tk.IntVar()
age_entry=ttk.Entry(paze1,width=16,textvariable=age_var)
age_entry.grid(row=1,column=1)
email_label=ttk.Label(paze1,text="Enter Your Email ID :")
email_label.grid(row=2,column=0,sticky=tk.W)
email_var=tk.StringVar()
email_entry=ttk.Entry(paze1,width=16,textvariable=email_var)
email_entry.grid(row=2,column=1)
gender_label=ttk.Label(paze1,text="Select Your Gender :")
gender_label.grid(row=3,column=0,sticky=tk.W)
gender_var=tk.StringVar()
gender=ttk.Combobox(paze1,width=16,textvariable=gender_var,state="readonly")
gender.grid(row=3,column=1,)
gender["values"]=("male","female","other")
gender.current(0)
rb_var=tk.StringVar()
radio_btn=ttk.Radiobutton(paze1,text="student",value="student",variable=rb_var)
radio_btn.grid(row=4,column=0)
radio_btn1=ttk.Radiobutton(paze1,text="Teacher",value="Teacher",variable=rb_var)
radio_btn1.grid(row=4,column=1)
chek_var=tk.IntVar()
chk_btn=ttk.Checkbutton(paze1,text="I agree terms & conditions",variable=chek_var)
chk_btn.grid(row=5,column=0)
def action():
    UN=name_var.get()
    age=age_var.get()
    email=email_var.get()
    gender=gender_var.get()
    rb=rb_var.get()
    if chek_var.get()==0:
        chk="No"
    else:
        chk="YES"
    print(f"User Name={UN} AGE={age} EMAIL ID={email},GENDER IS {gender},{rb},{chk}")
    os.chdir(r"f:\python")
    # with open("tkinter.txt","a")as f:
    #     f.write(f"{UN},{age},{email},{gender},{rb},{chk}\n")
    with open("file3.csv","a",newline="")as f:
        dict_writer=DictWriter(f,fieldnames=["username","age","emailid","gender","type of subscriber","subsribed or not"])
        if os.stat("file3.csv").st_size==0:
            dict_writer.writeheader()


        dict_writer.writerow({"username":UN,
                          "age":age,
                         "emailid":email,
                         "gender":gender,
                         "type of subscriber":rb,
                         "subsribed or not":chk})


    name_label.configure ( foreground="blue" )
    name_entry.delete ( 0, tk.END )
    age_entry.delete ( 0, tk.END )
    email_entry.delete ( 0, tk.END )

ttk.Button(paze1,text="SUBMIT",command=action).grid(row=6,column=1)

ttk.Label(paze2,text="Bank Account Regestration Form").grid(row="0",column="0")
ttk.Label(paze2,text="Accoun Type").grid(row="1",column="0",sticky=tk.W)
ttk.Label(paze2,text="Please specify the type of account you want to open.*").grid(row="3",column="0",sticky=tk.W)
cb_var=tk.StringVar
cb_box=ttk.Combobox(paze2,width="50",state="readonly",textvariable=cb_var)
cb_box.grid(row=4,column="0",sticky=tk.W)
cb_box["values"]=("*please select*","checking account","savings account","certificate of deposit(cd)","money market account","ira")
cb_box.current(0)
ttk.Label(paze2,text="Currency*").grid(row="5",column="0",sticky=tk.W)
rb_var=tk.StringVar()
rb=ttk.Radiobutton(paze2,text="USD",value="USD",variable=rb_var)
rb.grid(row="6",column="0",sticky=tk.W)
rb1=ttk.Radiobutton(paze2,text="EUR",value="EUR",variable=rb_var)
rb1.grid(row="7",column="0",sticky=tk.W)
ttk.Label(paze2,text="Contact Information").grid(row="8",column="0",sticky=tk.W)
ttk.Label(paze2,text="Name*").grid(row="9",column="0",sticky=tk.W)
cb_var1=tk.StringVar
cb_box1=ttk.Combobox(paze2,width="8",state="readonly",textvariable=cb_var)
cb_box1.grid(row=10,column="0",sticky=tk.W)
cb_box1["values"]=("Title","Ms","Miss","Mrs","Mr")
cb_box1.current(0)
first_var=tk.StringVar()
fst_box=ttk.Entry(paze2,width=10,textvariable=first_var)
fst_box.grid(row="10",column="0")
top=Frame(paze3,width=1600,height=50,bg="light blue",relief=SUNKEN)
top.pack(side=TOP)
left=Frame(paze3,width=800,height=700,relief=SUNKEN)
left.pack(side=LEFT)
right=Frame(paze3,width=300,height=700,bg="light blue",relief=SUNKEN)
right.pack(side=RIGHT)

label1=Label(top,font=("arial","50","bold"),fg="Red",text="Restaurent Management System",bd=10,anchor="w")
label1.grid(row=0,column=0)
localtime=time.asctime(time.localtime(time.time()))
label2=Label(top,font=("arial","30","bold"),fg="Green",text=localtime,bd=10,anchor="w")
label2.grid(row=1,column=0)

labels_list=["referance :","Large Fries :","Burger Meal :","Filet_o_Meal :","Chicken Meal :","Cheese Meal :","Drinks :","Cost of Meal :","Service Charge :","State Tax :","Sub Total :","Total Cost :"]
for i in range(0,6):
    label_name="label"+str(i)
    label_name=Label(left,font=("arial","16","bold"),text=labels_list[i],fg="green",anchor="w")
    label_name.grid ( row=i, column=0,padx=40,pady=2 )

count=0
for i in range(6,len(labels_list)):
    label_name2="label"+str(i)
    label_name2=Label(left,font=("arial","16","bold"),text=labels_list[i],fg="green",anchor="w")
    label_name2.grid ( row=count,column=2,padx=40,pady=2 )
    count=count+1


Entry_list={"referance :":StringVar(),
            "Large Fries :":StringVar(),
            "Burger Meal :":StringVar(),
            "Filet_o_Meal :":StringVar(),
            "Chicken Meal :":StringVar(),
            "Cheese Meal :":StringVar()}
Entry_list2={"Drinks :":StringVar(),
            "Cost of Meal :":StringVar(),
            "Service Charge :":StringVar(),
            "State Tax :":StringVar(),
            "Sub Total :":StringVar(),
            "Total Cost :":StringVar()}
count1=0
for i in Entry_list:
    entry=Entry(left,font=("arial","16","bold"),width=15,textvariable=Entry_list[i],insertwidth=4,justify="right",relief="ridge")
    entry.grid(row=count1,column=1,padx=5,pady=2)
    count1+=1
count2=0
for i in Entry_list2 :
    entry = Entry ( left, font=("arial", "16", "bold"), width=15, textvariable=Entry_list2[i], insertwidth=4,justify="right",relief="sunken")
    entry.grid ( row=count2, column=3,padx=2,pady=2 )
    count2 += 1

def ref():
    x=random.randint(1,2000)
    rand_num=str(x)
    Entry_list["referance :"].set(rand_num)
    cof=(float(Entry_list["Large Fries :"].get()))*25
    cobm=(float(Entry_list["Burger Meal :"].get()))*250
    cofom=(float(Entry_list["Filet_o_Meal :"].get()))*300
    cochm=float(Entry_list["Chicken Meal :"].get())*375
    cochesm=float(Entry_list["Cheese Meal :"].get())*350
    codr=float(Entry_list2["Drinks :"].get())*200
    com=(cof+cobm+cofom+cochm+cochesm+codr)
    ser_char=com/0.99
    state_tax=com*0.4
    sub_tot=ser_char+state_tax
    total_cost=(com+sub_tot)
    Entry_list2["Cost of Meal :"].set(com)
    Entry_list2["Service Charge :"].set(ser_char)
    Entry_list2["State Tax :"].set(state_tax)
    Entry_list2["Sub Total :"].set(sub_tot)
    Entry_list2["Total Cost :"].set(total_cost)

def reset():
    for i in Entry_list:
        Entry_list[i].set("")
    for i in Entry_list2:
        Entry_list2[i].set("")

def exit():
    paze3.destroy()


total_btn=Button(left,text="Total",command=ref,width=15,bg="light blue",fg="black")
total_btn.grid(row=6,column=1)
reset_btn=Button(left,text="Reset",command=reset,width=15,bg="light blue",fg="black")
reset_btn.grid(row=6,column=2)
quit_btn=Button(left,text="Quit",command=exit,width=15,bg="light blue",fg="black")
quit_btn.grid(row=6,column=3)

nb.mainloop()
