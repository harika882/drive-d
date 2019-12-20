from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.template import loader

def time(request):
    time=datetime.datetime.now()
    s=f"The server run at the time is from votes, {str(time)}"
    return HttpResponse(s)
def good_morning(request):
    return HttpResponse("hi! very good morning from votes")
def good_afternoon(request):
    return HttpResponse("hi! very good afternoon from votes")
def good_night(request):
    return HttpResponse("hi! very good night from votes")
# def index(request):
#     template=loader.get_template('index.html')
#     return render(request,'index.html',{})

# Create your views here.


# Create your views here.
