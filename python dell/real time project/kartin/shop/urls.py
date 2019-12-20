from django.conf.urls import url
from shop import views

urlpatterns=[url("msg/",views.show_mesage),
             url("temp/",views.template_view),
             url("fb/",views.fb_view)]