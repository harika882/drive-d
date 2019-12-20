from django.conf.urls import url
from polls import views


urlpatterns = [
    # url('time/',views.time),
    # url('morning',views.good_morning),
    # url('afternoon',views.good_afternoon),
    # url('night',views.good_night),
    # url('html',views.template_view)
    url('',views.index,name='index'),
    # url('ques/<int:ques_id>/',views.detail,name='detail'),
    # url ( 'vote/<int:ques_id>/', views.detail, name='detail' ),
    # url ( 'ques/<int:ques_id>/', views.detail, name='detail' ),

    # url('html',views.index)
    ]