import requests
import json

BASE = 'http://127.0.0.1:5000'

response =  requests.delete(BASE + "/video/6")

input()

response_2 =  requests.put(BASE + "/video/6", {'id': 6, 'name': 'test', 'views': 666, 'likes': 12345 }).json()
print(response_2)

input()

response_2 =  requests.get(BASE + "/video/6").json()
print(response_2)

input()

response_2 =  requests.patch(BASE + "/video/6", {'likes': 666})

input()

response_2 =  requests.get(BASE + "/video/6").json()
print(response_2)

input()

response =  requests.delete(BASE + "/video/6")

input()

response_2 =  requests.get(BASE + "/video/6").json()
print(response_2)