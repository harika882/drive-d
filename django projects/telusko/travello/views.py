from django.shortcuts import render
from django.http import HttpResponse
from.models import Travello

def sample(request):
    return HttpResponse("This is Travello app")
def home(request):
    return render(request,'index.html')
def details(request):
    tv1=Travello()
    tv1.name="Mumbai"
    tv1.desc="The City is very cool and hot"
    tv1.cost=700
    tv2=Travello()
    tv2.name = "Bangalore"
    tv2.desc = "The City is very cool"
    tv2.cost = 800
    tv3 = Travello()
    tv3.name = "Goa"
    tv3.desc = "The City is very cool & Sweet"
    tv3.cost = 1000
    return render(request,'index.html',{'tv1':tv1,'tv2':tv2, 'tv3':tv3})

def practice(request):
    dests=Travello.objects.all()
    return render(request, 'practice.html',{'dests':dests})