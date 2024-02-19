#!/usr/bin/env python3

import requests

url = 'http://ptl-822fd027-be476a53.libcurl.so/pentesterlab'
header = {"Content-Type":"application/xml"}
data = "<key><value>please</value></key>"

r = requests.post(url,headers=header,data=data)
print(r.text)
