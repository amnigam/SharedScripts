#!/usr/bin/env python3

import requests

url = 'http://ptl-0994ac6c-c291be06.libcurl.so/pentesterlab'
header = {"Accept-Language":"key-please"}

r = requests.get(url,headers=header)
print(r.text)


