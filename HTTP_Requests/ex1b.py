#!/usr/bin/env python3

# This is attempting the same exercise with REQUESTS module

import requests

url = 'http://ptl-c594a03c-4ebc1920.libcurl.so/pentesterlab'

r =requests.get(url)
print(r.text)
