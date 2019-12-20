from django.shortcuts import render
from.models import Dphotoes
from django.http import HttpResponse
def brs(request):
    photos=Dphotoes.objects.all()
    return render(request,'media1.html',{'photos':photos})



# Create your views here.
