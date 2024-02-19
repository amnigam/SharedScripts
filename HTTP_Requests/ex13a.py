#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value please&
# Note that we can send the exact character & in our request but it will not work since the server expects a URL encoded version of & or else it confuses it with another
# parameter that should be part of query string following &

# Hence, we need to send a normal request but only URL encode '&' which is %26

host = 'ptl-070030b8-f0774836.libcurl.so'
port = 80

headers = "GET /pentesterlab?key=please%26 HTTP/1.1\r\n"        # Notice, how & has been url encoded to %26
headers += "Host: ptl-070030b8-f0774836.libcurl.so\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

payload = bytes(headers,'utf-8')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())
