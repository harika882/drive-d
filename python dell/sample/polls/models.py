from django.db import models
from django.utils import timezone
import datetime
class Question(models.Model):
    qu_txt=models.TextField(max_length=200)
    pub_dt=models.DateTimeField('date published')
    def __str__(self):
        return self.qu_txt
    def was_published_recently(self):
        return self.pub_dt>=timezone.now()
datetime.timedelta(days=1)

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_txt=models.TextField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_txt

# Create your models here.
