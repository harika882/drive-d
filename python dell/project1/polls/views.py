from django.shortcuts import render,get_object_or_404
from datetime import datetime
from django.shortcuts import render
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.urls import reverse

#
# def time(request):
#     time=datetime.datetime.now()
#     s=f"The server run at the time is, {str(time)}"
#     return HttpResponse(s)
# def good_morning(request):
#     return HttpResponse("hi! very good morning")
# def good_afternoon(request):
#     return HttpResponse("hi! very good afternoon")
# def good_night(request):
#     return HttpResponse("hi! very good night")
# # def index(request):
# #     template=loader.get_template('index.html')
# #     return render(request,'index.html',{})
# def template_view(request):
#     time=datetime.datetime.now()
#     hour=int(time.strftime('%H'))
#     wish="hello! welcome !!!very Good"
#     if hour<12:
#         msg=wish+'morning'
#     elif hour>12 and hour<16:
#         msg=wish+'afternoon'
#     elif hour<21:
#         msg=wish+'Evening'
#     else:
#         msg=wish+'night'
#     response=render(request,'index.html',{'msg':msg,'date':time})
#     return response
# class IndexView(TemplateView):
#     template_name="index.html"
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]

    context={'latest_question_list':latest_question_list,}
    return render(request,'index.html',context)


    # return render(request,'index.html')

# Create your views here.
