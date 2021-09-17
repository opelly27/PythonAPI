import requests


base = "http://127.0.0.1:5000/"

r = requests.get(base + "helloworld")

print(r.json())