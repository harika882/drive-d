from django.shortcuts import render
from django.http import HttpResponse

posts=[{
    'author':'jamesanys',
    'title':'killbill',
    'posted_date':'17 oct,2000',
    'content':'first content'
        },
        {
    'author':'thomus',
    'title':'no country for oldman',
    'posted_date':'17 july,1900',
    'content':'second content'
        }
]

def home(request):
    context={'posts':posts}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})

# Create your views here.
