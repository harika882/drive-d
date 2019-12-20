from django.conf.urls import url
from shop import views

urlpatterns=[url("index/",views.index),
             url("",views.allProdCat, name="allprodcat"),
             url('<slug:c_slug>/',views.allProdCat,name='products by category')]