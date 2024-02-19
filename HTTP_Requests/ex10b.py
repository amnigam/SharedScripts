#!/usr/bin/env python3

import requests

# Challenge requires to send POST data with a key value of "key" repeating twice.
# This can be accomplished using a PREPARED REQUEST. However, Content-Type & Content-Length headers will need to be supplied with the request. Else it fails.

url = 'http://ptl-fd23a130-8b8f6b36.libcurl.so/pentesterlab'

body = "key=please&key=please"
conLength = len(body)
header = {"Content-Type":"application/x-www-form-urlencoded", "Content-Length":str(conLength)}

req = requests.Request('POST',url=url,headers=header)
prepared_req = req.prepare()

#print(prepared_req.url)
#print(prepared_req.body)

prepared_req.body = body            # Update the request's body with desired string.
print(prepared_req.body)

s = requests.session()

resp = s.send(prepared_req)
print(resp.text)
