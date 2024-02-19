#!/usr/bin/env python3

import requests

url = 'http://ptl-f0e8c20d-d5f4b8fd.libcurl.so/pentesterlab'
data = "<key value=\"please\"></key>"
conLen = len(data)
headers = {"Content-Type":"application/xml", "Content-Length":f"{conLen}"}

r = requests.post(url,headers=headers,data=data)
print(r.text)
