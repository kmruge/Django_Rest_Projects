import requests

endpoint = "http://127.0.0.1:8000/entry/2/"

response=requests.get(endpoint)
print(response)