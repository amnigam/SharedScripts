#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a request with the header X-HTTP-Method-Override set to HACK to /pentesterlab.
# This challenge requires sending a CUSTOM HEADER in the request.

host = 'ptl-6732c5fb-91eaecf6.libcurl.so'
port = 80

headers = "GET /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-6732c5fb-91eaecf6.libcurl.so\r\n"
headers += "X-HTTP-Method-Override: HACK\r\n"
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
