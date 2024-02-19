#!/usr/bin/env python3

import requests

# Challenge requires to send a query parameter twice. This is not possible with normal REQUESTS
# We need to send a PREPARED REQUEST with custom query string parameters

url = 'http://ptl-9ded388f-2c156f80.libcurl.so/pentesterlab'
#param = {"key":"please","key":"please"}    # I tried to pass this into params=param portion of creating request but it still takes the query string only once!

req = requests.Request('GET',url=url)
prepared_req = req.prepare()
prepared_req.url += "?key=please&key=please"        # Modifying the URL with necessary query string values. 

print(prepared_req.headers)                         # One can access the headers, body and url properties of the prepared request by using . operator 
print(prepared_req.url)

s =requests.session()                               # For prepared request you need to setup a Session
resp = s.send(prepared_req)
print(resp.text)

#r = requests.get(url,params=param)
#print(r.text)
#print(r.request.headers)
#print(r.request.url)
#print(r.request.body)
