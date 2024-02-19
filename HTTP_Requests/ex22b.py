#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a request with the header X-HTTP-Method-Override set to HACK to /pentesterlab
# This challenge can be solved with simple requests without needing prepared requests. However, in case if you wish to see the headers being sent with your request you 
# will need to use prepared requests. I am using Prepared Requests just to confirm whether my header is present or not. 

url = 'http://ptl-6732c5fb-91eaecf6.libcurl.so/pentesterlab'
header = {"X-HTTP-Method-Override":"HACK"}

req = requests.Request('GET',url=url,headers=header)
prepared_req = req.prepare()

# The following line will print the HEADERS for the prepared request
print(prepared_req.headers)

s = requests.session()

r = s.send(prepared_req)
print(r.text)
