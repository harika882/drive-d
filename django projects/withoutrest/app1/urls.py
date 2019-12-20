from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import views
urlpatterns=[
    # url(r'^api', views.sample),
    # url(r'^apijson', views.js_sample, name='js_sample'),
    # url('dir_js_sa', views.dir_js_sa, name='direct_by_json'),
    url(r'^employees/',views.EmployeeView.as_view())
]
