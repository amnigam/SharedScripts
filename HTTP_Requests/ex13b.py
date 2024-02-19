#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value please&
# Note, only the & portion needs to be URL encoded. 

url = 'http://ptl-070030b8-f0774836.libcurl.so/pentesterlab'
#url = 'http%3A%2F%2Fptl%2D070030b8%2Df0774836%2Elibcurl%2Eso%2F'       # Initially, I thought of URL encoding the whole URL. But it is not that way.

req = requests.Request('GET',url=url)
prepared_req = req.prepare()

#prepared_req.url += "?key=please&"
prepared_req.url += "?key=please%26"        # Note how we have URL encoded only &

# We can leverage requests.utils.quote method to convert our target string into URL encoded one. 
# If you want to use it then comment out above prepare_req.url line of code
#encoded = requests.utils.quote("please&")      # Un-comment this if you want to leverage requests.utils.quote
#prepared_req.url += "?key=" + encoded          # Un-comment this if you want to leverage requests.utils.quote

s = requests.session()
resp = s.send(prepared_req)
print(resp.url)

print(resp.text)
