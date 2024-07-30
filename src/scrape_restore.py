"""
Script that contains the code to scrape the Restor-Eco page
"""

import requests

from util.constants import API, HEADERS


api = API.replace("x", "1").replace("y", "30")
path = api.split("/")
path = path[3:]
path = "/".join(path)

headers = HEADERS.copy()
headers["path"] = path

print(api)
print(path)
r = requests.get(api, headers=headers)
# print(r.content)
