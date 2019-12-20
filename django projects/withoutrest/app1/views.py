from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import Employee
from.serializers import EmployeeSerializers
# def sample(request):
#     data={'name':'Harika',
#           'gender':'female',
#           'address':'bangalore'}
#     resp=f"<h1>name:{data['name']}<br> gender:{data['gender']}<br> address:{data['address']}</h1>"
#     return HttpResponse(resp)
# import json
# def js_sample(request):
#     data = {'name': 'Harika',
#             'gender': 'female',
#             'address': 'bangalore'}
#     js_data=json.dumps(data)
#     return HttpResponse(js_data,content_type='application/json')
# from django.http import JsonResponse
# def dir_js_sa(request):
#     data = {'name': 'Harika',
#             'gender': 'female',
#             'address': 'bangalore'}
#     return JsonResponse(data)

class EmployeeView(APIView):
    def get(self,request):
        employee1=Employee.objects.all()
        serializer=EmployeeSerializers(employee1,many=True)
        return Response(serializer.data)
    def post(selfself):
        pass
