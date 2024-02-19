#!/usr/bin/env python3

import requests

url = 'http://ptl-859adb41-fc1d0cc1.libcurl.so/pentesterlab'
param = {"key":"please"}

r = requests.get(url,params=param)
print(r.text)
