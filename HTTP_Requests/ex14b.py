#!/usr/bin/env python3

import requests

url = 'http://ptl-0d5040f2-4a5329ea.libcurl.so/pentesterlab'

req = requests.Request('GET',url=url)
prepared_req = req.prepare()

enc = requests.utils.quote("?key")
prepared_req.url += "?"+enc + "=please"

print(prepared_req.url)

s = requests.session()

resp = s.send(prepared_req)
print(resp.url)
print(resp.text)

