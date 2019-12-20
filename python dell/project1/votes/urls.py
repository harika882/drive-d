from django.conf.urls import url
from votes import views


urlpatterns = [
    url('time/',views.time),
    url('morning',views.good_morning),
    url('afternoon',views.good_afternoon),
    url('night',views.good_night),
    # url('html',views.index)
    ]