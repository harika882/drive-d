from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BlogArticle(models.Model):
    title=models.CharField(max_length=200)
    blog_content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
