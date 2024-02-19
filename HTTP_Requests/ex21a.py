#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a request with the method HACK to /pentesterlab

host = 'ptl-ecda8634-ff04dccb.libcurl.so'
port = 80

headers = "HACK /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-ecda8634-ff04dccb.libcurl.so\r\n"
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
