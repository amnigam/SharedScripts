#!/usr/bin/env python3

import socket

# In this challenge your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value please followed by a NULL Byte

host = 'ptl-a4c50e24-cbdba572.libcurl.so'
port = 80

headers = "GET /pentesterlab?key=please%00 HTTP/1.1\r\n"
headers += "Host: ptl-a4c50e24-cbdba572.libcurl.so\r\n"
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
