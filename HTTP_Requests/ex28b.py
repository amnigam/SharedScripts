#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a request to /pentesterlab using HTTP multipart. 
# A multipart request essentially means that we are sending some kind of attachment. Hence, you need to provide a file. 
# Once you create a request with a file to be uploaded (files dictionary) the requests module automatically creates a multipart request
# This assignment can be concluded with REQUESTS module alone. However, because I wanted to look at the headers I have created a prepared request as well. 

files = {"file":open("test.txt","rb")}
url = 'http://ptl-f968be36-6030bc2a.libcurl.so/pentesterlab'

# r = requests.post(url,files=files)        # This is sufficient to conclude the challenge
# print(r.text)                             

req = requests.Request('POST',url,files=files)
prepared_req = req.prepare()

print(prepared_req.url)
print(prepared_req.headers)
print(prepared_req.body.decode())       # We are decoding because the body is encoded in bytes.

s = requests.session()
resp = s.send(prepared_req)

print(resp.text)
