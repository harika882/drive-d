from django.conf.urls import url
from travello import views
urlpatterns=[url("home",views.sample),
             url('index',views.home),
             url("dy_ch_de",views.details),
             url("pract",views.practice)]