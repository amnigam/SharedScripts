#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a request to /pentesterlab/../pentesterlab

host = 'ptl-433f1733-7de88249.libcurl.so'
port = 80

headers = "GET /pentesterlab/../pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-433f1733-7de88249.libcurl.so\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

payload = bytes(headers,'utf-8')

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())

