from django.conf.urls import url
from basics import views

urlpatterns=[
    url('wish/',views.wish_view),
    url('first/',views.first_view),
    url('game/',views.game_view),
    url("image/",views.image_view),
    url("fb",views.fibbonacci_series)
]