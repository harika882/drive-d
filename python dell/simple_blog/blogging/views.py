from django.shortcuts import render
from django.http import HttpResponse
from blogging.models import BlogArticle
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
    blogs=BlogArticle.objects.all()
    if request.method=='POST':
        username=request.POST["username"]
        pwd=request.POST["password"]
        user=authenticate(username=username,password=pwd)
        if user is not None:
            login(request,user)
            return render (request,"design.html",{'testvar':"test string!","blogs":"blogs",'user':user})

    return render(request,'design.html',{'testvar':"test string!","blogs":"blogs",'user':None})
    # return HttpResponse("Hello String!")
def createdialogue(request):
    firstlog=BlogArticle()
    firstlog.title=request.POST["title"]
    firstlog.author=request.user
    firstlog.blog_content=request.POST["blog_content"]
    firstlog.user()
    return render ( request, "design.html", {'testvar' : "test string!", "blogs" : "blogs", 'user' : user} )
