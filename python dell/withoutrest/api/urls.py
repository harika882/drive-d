from django.conf.urls import url
from api import views
urlpatterns=[url("@ed",views.emp_data),
             url("@jd",views.emp_data_json),
             url ( "@jd1", views.emp_data_json1),
             url("@cjd",views.Data.as_view())]