#!/usr/bin/env python3

import requests

url = 'http://ptl-a7705a3f-08dccdb6.libcurl.so/pentesterlab'
header = {"X-Forwarded-For":"1.2.3.4"}

r = requests.get(url,headers=header)
print(r.text)
