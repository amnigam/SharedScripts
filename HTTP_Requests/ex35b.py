#!/usr/bin/env python3

import requests

url = 'http://ptl-15423def-8fd08cb0.libcurl.so/pentesterlab'
data = "<key><value>&lt;&amp;please&gt;</value></key>"
conLen = len(bytes(data,'utf-8'))
header = {"Content-Type":"application/xml", "Content-Length":f"{conLen}"}

r = requests.post(url,headers=header,data=data)
print(r.text)
