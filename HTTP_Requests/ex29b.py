#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a request to /pentesterlab using HTTP multipart with a file (at least one byte in size) using the parameter name: filename.
# This is pretty much the same as previous challenge. 
# I haven't used prepared requests to view the HEADERS but you can if you want to. 

url = 'http://ptl-e6ffac50-e6a3aef7.libcurl.so/pentesterlab'
files = {"filename":open("test.txt","rb")}

#r = requests.post(url,files=files)
#print(r.text)

req = requests.Request('POST',url,files=files)
prepared_req = req.prepare()

print(prepared_req.url)
print(prepared_req.headers)
print(prepared_req.body.decode())

s = requests.session()
resp = s.send(prepared_req)
print(resp.text)
