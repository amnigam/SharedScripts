#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following YAML: key: please. The request should also set the header Content-Type to application/yaml.

url = 'http://ptl-5b04c57d-237d61fd.libcurl.so/pentesterlab'
body = "key: please"
conLen = len(body)
headers = {"Content-Type":"application/yaml", "Content-Length":f"{conLen}"}

req = requests.Request('POST', url, headers=headers, data=body)
prepared_req = req.prepare()

print(prepared_req.url)
print(prepared_req.headers)
print(prepared_req.body)

s = requests.session()
resp = s.send(prepared_req)

print(resp.text)
