#!/usr/bin/env python3

import requests

url = 'http://ptl-8ce13360-f3de5382.libcurl.so/pentesterlab'
data = {}

r = requests.post(url,data=data)
print(r.text)
