#!/usr/bin/python3
import requests


res = requests("https://www.w3schools.com/python/module_requests.asp")

print(res.content)
print("Hello")
