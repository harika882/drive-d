from django.db import models
class Employee(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    emp_id=models.IntegerField()

    def __Str__(self):
        return self.first_name

# Create your models here.
