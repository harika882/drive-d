from django.db import models

class Travello(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    cost=models.IntegerField()
    offer=models.BooleanField(default=False)
    img=models.ImageField(upload_to='pics')


# Create your models here.
