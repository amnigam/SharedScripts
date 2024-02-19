#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a request with the header X-Forwarded-Host set to pentesterlab.com to /pentesterlab

host = 'ptl-f3928b1a-57943158.libcurl.so'
port = 80

headers = "GET /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-f3928b1a-57943158.libcurl.so\r\n"
headers += "X-Forwarded-Host: pentesterlab.com\r\n"
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

