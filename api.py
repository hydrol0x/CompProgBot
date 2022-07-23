#!/usr/bin/env python
import requests

url = "https://clist.by:443/api/v2/contest/"
headers = {
    "Authorization": "ApiKey hydrolox:5878cb1a42f5f4adf14b899fa25c88e4f4e4be93"}

response = requests.get(url, headers=headers, params="?format=json")
print(response.content)
