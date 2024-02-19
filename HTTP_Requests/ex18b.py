#!/usr/bin/env python3

import requests

# In this challenge your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value please followed by a double-encoded NULL Byte

url = 'http://ptl-e3e9eb3c-d73e3a12.libcurl.so/pentesterlab'
enc = requests.utils.quote("please%00")     # Encode the null byte

req = requests.Request('GET',url=url)
prepared_req = req.prepare()

prepared_req.url += "?key=" + enc

s = requests.session()
resp = s.send(prepared_req)

print(resp.url)
print(resp.text)

