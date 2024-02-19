#!/usr/bin/env python3

from requests import Request, Session

# Challenge requires to send a POST request with query string parameters as well as BODY
# This can only be accomplished through PREPARED REQUESTS

url = 'http://ptl-9d54dbbb-487d3701.libcurl.so/pentesterlab'
data = {"key":"please"}             # This is the body of POST request
query = "?key=please"               # This is the query string portion for GET request

#header = {"Content-Type":"application/x-www-form-urlencoded", "Content-Length":"10"}       # We don't need to send HEADER since our POST request is valid! 
#req = Request('POST',url=url,data=data,headers=header)                                     # We can drop headers

req = Request('POST',url=url,data=data) 
prepared_req = req.prepare()

prepared_req.url += query           # Append query string to URL
s = Session()

resp = s.send(prepared_req)
print(resp.text)
