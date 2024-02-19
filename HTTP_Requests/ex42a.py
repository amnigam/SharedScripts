#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a GET request to /pentesterlab with an authentication Basic with the username key and the password please.

host = 'ptl-35f3c11e-f38b63e1.libcurl.so'
port = 80

headers = "GET /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-35f3c11e-f38b63e1.libcurl.so\r\n"
headers += "Authorization: Basic a2V5OnBsZWFzZQ==\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

payload = bytes(headers,'utf-8')
print(payload.decode())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())

