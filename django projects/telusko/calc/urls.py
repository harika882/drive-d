from django.conf.urls import url
from calc import views
urlpatterns=[url("home",views.sample),
             url("add",views.add)]