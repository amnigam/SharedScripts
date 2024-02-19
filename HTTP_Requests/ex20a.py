#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key as a hash/dictionary with the key please set to 1

host = 'ptl-24a41ea4-6c994820.libcurl.so'
port = 80

headers = "GET /pentesterlab?key[please]=1 HTTP/1.1\r\n"
headers += "Host: ptl-24a41ea4-6c994820.libcurl.so\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))

payload = bytes(headers,'utf-8')

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())
