#!/usr/bin/env python3

import socket

#In this challenge your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value please followed by a double-encoded NULL Byte

host = 'ptl-e3e9eb3c-d73e3a12.libcurl.so'
port = 80

headers = "GET /pentesterlab?key=please%2500 HTTP/1.1\r\n"
headers += "Host: ptl-e3e9eb3c-d73e3a12.libcurl.so\r\n"
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
