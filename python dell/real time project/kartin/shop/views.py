from django.shortcuts import render
from django.http import HttpResponse

def show_mesage(request):
    return HttpResponse("hi good morning!")
def template_view(request):
   return render(request,"pract.html",{})
def fb_view(request):
    return render(request,"fb.html",{})

