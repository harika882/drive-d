from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.
# def index(request):
#     return HttpResponse("hi this is ecommerce project")

def catalog(request):
    if 'cart' not in request.session:
        request.session['cart']=[]
    cart=request.session['cart']
    request.session.set_expiry(0)
    store_items=Product.objects.all()
    ctx={'store_items':store_items,'cart_items':len(cart)}
    return render(request,'catalog.html',ctx)