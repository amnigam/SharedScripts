#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following JSON: {"key": "[VALUE]"} with [VALUE] set to please". The request should also set the header Content-Type to application/json.

url = 'http://ptl-eaa872dd-c7434967.libcurl.so/pentesterlab'
body = {"key": "please\""}          # Inside a JSON you can escape " with \" 
conLen = len(body)
headers = {"Content-Type":"application/json", "Content-Length":f"{conLen}"}

req = requests.Request('POST', url, headers=headers, json=body)
prepared_req = req.prepare()

print(prepared_req.url)
print(prepared_req.headers)
print(prepared_req.body)

s = requests.session()
resp = s.send(prepared_req)

print(resp.text)
