#!/usr/bin/env python3

from requests import Request, Session

# In this challenge, we need to send a GET request containing POST data in it.
# This can be accomplished with SOCKET library and ex8a.py contains the code.

s = Session()

url = 'http://ptl-36a3f6c8-2a49d156.libcurl.so/pentesterlab'
data = {"key":"please"}
headers = {"Content-Type":"application/x-www-form-urlencoded", "Content-Length":"10"}

r = Request('GET',url,data=data,headers=headers)
prep = r.prepare()

resp = s.send(prep)

print(resp.text)

