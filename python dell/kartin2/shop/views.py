from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product


def index(request):
    return render(request,'index.html',{})


def allProdCat(request,c_slug=None):
    c_page=None
    products=None
    if c_slug is not None:
        cat=Category.objects.get(slug=c_slug)
        products=Product.objects.filter(category=cat,available=True)
        "load category and filter products by that category"
    else:
        products = Product.objects.filter (available=True )
        "load all products"
    return render(request,'category.html',{'Category':c_page,'products':products})



















# def detail(request,ques_id):
#     question=get_object_or_404(Question,pk=ques_id)
#     return render(request,'shop/category.html',{question:question})
#
# def votes(request,ques_id):
#     question=get_object_or_404(Question,pk=ques_id)
#     try:
#         choice_id=request.POST['choice']
#         selected_choice=question.choice_set.get(pk=choice_id)
#         expect(KeyError,Choice,DoesNotExist):
#         return render(request,)
#

# Create your views here.
