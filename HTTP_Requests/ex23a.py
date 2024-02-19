#!/usr/bin/env python3

import socket

# n this challenge, your goal is to send a request with the header X-Forwarded-For set to 1.2.3.4 to /pentesterlab

host = 'ptl-a7705a3f-08dccdb6.libcurl.so'
port = 80

headers = "GET /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-a7705a3f-08dccdb6.libcurl.so\r\n"
headers += "X-Forwarded-For: 1.2.3.4\r\n"
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

