from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to="Category",blank=True)

class Product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug = models.SlugField ( max_length=200, unique=True )
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to="product",blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


