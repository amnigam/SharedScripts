#!/usr/bin/env python3

import requests

url = 'http://ptl-051b79f1-ea43c084.libcurl.so/pentesterlab'

enc = requests.utils.quote("pretty please")     # URL encode the space

req = requests.Request('GET',url=url)
prepared_req = req.prepare()

prepared_req.url += "?key=" + enc

s = requests.session()
resp = s.send(prepared_req)
print(resp.url)
print(resp.text)

