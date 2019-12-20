from django.test import TestCase
import requests
BaseUrl='http://127.0.0.1:8000/'
EndUrl='dir_js_sa'
resp=requests.get(BaseUrl+EndUrl)
print(resp.json())


