#
# # #DECORATORS IS A FUNCTION IT INCREASE THE FUNCTIONALITY OF OTHER FUNCTIONS
# def decorate_func(any_function):
#     def wrape_func():
#         print("this is awesome function")
#         return any_function()
#     return wrape_func
# def func1():
#     print("this is function1")
#
# def func2():
#     print("this is function2")
# # var1=decorate_func(func1)
# # var2=decorate_func(func2)
# # var1(),var2()
# #
# #
# @decorate_func
# def func1():
#     print("this is function1")
#
# # @decorate_func
# # def func2():
# #     print("this is function2")
# func1()
# # func2()
# # from functools import wraps
# # def deccorate_func2(any_func):
# #     @wraps(any_func)#it override by any_func
# #     def wrap_func(*args,**kwargs):
# #         '''this is wrap function'''
# #         total=1
# #         for i in args:
# #             total*=i
# #         print(total)
# #         print("this is awesome function")
# #         return any_func(*args,**kwargs)
# #     return wrap_func
# #
# # @deccorate_func2
# # def add(a,b):
# #     '''this is add function'''#for this doc string we have to import wrap module
# #     return a+b
# # @deccorate_func2
# # def sum(a,b,c):
# #     '''this is sum function'''
# #     return a+b+c
# # # print(add(5,9))
# # # print(add.__doc__)
# # print(sum(5,4,3))
# # print(sum.__doc__)
# from functools import wraps
# def print_function_data(any_func):
#     @wraps(any_func)
#     def wrap_func(*args,**kwargs):
#         print("you are calling",any_func.__name__,"function")
#         print(any_func.__doc__)
#         return any_func(*args,**kwargs)
#     return wrap_func
# @print_function_data
# def sum2(a,b):
#     '''this function takes two numbers as parameters and return their sum'''
#     return a+b
# print(sum2(5,4))
from functools import wraps
import time
def cal_time(any_func):
    @wraps(any_func)
    def wrap_func(*args,**kwargs):
        print(f'executing...{any_func.__name__} function')
        t1 = time.time ()
        returned_val= any_func(*args,**kwargs)
        t2 = time.time ()
        print (f'{t2 - t1} seconds')
        return returned_val
    return wrap_func
@cal_time
def fibbonacci():
    a=0
    b=1
    series=int(input("enter the rangee of seriees"))
    for i in range(series):
        print(a)
        c=a+b
        a=b
        b=c
    return c
print(fibbonacci())
# data type checking by using decoraters
# def decorater(func):
#     def wrapper(*args,**kwargs):
#        if all([type(i)==int or type(i)==float for i in args]):
#              return func(*args,**kwargs)
#        else:
#                 print("wrong arguments")
#     return wrapper

# @decorater
# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(add(7,9,10,2.5,3.6,'jfdg'))
#
# def input_data_type(data_type):
#     def decorate(function):
#         def wrap(*args,**kwargs):
#             if all([type(i)==data_type for i in args]):
#              return function(*args,**kwargs)
#             else:
#                 print(f'wrong data type')
#         return wrap
#     return decorate
# @input_data_type(int)
# def add2(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(add2(9,6,2.3))

#GENERATOR:IT IS NOTHING BUT ITERATOR WHERE WE USED FOR MEMORY SAVING.
# def square():
#     l=[]
#     for i in range(1,10):
#         l.append(i**2)
#     yield l
# print(square())
# var=square()
# for i in var:
#     print(i)
# for i in var:#this loop will not give any data because it is generator. one time only
#     print(i)
# def square(a):
#     return a**2
# print(square(5))
# l=[1,2,3,4]#iterable
# i=iter(l)
# print(i)
# print(next(i))#this is iterator
# print(next(i))
# print(next(i))
# print(next(i))
# l1=list(map(lambda a:a**2,l))#iterator
# print(l1)
# square=[i**2 for i in range(1,11)]#list comprehension
# print(square)
# square=(i**2 for i in range(1,11))#generator comprehension
# print (square)#it gives generator object
# for i in square:
#     print(i)
# for i in square:#here will not give the output when we using generator it will not give the output more than one time
#     print(i)

#OBJECT ORIENTED PROGRAMING. IN PYTHON EVERYTHING IS A OBJECT
# #CREATING OWN CLASS
# class Person:
#     def __init__(self,first_name,last_name,age):#first_name,last_name,age are called attributes
#         print("calling init method")
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#
# p1=Person("harika","golla",26)#p1 is an object
# p2=Person("anil","golla",30)#p2 is an object
# print(p1.first_name)
# print(p2.first_name)
# #EXERCISE
# class Laptop :
#     def __init__(self, brand_name,model_name,price) :  # first_name,last_name,age are called attributes
#         print ( "calling init method" )
#         #instance variables
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price =price
#     def apply_discount(self,percentage):
#            return self.price-((self.price*percentage)//100)
#
# p1 = Laptop( "lenovo", "2006", 2600 )  # p1 is an object or instance
# p2 = Laptop ( "dell", "2002", 3000 )  # p2 is an object
# print ( p1.brand_name )
# print ( p2.model_name )
# print(p1.apply_discount(10))
# #instance methods
# class Person :
#     def __init__(self, first_name, last_name, age) :
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_name(self):#instancee method
#         return f"{self.first_name}{self.last_name}"
#     def is_above_age(self):#instance method
#         if self.age>18:
#             return f"age is greaterthan 18"
#         return f"age is below 18"
# p1 = Person ( "harika", "golla", 12 )  # p1 is an object
# p2 = Person ( "anil", "golla", 30 )  # p2 is an object
# print ( p1.first_name )
# print ( p2.first_name )
# print(p1.full_name())
# print(Person.full_name(p1))
# print(p2.is_above_age())
# #instance variables:where we declaring variables inside the class
# class Circle:
#     '''it is circle class'''
#     pi=3.14#class variable or instance variable
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#          return 2*self.pi*self.radius
#
# a=Circle(10)
# # a.pi=2.7
# print(a.area())
# print(a.__dict__)#all variables will be showm
# print(a.__class__)#calss name display
# print(a.__doc__)#comments will bee shown
# print(a.__dir__)#memory location abject
#Exercise:a class has how many objects
class Teacher:
    count=0#class variable/class attribute
    def __init__(self,first,last,age):#it is constructor
       Teacher.count+=1
       self.first_name=first
       self.last_name=last
       self.age=age
    @classmethod# it is decorator
    def count_instance(cls):#class method
        return f"u have created {cls.count} instances of {cls.__name__} class"

    def full_name(self):#instancee method
        return f"{self.first_name}{self.last_name}"

    @classmethod
    def from_string(cls,string):#in another way to create object
        first,last,age=string.split(",")
        return cls(first,last,age)
    @staticmethod
    def hello():
        print("hello,static method calling")
print(Teacher.__dict__)
# b1=Teacher("harika","golla",25)
# b2=Teacher("anil","golla",31)
# b3=Teacher("deepak","golla",2)
# b4=Teacher.from_string("harika,golla,25")
#
# print(Teacher.count)#class variable calling
#
# print(Teacher.count_instance())#class method calling
#
# print(b1.full_name())#b1 object is creeateed by init constructor
# print(b4.full_name())#b4 object is createed by from_string constructor

# Teacher.hello()#static method calling

#property,setter,getter decoraters
# class Laptop:
#     def __init__(self,model_name,brand_name,price):
#         self.model=model_name
#         self.brand=brand_name
#         self._price=max(price,0)
#         # self.complete_specificatin=f"laptop brand is {self.brand} model is {self.model} and price is{self._price}"
#     @property#here we useed property deecorator thas y it automatically change the price whateveer we given
#     def complete_specification(self):
#         return f"laptop brand is {self.brand} model is {self.model} and price is{self._price}"
#     def calling(self,number):
#         return f"calling number {number}"
#
# a1=Laptop("dell","2007",-2500)
# print(a1.calling(905271618))
# print(a1.__dict__)
# a1._price=500
# # print(a1.complete_specificatin)
# print(a1.complet e_specification)#actually it is method but there is no need to call like a function
# print(a1._price)
# print()

#INHERITANCE:frombase class to deriveed class inherit all the methods,variables etc....
class Normal_phone:#super class/base class/parent class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def mobile_description(self):
        return f"mobile brand is {self.brand} model is {self.model} price is {self.price}"

class Smart_phone(Normal_phone):#sub class/derived class/child class
    def __init__(self,brand,model,price,ram,internal_memory,camera):
        #first way
        # Normal_phone.__init__(self,brand,model,price)#inherite base class instancees to derived class

        super().__init__(brand,model,price)#second way
        self.ram=ram
        self.internal_memory=internal_memory
        self.camera=camera
#
# phone=Normal_phone("nokia","2001",2500)
# iphone=Smart_phone("nokia","2001",2500,"4g","8gb","200px")
# print(phone.__dict__)
# print(iphone.__dict__)
# print(iphone.mobile_description())
# print(isinstance(iphone,Smart_phone))#isinstance is finding the object of which class
# print(issubclass(Smart_phone,Normal_phone))#issubclass is finding the given class is subclass or not
#MULTIPLE INHERITANCE:IF MOREETHAN ONE CLASS INHERIT TO THE SINGLE CLASS IS CALLED MULTIPLE INHERITANCE
# class A:
#     def class_a(self):
#         return f"this is class a method"
#     def hello(self):
#         return f"calling hello method from class a"
# class B:
#     def class_a(self):
#         return f"this is class a method"
#     def hello(self):
#         return f"calling hello method from class a"
# class C(A,B):
#     pass
# instance_a=A()
# instance_b=B()
# instance_c=C()
# print(instance_c.hello())#it is folloing by method revolution order
# print(help(C))#finding method revolution order or MRO
# print(C.__mro__)#it gives mro in tuple
# print(C.mro())#it gives mro in list

# class AA:
#     def __init__(self,a1,a2):
#         self.a1=a1
#         self.a2=a2
#     def __str__(self):
#         return f"hi this is str method"
#     def __repr__(self):
#         print(f"hi this is representation method")
#         return f"AA(\'{self.a1}\',\'{self.a2}\')"#this will represent like a object
#     def full_name(self):
#         return f'{self.a1} {self.a2}'
#     def __len__(self):
#         return len(self.full_name())
#     def __add__(self, other):
#         return self.a1+other.a1
#     def __abs__(self):
#
#
# obj=AA("harika","golla")
# obj2=AA("harika","golla")
# print(obj)#try only with init method
# print(obj)#try including str method
# print(obj.__str__())#or print(str(obj))
# print(obj.__repr__())#or print(repr(obj))
# print(obj.full_name())
# print(obj.__len__())
# print(obj+obj2)
# print(len(obj))

#ERRORS(IN BUILT ERRORS)
#1.SYNTAX ERROR
# def func:
#2.INDENTATION ERROR
# for i in range(1,11):
# print(i)
#3.NAME ERROR
# print(name)#here name is not difined
#4.INDEX ERROR
# l=[1,2,3]
# print(l[3])#here list is out of rangee
#5.VALUE ERROR
# b="fgg"
# int(b)
#6.ATTRIBUTE ERROR
# l=[1,2,1,3]
# l.push(12)
#KEY ERROR
# dict={"name":"harika"}
# print(dict["age"])
#ERROR RAISING:the program will not be terminated if we raise the eroor
# def add(a,b):
#     if type(a)==int and type(b)==int:
#         return a+b
#     raise ValueError("u r parsing wrong data type")
# # print(add(2,"5"))
#
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         raise NotImplementedError("u have to define this method in sub classes")
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed
#     def sound(self):
#         return f"bow bow"
# class Cat(Dog):
#     def __init__(self,name,breed):
#         super().__init__(name,breed)
#     def sound(self):
#         return f"maew maew maew"
# dogy=Dog("daber","pug")
# Caty=Cat("sunny","milk")
# print(dogy.sound())
# print(Caty.sound())
# help(dogy)
# print(Cat.mro())
# while True:
#     try:
#         age=int(input("enter ur age"))
#         break
#     except ValueError:
#         print( "u entered wrong data type" )
#     except:
#         print("unexpected error")
# if age<18:
#     print("u can't play the game")
# else:
#     print("u can play the game")

# def division(a,b):
# try:
#     a=int(input("a="))
#     b=int(input("b="))
#     print(a/b)
# except ZeroDivisionError as err:
#     print(err)
# except TypeError as err:
#     print(err)
# except:
#     print("unexcepected error")
# else:#if there is no errors in try block then it will continue with the else block
#     print(f"u r taking the values a and b are:{a},{b}")
# finally:#if theere is error or no error finall block will always excuted
#     print("hi...!!")
#
# print(division(5,2))

# class UrSoYoung(ValueError):
#     pass
# age=int(input("enter ur age"))
# if age>18:
#     raise UrSoYoung("u r so young")#raising own error

#DEBUGGING:DEBUGGING MEANS FIND AND RESOLVE THE PROBLEMS WITH IN A COMPUTER PROGRAM
# import pdb
# pdb.set_trace()
# name=input("enter the name")
# age=input("enter the age")
# print(f"heello {name} ur agee is {age}")
# age2=int(age)+5
# print(f"hi {name} ur age will be {age2} years after 5 years")

#debugging commands
# l:will show in which line
# n:move to the next line
# q:quit the progrram
# c:continue to execution

#READ FILE

# f=open(r"C:\Users\Katthik\Desktop\Harika\honey.txt","r")#by default read mode
# print(f.read())#file reading
# print(f.read())#it will not read the file again bcz the cursor will at last position
# print(f"cursor position is {f.tell()}")
# print(f"cursor position to change in 0 place {f.seek(0)}")
# # print(f.read())#now we can read the file
# # print(f.readline(),end="")#read the file line by line
# # print(f.readline(),end="")
# # print(f.readlines())#it will read the file and return in list format
# for line in f.readlines()[::2]:#we can do loop also
#     print(line,end="")
# print()
# print(f.name)#will shown file name
# print(f.closed)#find file will close or not
# f.close()#close the file
# print(f.closed)

# with open("hello","a") as fi:
#     # print(fi.write("hello"))#it override the file with hello
#     print(fi.write("\nhello"))
# print(fi.closed)
#
# with open("txt1","r+")as f:
#     (f.write("hello.."))

#read the file and write in anoher file
# with open("txt1","r")as rf:
#     with open("file3.txt","w")as wf:
#         wf.write(rf.read())
# with open("newfile","a")as nw:
#     nw.write("harshith,100")
#     nw.write("\nmohith,50")
with open("newfile","r") as rf:
    with open("hello","w",newline="") as wf:
        for line in rf.readlines():
            name,salary=line.split(",")
            wf.write(f"\n{name}'s salary is {salary}")

#CSV FILE READING
# from csv import reader
# with open("csv.txt","r") as cf:
#     data=reader(cf)
#     print(data)
#     for row in data:
#         print(row)
# from csv import DictReader
# with open("csv.txt","r") as cf:
#     data=DictReader(cf)
#     print(data)
#     for row in data:
#         print(row)
#         print(row["name"])
#csv file writing
# from csv import writer
# with open("cswrite.txt","w",newline="")as cw:
#     cw_writer=writer(cw)
#     #there is two methods to write csv files
#     #method1
#     # cw_writer.writerow(["name","countries"])
#     # cw_writer.writerow(["harika","india"] )
#     # cw_writer.writerow(["deepak","india"] )
#     #method2
#     cw_writer.writerows([["name","countries"],["harika","india"],["deepak","india"]])
#
# from csv import DictWriter
# with open("cswrite.txt","w",newline="")as cw:
#     cw_writer=DictWriter(cw,fieldnames=["name","countries"])
#     cw_writer.writeheader()
#     #there is two methods to write csv files
#     #method1:writerow
#     # cw_writer.writerow({"name":"harika",
#     #                      "countries":"india"})
#     # cw_writer.writerow ({"name" : "deepak",
#     #                   "countries":"india"} )
#     #method2
#     cw_writer.writerows([{"name":"harika","countries":"india"},{"name" : "deepak", "countries":"india"}])



import random
from tkinter import*
from tkinter import messagebox
root=Tk()
# root.geometry("100x100+0+0")
root.title("Number guessing Game")
# root.config(bg="green")
label=Label(root,text="Guess The Number :")
label.grid(row=0,column=0)
num_var=StringVar()
entry=Entry(root,width=10,textvariable=num_var)
entry.grid(row=0,column=1)
def action():
    main_num=10
    found=False
    num1=num_var.get()
    num=int(num1)
    while not found:
        if num==main_num:
            messagebox.showinfo("title","U guessed right number")
            found=True
            break
        else:
            if num < main_num:
                messagebox.showinfo("title","the number is low!")
            else:

                messagebox.showinfo("title","the number is high")
        # continue
button=Button(root,text="SUBMIT",command=action)
button.grid(row=1,columnspan=2)
root.mainloop()
