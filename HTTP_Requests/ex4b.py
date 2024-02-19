#!/usr/bin/env python3

import requests

url = 'http://ptl-9b5aaa21-3c530e74.libcurl.so/pentesterlab'

header = {"Content-Type": "key/please"}

r =requests.get(url,headers=header)
print(r.text)
