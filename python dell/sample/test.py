import requests
Base_url='http://127.0.0.1:8000/sample/polls'
End_point='json'
resp=requests.get(Base_url+End_point)
print(resp.json())
