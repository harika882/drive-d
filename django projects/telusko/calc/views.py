from django.shortcuts import render
from django.http import HttpResponse

def sample(request):
    return render(request,'home.html',{'name':'harika'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    sum=(val1)+(val2)
    subtract=val1-val2
    mul=val1*val2
    division=val1/val2
    return render(request,'result.html',{'result':sum,'subtract':subtract,'mul':mul,'division':division})
