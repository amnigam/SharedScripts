#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth

# In this challenge, your goal is to send a GET request to /pentesterlab with an authentication Basic with the username key and the password please.

url = 'http://ptl-35f3c11e-f38b63e1.libcurl.so/pentesterlab'

req = requests.Request('GET',url,auth=HTTPBasicAuth('key','please'))
prepared_req = req.prepare()

print(prepared_req.url)
print(prepared_req.headers)

s = requests.session()
resp = s.send(prepared_req)

print(resp.text)


