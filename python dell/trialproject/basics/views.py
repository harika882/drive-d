from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from datetime import datetime
def wish_view(request):
    return HttpResponse("Hello, Good Morning!")
def first_view(request):
    return  render(request,"first.html",{})
def game_view(request):
    num=25
    guess_num=int(input("enter the number:"))
    if num==guess_num:
        msg=f"u won the game."
    else:
        msg=f"better luck next time."
    return render(request,"first.html",context={'msg':msg})
def image_view(request):
    date=datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        msg=f"hello guest very good morning."
    elif h<16:
        msg=f"hello guest good afteernoon."
    elif h<21:
        msg=f"hello guest very good evening."
    else:
        msg=f"hello guest good night."
    my_dict={'msg':msg,'date':date}
    response=render(request,"first.html",context=my_dict)
    return response
def fibbonacci_series(request):
    num=int(input("enteer the range of seies:"))
    first=0
    second=1
    for i in range(num):
        print(first)
        temp=first
        first=second
        second=first+temp

    return render(request,"first.html",context={"first":first})


# Create your views here.
