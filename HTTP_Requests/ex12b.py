#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value =please

url = 'http://ptl-8ad1324b-f461c4a6.libcurl.so/pentesterlab'

req = requests.Request('GET',url=url)
prepared_req = req.prepare()

prepared_req.url += "?key==please"
s = requests.session()

res = s.send(prepared_req)
print(res.text)
