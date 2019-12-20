from django.db import models

class Dphotoes(models.Model):
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.img



# Create your models here.
