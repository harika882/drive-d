# a = int ( input ( "enter the range:" ) )
# for i in range(a):
#     num=i
#     result = 0
#     n=len(str(i))
#     while(i!=0):
#         k=i%10
#         result=result+k**n
#         i=i//10
#     if num==result:
#         print(num)
# first = 0
# second = 1
# # print ( "the fibonacci series is:" )
# # for i in range (2, a ) :
#     # print ( first )
#     # temp = first
#     # first = second
#     # second = temp + first
# # print("prime numbers in the range:")
# # for num in range(a):
# #     if num>1:
# #         for i in range(2,num):
# #             if num%i==0:
# #                break
# #         else:
# #             print(num)
#
# b=int(input("enter the factorial num:"))
# product=1
# a=b
# while(a!=0):
#     product=product*a
#     a=a-1
#     continue
# print(b,"factorial is:",product)
# #
# # for i in range(1,20):
# #     if i==5:
# #         continue
# #     else:
# #         print(i)
# # else:
# #     print("hello")
# # '''a string is polindrum or not and to check number also'''
# # str=input("enter a string:")
# # rev_str=str[::-1]
# # print(rev_str)
# # rev_str1=""
# # for i in range(len(str)):4
# #     rev_str1=str[i]+rev_str1
# # if str==rev_str1:
# #     print("The String is a Polindrum")
# # else:
# #     print("the given string is not a polindrum")
#
# # num=int(input("enter a number:"))
# # num1=str(num)
# # rev_num2=""
# # for i in range(len(num1)):
# #     rev_num2=num1[i]+rev_num2
# # if num1==rev_num2:
# #     print("The given number is a Polindrum")
# # else:
# #     print("the given number is not a polindrum")
# # sum of each digit in given number
# # result=0
# # while(num!=0):
# #     k=num%10
# #     result=k+result
# #     num=num//10
# #
# # # print(result)
# # print('this is \\\\ double blackslash')
# # print("these are /\\/\\/\\/\\/\\ mountain")
# # print("he is\tawesomee")
# # print("\\\"\\n\\t\\\'")
# # print("\U0001F608")
# # name, afe=input("enter name and age").split(",")
# # print(name)
# # print(afe)
# #
# #
# # n1,n2,n3=input("enter three numbers").split(",")
# # n4=int(n1)+int(n2)+int(n3)
# # avg=n4/3
# # print(f"{n1}+{n2}+{n3}",avg)
# # name="Harika is a good girl"
# # name1="     jhhfksasl     "
# # print(name)
# # print(name[::-1])
# # print(len(name))#length method is used for finding length of a string
# # print(name.lower())#lower method is used for to change all letters in lower case
# # print(name.upper())#upper method is used for to change all letters in upper case
# # print(name.title())#title method to change the each word first letter in upper case
# # print(name.count("i"))#count method is used for to find a specific letter in which times
# # print(name1.lstrip())#strip,lstrip,rstrip methods is used to remove the white spaces besides of a string
# # print(name1.rstrip())
# # print(name.replace(" ",".",2))#replace method is used to replace the speccific element
# # print(name.find("is"))#find method is shown the specific element index
# # print(name.center(25,"-"))#it is used to add the specific characters both sides of a string
# # print(name.center(len(name)+4,"@"))
#
# # 06.03.2019
# # win_num=int(input("Guess the number b/w 1 to 100:"))
# # if win_num==5:
# #     print("YOU WIN")
# # else:#nested if else
# #     if win_num>5:
# #         print("your number too high")
# #     else:
# #             print("your number too low")
#
# # name=input("enter name:")
# # age=int(input('enter the age:'))
# # if  (name[0]=="a"or name[0]=="A")and age>10:
# #     print("You can watch coco movie")
# # else:
# #     print("sorry, you cannot watch coco")
#
# #
# # age=int(input('enter person age;'))
# # if age==0 or age<0:
# #     print('u cant watch')
# # elif 0<age<=3:
# #     print("the tkt cost free")
# # elif 4<age<=10:
# #     print("tkt cost:150")
# # elif 11<age<=60:
# #     print("tkt cost: 250")
# # elif age>60:
# #     print("tkt cost:200")
# #
# # total=0
# # i=0
# # while i<11:
# #     total=total+i
# #     i+=1
# # print(total)
# #
# # num=int(input("enter a number:"))
# # result=0
# # while num!=0:
# #     k=num%10
# #     result=result+k
# #     num=num//10
# # print("sum of digits in a given num;",result)
# # num1=str(num)
# #
# # for i in range(len(num1)):
# #     result=result+int(num1[i])
# # print ( "sum of digits in a given num;", result )
#
# # name=input("enter ur name")
# # temp=""
# # for i in range(len(name)):
# #     if name[i] not in temp:
# #         print("{},{}".format(name[i],name.count(name[i]))
# #         temp+=name[i]
#
# # for i in range(1,11):
# #     if i==7:
# #         break
# #     for j in range(1,i+1):
# #         if j==5:
# #             continue
# # #         print(j)
# # win_num=50
# # game_over=False
# # guess=1
# # num=int(input("enter the number:"))
# # while not game_over:
# #     if win_num==num:
# #         print("you win and u guess in",guess,"times")
# #         game_over=True
# #     else:
# #         if num>win_num:
# #             print("too high")
# #         else:
# #             print("too low")
# #
# #         num = int ( input ( "guess again:" ) )
# #         guess += 1
# # same program by using continue and break
# import random
# win_num=random.randint(1,100)
# guess=1
# while True:
#     num = int ( input ( "enter the number:" ) )
#     if win_num == num :
#         print ( "you win and u guess in", guess, "times" )
#         break
#     else :
#         if num > win_num :
#                 print ( "too high" )
#         else :
#                 print ( "too low" )
#
#         guess += 1
#         continue
# # for i in range(11,0,-1):
# #     print(i)
# # def add_two(a,b):
#     # return a+b
#      # print(a+b)
# # print(add_two(5,6))
# # add_two(9,0)
# # def odd_even(num):
# #     if num%2==1:
# #         # print("num is odd")
# #         return "num is odd"
# #     # if num%2==0:
# #         # print("num is even")
# #     return "num is even"
# #
# #
# # print(odd_even(15))
# # num1=int(input("enter the first number;"))
# # num2=int(input("enter the second number"))
# # def greater(num1,num2):
# #     if num1>num2:
# #         return num1
# #     return num2
# # print(greater(num1,num2))
# #
# # def greatest(a,b,c):
# #     bigger=greater(a,b)
# #     return greater(bigger,c) #or without second line return greater(greater(a,b,c)
# # print(greatest(5,9,11))
#
# #  polindrum means word that reads same backwards as forwards
# # def polindrum(string):
# #     # if string==string[::-1]:
# #     return string==string[::-1]
# #     # return False
# # print(polindrum("madam"))
# # num=int(input("enter the range:"))
#
# # def fibonacci(num):
# #     a=0
# #     b=1
# #     if num==1:
# #         print(a)
# #     elif num==2:
# #         return a,b
# #     elif num>2:
# #         print(a,"\n",b)
# #         for i in range(num-2):
# #             c=a+b
# #             a=b
# #             b=c
# #             print(c)
# #
# # print(fibonacci(10))
# # dt.08.03.2019
# # LIST METHODS
# # s={2,3,5,7,9,11}
# # for ele in s:
# #     print(ele)
# # f1=["APPLE","BANANA","ORANGE","GRAPE"]
# # f2=["ROSE","JASMIN","LILLY","SUNFLOWER"]
# # print(len(f1))
# # print(f1)
# # f1.append("fghf")
# # print(f1)
# # print(f1.count("harika"))
# # f1.sort()
# # print(f1)
# # f1.insert(2,"fgjhfg")
# # print(f1)
# # f1.extend(f2)
# # print(f1)
# # print(len(f1))
# # f2.pop(2)
# # print(f2)
# # del (f2)
# # print(f2)
# # f1.remove("harika")
# # print(f1)
# # f1.append(f2)
# # print(f1)
# # # DIFFEERANCEE BETWEEN '==" AND 'IS'
# # print(f1==f2)#here '=='means both list of elements are same or not
# # print(f1 is f2)#here 'is' means both list of elements are stored in same memory or not
# # # split method and join method
# # # split method used to convert string to list
# # name="harika niharika golla".split(".")
# # # name.split()
# # print(name)
# # f3=["jfjh","kfghf","jhgh"]
# # print(' '.join(f1))
# # print(f1)
#
# # def armstrong_num():
# #     n=int(input("enter the range"))
# #     # result=0
# #     for i in range(n):
# #         result=0
# #         num=i
# #         n1=len(str(i))
# #         while (i!=0):
# #             k=i%10
# #             result=result+k**n1
# #             i=i//10
# #         if num==result:
# #             print (result)
# #         # print("it is not armstrong num")
# #
# # # armstrong_num()
# #
# # n = int ( input ( "enter the range of series" ) )
# # def fibbonacci_series(n):
# #     a=0
# #     b=1
# #     if n==1:
# #         print(a)
# #     elif n==2:
# #         print(a,b)
# #     elif n>2:
# #         print(a)
# #         print(b)
# #         for i in range(2,n):
# #             c=a+b
# #             a=b
# #             b=c
# #             print(c)
# #
# # fibbonacci_series(n)
# # 13.03.2019
# # from django.shortcuts import render_to_responce
# # def index(request):
# #         return rnder_to_responce("index.html")
# #
# # l=[2,4,6,8,9]
# # # print(len(l))
# # # for i in range(len(l)):
# # #        print(l[i])
# # num=list(range(0,11))
# # print(num)
# # num.pop()
# # print(num)
# # print(num.index(2))
#
# # def lis_ele(l):
# #         square=[]
# #         for i in l:
# #                 square.append(i**2)
# #         print(square)
# # num=list(range(0,11))
# # # lis_ele(num)
# # l=listint(input("enter the range:"))
# # for i in range(len(l)):
# #         l.append(int(input()))
# # def reverse_list(l):
# #         reverse=[]
# #         for i in range(len(l)):
# #                 reverse.append(l)
# #                 return reverse
#
# # print(reverse_list(l))
# # accesing the elements in list
# # l=[1,2,3,5,7]
# # x=0
# # for i in l:
# #         x+=i
# # print(x)
# # print(l)
# # print(type(l))
# # for ele in range(len(l)):
# #         print(l[ele])
# # taking elements from the input to the list
# # my_list=[]
# # list1=[]
# # n=int(input("enter the range of the list: "))
# # x=0
# # k=1
# # for i in range(n):
# #         my_list.append(int(input()))
# #         x+=my_list[i]
# #         k*=my_list[i]
# # print(my_list)
# # print("sum of the values:",x,"\n multiplication of the numbers:",k)
# # def squares():
# #         my_list = []
# #         list1 = []
# #         n = int ( input ( "enter the range of the list: " ) )
# #         for i in range ( n ) :
# #                 my_list.append ( int ( input () ) )
# #         for i in range(len(my_list)):#squares of the list
# #                 list1.append(my_list[i]**2)
# #         return list1
# # print(squares())
# # def reverse_list(l):
# #         list=[]
# #         for i in range(len(l)):
# #               # list.append(l.pop())
# #                 l.reverse()
# #         return l# or we can write return l[::-1]
# #         # return list
# # l=[2,5,7,9,11]
# # print(reverse_list(l))
# #
# # def reverse_strlist(l):
# #         list=[]
# #         for i in l:
# #                 list.append(i[::-1])
# #                 for ele in i:
# #                         list.reverse()
# #         return list
# # l1=["abc","xyz","poq"]
# # print(reverse_strlist(l1))
# # def rev_str(l):
# #         list=[]
# #         for i in range(len(l)):
# #                 list.append(l.pop())
# #         return list
# # l=["abc","xyz","poq"]
# # print(rev_str(l))
#
# # def odd_even(l):
# #         list1=[]
# #         list2=[]
# #         for i in l:
# #                 if i%2==0:
# #                         list1.append(i)
# #                 else:
# #                         list2.append(i)
# #         output=[list1,list2]
# #         return output
# # l=[1,2,3,4,5,6,7,8,9]
# # print(odd_even(l))
#
# # finding common numbers
# # def com_finder(l1,l2):
# #         l3=[]
# #         for i in l1:
# #                 if i in l2:
# #                         l3.append(i)
# #         return l3
# # l1=[2,4,6,8,10,3,5]
# # l2=sorted(l1)
# # l1.sort()
# # print(sorted(l1))
# # l2=[2,4,7,9,3,5,6,11]
# # print(com_finder(l1,l2))
# #
# # def nes_list(l):
# #         count=0
# #         for i in l:
# #                 if type(i)==list:
# #                         count=count+1
# #         return count
# # # l=[1,2,[3,5],[7,9],[11,3]]
# # # print(nes_list(l))
# # # TUPLE
# # num=(2,4,6,8,9,11,12)
# # print(len(num))
# # print(min(num))
# # print(max(num))
# # print(num.count(2))
#
#
# # DICTIONARIES
# # d={'name':'harika',
# #    'age':27,
# #    'music':'melodies,western,traditional',}
# # print(d)
# # for val in d.keys():
# #     # print(key)
# #     print(val)
# # d1={'qualification':'mca',
# #     'city':'nellore'}
# # d.update(d1)
# # print(d)
# # d2=d.fromkeys(['name','age','city'],'unknown')
# # print(d2)
# # print(d.get('name'))
# # print(d.get('names'))
# # d3=d.copy()
# # print(d3)
# # d2=d.clear()
# # print(d2,'\n', d3)
# # print(d.get('name','not found'))
# # users={}
# # user1={'name':'harika',
# #         'age':27,
# #        'city':'nellore'}
# # user2={'name':'ramya',
# #         'age':27,
# #        'city':'nellore'}
# # user3={'name':'archana',
# #         'age':27,
# #        'city':'nellore'}
# # users.update(user1)
# # users.update(user2)
# # print(users)
#
# # exercise-1 defining a function and find cube of values
# # def cube_finder(n):
# #     cube={}
# #     for i in range(1,n+1):
# #         cube[i]=i**3
# #     return cube
# # print(cube_finder(int(input("enter the range:"))))
#
# # finding fibbonacci series using dictionaries
# # def fib_series(n):
# #     fib={}
# #     a=0
# #     b=0
# #     c=1
# #     for i in range(1,n+1):
# #         fib[i]=c
# #         a=b
# #         b=c
# #         c = a + b
# #     return fib
# # print(fib_series(int(input("enter the range:"))))
#
# # finding prime numbers
# # def prime_num(n):
# #     prime={}
# #     count=1
# #     for num in range(n):
# #         if num>1:
# #            for i in range(2,num):
# #                if(num%i)==0:
# #                 break
# #            else:
# #                prime[count] = num
# #                count += 1
# #     return prime
# # print(prime_num(int(input("enter the range:"))))
#
# # word counter by using dictionaries
# # def word_counter(s):
# #     count={}
# #     for i in s:
# #         count[i]=s.count(i)
# #     return count
# # print(word_counter(['harika','harika','deepak']))
#
# # TAKING INPUT FROM USERS BY USING DICTIONARIES
# d={}
# # d['name']=input("enter ur name:")
# # d['age']=input("enter ur agee")
# # d['fav_movies']=input("enter fav movies by comma").split()
# # d['fav_songs']=input("enter fav songs by comma").split()
# # for key,val in d.items():
# #     print(key,':',val)#printing key and values by using for loop
# # for key in d.keys():#printing key by using for loop
# #     print(key)
# # for val in d.values():#printing values by using for loop
# #     print(val)
#
# #SET
# # s={1,2,3,4,5,6,7,8,9}
# # s1=(1,2,3,4,5,6,7,8,)
# # s2=set(s1)
# # print(type(s2))
# # s.add(11)
# # s.remove(6)
# # s.pop()
# # s.discard(12)#it shown no error if the element is not in set but using remove method it occurs error
# # print(s)
# # for i in s:
# #     print(i)
# # if 3 in s:
# #     print('present')
# # # for i in
# # l=[1,2,3,4,5,1,2,5,7,9]
# # s=set(l)#set removes duplicate values
# # print(s)
# # s1={4,5,6}
# # s2={7,8,9,4,5,6}
# # union_set=s1 | s2
# # print(union_set)
# # inter_section=s1&s2
# # print(inter_section)
#
# # LIST COMPHREHENCES
# # DO THE CODE IN SINGLE LINE
# # SUARES OF NUMBERS
# # square=[]
# # for i in range(1,11):
# #     square.append(i**2)
# # print(square)
# # # the abovee program in a single line by using list comphrehence
# # square=[i**2 for i in range(1,11)]
# # print(square)
# # cube=[i**3 for i in range(1,11)]
# # print(cube)
# # negetive=[-i for i in range(1,11)]
# # print(negetive)
# # s=['harshith','harika','deepak']
# # s1=[i[0] for i in s]
# # print(s1)
# # reverse_string=[i[::-1] for i in s]
# # print(reverse_string)
# # even_num=[i for i in range(1,12) if i%2==0]
# # odd_num=[i for i in range(1,12) if i%2==1]
# # print(f'{even_num},{odd_num}')
# # list=[2,4.0,3,'ghjfd',[2,4,70],'jfg']
# # list1=[str(i) for i in list if type(i)==int or type(i)==float]
# # print(list1)
# # esq_ocub=[i**2 if i%2==0 else i**3 for i in range(1,11)]
# # print(esq_ocub)
# # nested_list=[[i for i in range(1,4)]for j in range(3)]
# # print(nested_list)
# # set comprehension
# # s={ i**2 for i in range(1,11)}
# # print(s)
# # #dictionary comprehension
# # dict={i:i**2 for i in range(1,11)}
# # print(dict)
# # #flexible functions
# # #*ags, *operator
# # def sum(a,b,c,d):
# #     return a+b+c+d
# # print(sum(2,4,6,8))
#
# # def sum(*args):#by using *args we can pass more than one argument
# #     print(args)
# #     total=0
# #     for i in args:
# #         total=total+i
# #     return total
# #
# # print(sum(2,4,8,9,7,5,9,4,9,8,5))
# #
# # #args with normal operator
# # def multiply(num,*args):
# #     total=1
# #     for i in args:
# #         total*=i
# #     return total
# # print(multiply(4,7,8))#4 is going in num and remaining numbers going to args.
# # #parsng a list as argument
# # def multiply(*args):
# #     total=1
# #     for i in args:
# #         total*=i
# #     return total
# # num=list(range(1,11))
# # print(multiply(num))
# # print(multiply(*num))#here we using *num it is doing a list in unpacking
# #
# # #exercise
# # def power(num,*args):
# #     print(args)
# #     if len(args)==0:
# #         print("hey u didnt pass any arguments")
# #     else:
# #         power=[i**num for i in args]
# #         return power
# # num=list(range(1,10))
# # print(power(3,0))
#
#
# #**kwars(double star keword arguments)
# # def func(**kwargs):
# #     print(kwargs)
# #     print(type(kwargs))
# #     for k,v in kwargs.items():
# #         print(k,":",v)
# #
# # func(age=7,age2=8,age3=9,age4=10)
# # dict={"name":"harika","age":24}
# # func(**dict)#dict unpacking
# #
# # #exercise:
# # def func(*args):
# #     for name in args:
# #         print(name)
# #
# # func("harika","deepak","anil")
#
# # LAMDA EEXPRESSION(ANNONYMUS FUNCTION):making a function in a single line
# # def add(a,b):
# #     return a+b
# # add2=lambda a,b:a+b#by using lamda expression
# # print(add2(5,6))
# #
# # multiply=lambda a,b:a*b
# # print(multiply(5,6))
# #
# # num=int(input("enter the number"))
# # is_even=lambda num:num%2==0
# # print(is_even(num))
# #
# # last_char=lambda s:s[-1]
# # print(last_char("harika"))
# #
# # reverse_string=lambda s:s[::-1]
# # print(reverse_string("deepak"))
#
# #MAP FUNCTION (IT MAPS ONE FUNCTION BEHAVIOUR TO OTHER PLACES WER WE USING
# # def square(a):
# #     return a**2
# # l1=[2,4,6,8,9,1,0,5]
# # squares=map(square,l1)#it gives object memory location
# # print(squares)
# # squares=list(map(square,l1))
# # print(squares)
# # squares=list(map(lambda a:a**2,l1))#by using lambda expression
# # print(squares)
# # squares=[a**2 for a in l1]#by using list comprehension
# # print(squares)
#
# #enumerate()function:it tracks thee position ofargument
# # l1=[4,6,"jhfuadhg","abc","456jh"]
# # for pos,item in enumerate(l1):
# #     print(pos,item)
# #
# # #findout the position of item
# # names=["harika","deepak","anil","abs","jhfd"]
# # def target(target):
# #     for pos,item in enumerate(names):
# #         if target==item:
# #             return pos
# # print(target("anil"))
#
# #filter function:filter the items
# # l1=[10,12,23,4,5,6,7,8,9,10]
# # even=tuple(filter(lambda a:a%2==0,l1))
# # print(even)
# # range1=range(1,20)
# # range=range(1,20)
# # even=list(filter(lambda a:a%2==0,range))
# # print(even)
# # even_num=dict(zip(range1,even))#zip function usees to zip the lists,tuples.....
# # print(even_num)
#
# #*OPERATOR WITH ZIP FUNCTION
# # l1=[2,4,6,8,10,12]
# # l2=[5,8,7,4,9,4,5]
# # pack=list(zip(l1,l2))#combinding two lists into single list
# # print(pack)
# # l1,l2=list(zip(*pack))
# # print(list(l1),"\n",list(l2))
# # max_num=[]
# # for pair in zip(l1,l2):
# #     max_num.append(max(pair))
# # print(max_num)
#
#
#
# # users=["user1","user2","user3","user4"]
# # first_name=["harika","deepak","anil"]
# # last_name=["golla","golla","golla"]
# # user_list=tuple(zip(users,first_name,last_name))
# # print(user_list)
# # user_list=dict(zip(users,first_name))
# # print(user_list)
#
#
# #iterator vs iteerable
# # l=[1,2,3,4,5,6,7]#list,tuple,set,....are iteerables
# # square=(map(lambda a:a**2,l))#iteator) and most important map,filter these are iteration only one time
# # for i in square:
# #     print(i)
# # for i in square:# giving only one time printing
# #     print(i)
#
# # print(next(iter(square)))
# # print(next(iter(square)))
# # print(next(iter(square)))
# # print(next(iter(square)))
#
# #EXERCISE
# # l1=[2,4,6,7,9]
# # l2=[4,5,6,4,5]
# # def averag(*args):
# #     avg=[]
# #     for pair in zip(*args):
# #         print(pair)
# #         avg.append(sum(pair)/len(pair))
# #     return avg
# # print(averag(l1,l2))
# #
# # average=lambda *args:[sum(pair)//len(pair) for pair in zip(*args)]
# # print(average(l1,l2,[4,8,9,7,4]))
#
#
# #min() and max() functions
# # l=[5,8,25,85,74,51,8,0.3,45]
# # print(min(l),max(l))
# # students=["hadfri","fjhgjar","deepak","df"]
# # print(min(students),max(students))
# # def func(item):
# #     return len(item)
# # print(max(students,key=func))
# # print(max(students,key=lambda item:len(item)))
# #
# # students={"harika":{"score":90,"age":24},
# #             "anil":{"score":100,"age":27},
# #              "deepak":{"score":95,"age":5}
# # }#dictionary inside dictionary
# # students1=[
# #             {"name":"harika","score":90,"age":24},
# #             {"name":"anil","score":100,"age":27},
# #             {"name":"deepak","score":95,"age":5}
# #
# # ]#dictionary inside list
# # print(min(students,key=lambda item:students[item]["score"]))
# # print(min(students1,key=lambda item:item.get("score"))["name"])
# # print(min(students1,key=lambda item:item.get("score")))
#
# #sort() and sorted()
# # fruits=["banana","orange","mango","apple","grapes"]
# # # print(sorted(fruits))
# # fruits.sort()
# # print(fruits)
# # fruits2=("banana","orange","mango","apple","grapes")
# # print(sorted(fruits2))
# #
# # guitars=[{"name":"piano","price":45200,"quality":"good"},
# #         {"name":"guitar","price":42000,"quality":"good"},
# #          {"name":"hamper","price":58200,"quality":"good"}
# #          ]
# # print(sorted(guitars,key=lambda item:item.get("price")))
# # print(guitars)
#
# # def sum(a,b):
# #     '''this function defines sum of two numbers'''
# #     return a+b
# # print(sum.__doc__)
# # print(len.__doc__)
# # print(max.__doc__)
# # print(min.__doc__)
# # print(sorted.__doc__)
# # print(help(sum))
# # print(help(len))
# #
# # l=[1,2,4,6,8,5]
# # def square(a):
# #     return a**2
# # # print(square(l))
# # print(list(map(lambda a:a**2,l)))#by using map function
# # square2=[a**2 for a in l]#by using list comprehension
# # print(square2)
# # def my_map(func,l):
# #     new_list=[]
# #     for i in l:
# #         new_list.append(func(i))
# #     return new_list
# # print(my_map(square,l))#by using own map function
#
# # def square(a):
# #     return a**2
# # s=square
# # print(s.__name__)
# # print(square.__name__)
#
# #function return function
# # def outer_func():
# #     def inner_func():
# #         print("this is inner func")
# #     return inner_func#or  return inner_func() we can call outer_func() directly
# # var=outer_func()
# # var()
#
# # def outer_func2():
# #     def inner_func2(msg):
# #         print(msg)
# #     return inner_func2
# # var=outer_func2()
# # var("hi this is me")
# #
# # def outer_func(msg):
# #     def inner_func():
# #         print(msg)
# #     return inner_func
# # var=outer_func("hello there!")
# # var()
# #
# # def power(x):
# #     def square(num):
# #         print(num**x)
# #     return square
# # square=power(2)
# # cube=power(3)
# # forth=power(4)
# # square(5),cube(7),forth(4)


# def main():
#   strings = ['Hello', 'World', 'Goodbye']
#   desired_concatenated_string = 'GoodbyeHello'
#   was_found = is_matching_concat_string_pair(strings,
#                                              desired_concatenated_string)
#   message = 'Given a list of strings {0}, the function checking whether the list contains a concatenated string \'{1}\' returned value: {2}\n'.format(
#       strings, desired_concatenated_string, was_found)
#   print(message)


# if __name__ == '__main__':
#   main()
def is_matching_concat_string_pair(string_list, desired_concatenated_string):
    for i in string_list:
        print(i[0])
#         for j in i:
#             if str(i)+str(j)==desired_concatenated_string:
#                 print("False")
#             elif str(j)+str(string_list[0])==desired_concatenated_string:
#                 print("True")
#             elif str(j)+str(string_list[0])==desired_concatenated_string or str(j)+str(string_list[1])==desired_concatenated_string:
#                 print("True")
# l1 = ["B", "C","A", "D"]
l2=["A","A","C","AC"]
is_matching_concat_string_pair(l2, "AAC")
#
#
