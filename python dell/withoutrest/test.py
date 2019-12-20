import requests
Base_url="http://127.0.0.1:8000/"
end_url="apijson"
r=requests.get(Base_url+end_url)
print(r.json())
