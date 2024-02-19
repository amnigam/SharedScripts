#!/usr/bin/env python3

import requests

url ='http://ptl-323be71a-1763ac74.libcurl.so/pentesterlab'
data = "<key><value>please</value></key>"

# This challenge can be done with simple requests. However, using prepared requests to see what HEADERS are bing sent. 

#r = requests.post(url,data=data)
#print(r.text)

req = requests.Request('POST', url=url, data=data)
prepared_req = req.prepare()

print(prepared_req.url)
print(prepared_req.headers)
print(prepared_req.body)

s = requests.session()
resp = s.send(prepared_req)

print(resp.text)
