from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
def index(request):
    return HttpResponse("good morning")

def template(request):
    return render(request,'sample.html',{})

def rest_api_view(request):
    emp_data={"empname":"niharika",
                      "empno":251,
                "empadd":"hyderabad"}
    # resp=f"<h1>employee name:{emp_data['empname']}<br>employee num:{emp_data['empno']}<br>employee adress:{emp_data['empadd']}</h1>"
    # json_data=json.dumps(emp_data)
    # return HttpResponse(json_data,content_type='application/json')
    return HttpResponse(f"<h1>employee name:{emp_data['empname']}<br>employee num:{emp_data['empno']}<br>employee adress:{emp_data['empadd']}</h1>")
def json_view(request):
    emp_data = {"empname" : "niharika",
                "empno" : 251,
                "empadd" : "hyderabad"}
    return JsonResponse(emp_data)