#!/usr/bin/env python3

import requests
# In this challenge, send a POST request to /pentesterlab with the body of the request containing the following XML: <key value="[VALUE]"></key> with [VALUE] set to "please. The request should also set the header Content-Type to application/xml.

url = 'http://ptl-c12c70af-e9361f42.libcurl.so/pentesterlab'
body = "<key value=\"&quot;please\"></key>"     # Escape first quote and then HTML encode the quote for it to be interpreted at server
conLen = len(body)
headers = {"Content-Type":"application/xml", "Content-Length":f"{conLen}"}

r = requests.post(url, headers=headers, data=body)
print(r.text)
