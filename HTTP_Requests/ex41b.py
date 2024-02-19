#!/usr/bin/env python3

import requests

# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following YAML: key as an array with two values: please and please2. The request should also set the header Content-Type to application/yaml.

url = 'http://ptl-49823e0b-cb6e7944.libcurl.so/pentesterlab'
body = "key: [please, please2]"
conLen = len(body)

header = {"Content-Type":"application/yaml", "Content-Length":f"{conLen}"}

r = requests.post(url,headers=header,data=body)
print(r.text)
