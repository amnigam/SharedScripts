#!/usr/bin/env python3

import requests

cookie = {"key":"please"}

url = 'http://ptl-490ab3b2-65cba497.libcurl.so/pentesterlab'

r = requests.get(url,cookies=cookie)
print(r.text)
