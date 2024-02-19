#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following XML: <key><value>[VALUE]</value></key> where [VALUE] should be replaced with <please>. The request should also set the header Content-Type to application/xml.

url = 'http://ptl-9d8e5f63-d07e17fc.libcurl.so/pentesterlab'

#data = "<key><value><please></value></key>"        # Sending out this data in body will result in "Error parsing reques"
data = "<key><value>&lt;please&gt;</value></key>"   # Need to encode the data. Else it waits for corresponding tag since our content type is application xml.

conLen = len(data)
header = {"Content-Type":"application/xml", "Content-Length":f"{conLen}"}

req = requests.Request('POST',url,headers=header)
prepared_req = req.prepare()

prepared_req.body = data
print(prepared_req.url)
print(prepared_req.headers)
print(prepared_req.body)

s = requests.session()
resp = s.send(prepared_req)
print(resp.text)

