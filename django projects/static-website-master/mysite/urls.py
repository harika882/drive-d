
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^pages/',include('pages.urls')),

]
