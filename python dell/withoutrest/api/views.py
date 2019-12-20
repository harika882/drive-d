from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
def emp_data(request):
    emp={'empno':100,
         'empname':'harika',
         'empsal':100000,
         'empaddress':'Bangalore'}
    resp='<h1>Employee Number:{}<br>Employee Name:{}' \
         '<br>Employee Salary:{}<br>Employee Adress:{}' \
         '</h1>'.format(emp['empno'],emp['empname'],emp['empsal'],emp['empaddress'])
    return HttpResponse(resp)
import json
def emp_data_json(request):
    emp={'empno':100,
         'empname':'harika',
         'empsal':100000,
         'empaddress':'Bangalore'}
    json_data=json.dumps(emp)
    return HttpResponse(json_data,content_type='application/json')

def emp_data_json1(request):
    emp={'empno':100,
         'empname':'harika',
         'empsal':100000,
         'empaddress':'Bangalore'}
    return JsonResponse(emp)

from django.views.generic import View
class Data(View):
    def get(self,request,*args,**kwargs):
        emp = {'empno' : 100,
               'empname' : 'harika',
               'empsal' : 100000,
               'empaddress' : 'Bangalore'}
        return JsonResponse(emp)
    def emp_data_json(request):
        emp={'empno':100,
         'empname':'harika',
         'empsal':1010000,
         'empaddress':'Bangalore'}
        json_data=json.dumps(emp)
        return HttpResponse(json_data,content_type='application/json')

    def emp_data_json1(request):
        emp={'empno':100,
         'empname':'harika',
         'empsal':100020,
         'empaddress':'Bangalore'}
        return JsonResponse(emp)

# Create your views here.
