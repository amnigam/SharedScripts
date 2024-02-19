#!/usr/bin/env python3

import requests

url = 'http://ptl-f3928b1a-57943158.libcurl.so/pentesterlab'
header = {"X-Forwarded-Host":"pentesterlab.com"}

req = requests.Request('GET',url,headers=header)
prepared_req = req.prepare()

s = requests.session()

print(prepared_req.headers)

res = s.send(prepared_req)
print(res.text)
