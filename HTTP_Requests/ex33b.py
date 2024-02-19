#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following XML: <key><value>[VALUE]</value></key> where [VALUE] should be replaced with >please. The request should also set the header Content-Type to application/xml

url = 'http://ptl-1a0da154-a8aec67c.libcurl.so/pentesterlab'

header = {"Content-Type":"application/xml"}
data = "<key><value>>please</value></key>"

r = requests.post(url,headers=header,data=data)
print(r.text)
