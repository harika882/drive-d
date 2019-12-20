from django.conf.urls import url
from blogging import views
urlpatterns=[url("",views.index),
             url("addblog",views.createdialogue)]