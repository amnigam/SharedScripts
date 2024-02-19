#!/usr/bin/env python3

import requests

url = 'http://ptl-8812fd89-84d14223.libcurl.so/pentesterlab'
data = {"key":"please"}

r =requests.post(url,data=data)
print(r.text)

