from django.db import models


# Create your models here.
class Product(models.Model):
    Name=models.CharField(max_length=800)
    price=models.FloatField()
    description=models.TextField(max_length=800)
    imglink=models.ImageField(upload_to='Product',blank=True)
class Order(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=400)
    payment_mode=models.CharField(max_length=400)
    payment_data=models.CharField(max_length=200)
    items=models.TextField()
    fulfilled=models.BooleanField()