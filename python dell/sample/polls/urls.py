from django.conf.urls import url
from polls import views

urlpatterns=[url("indx",views.index),
             url("tmplte/",views.template),
             url("rest",views.rest_api_view),
             url("json",views.json_view)]