#!/usr/bin/env python3

import requests

url = 'http://ptl-f36f992d-62e1c026.libcurl.so/pentesterlab'
files = {"filename":open("../test.txt","rb")}

req = requests.Request('POST',url,files=files)
prepared_req = req.prepare()

print(prepared_req.url)
print(prepared_req.headers)
print(prepared_req.body.decode())

s = requests.session()
resp = s.send(prepared_req)
print(resp.text)

