#!/usr/bin/env python3

import requests

url = 'http://ptl-46d4d3ff-1b681f4e.libcurl.so/'

req = requests.Request('GET',url)
prepared_req = req.prepare()

enc = requests.utils.quote('#pentesterlab')

prepared_req.url += "pentesterlab" + enc
print(prepared_req.url)

s = requests.session()
resp = s.send(prepared_req)
print(resp.text)

