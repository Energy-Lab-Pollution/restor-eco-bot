"""
Script that contains the code to scrape the Restor-Eco page
"""

import requests

from util.constants import API, HEADERS


api = API.replace("x", "1").replace("y", "30")
path = api.split("/")
path = path


print(api)
print(path)
r = requests.post(api, headers=HEADERS)
print(r.content)
