#!/usr/bin/env python3

import requests

url = 'http://ptl-d51a6bb5-f6c3cf02.libcurl.so/pentesterlab'

req = requests.Request("GET",url=url)
prepared_req = req.prepare()

enc = requests.utils.quote("please#")
prepared_req.url += "?key=" + enc

s = requests.session()
resp = s.send(prepared_req)
print(resp.url)
print(resp.text)
