from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = "shortenersite"

urlpatterns = [
    url(r'^$', views.index, name='home'),
    # for our home/index page

    url(r"^(\w{6})$", views.redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL

    url(r'^makeshort/$', views.shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL

    path('url_list/', views.url_list, name="url_list"),
]