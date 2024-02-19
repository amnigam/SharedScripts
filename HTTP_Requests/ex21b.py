#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a request with the method HACK to /pentesterlab
# We are sending a "Custom HTTP Verb" as part of the prepared request to solve this challenge

url = 'http://ptl-ecda8634-ff04dccb.libcurl.so/pentesterlab'

req = requests.Request('HACK',url=url)      # Defining the CUSTOM HTTP Verb (HACK)
prepared_req = req.prepare()
print(prepared_req.headers)

s = requests.session()
resp = s.send(prepared_req)

print(resp.text)
