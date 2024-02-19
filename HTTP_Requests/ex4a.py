#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'ptl-9b5aaa21-3c530e74.libcurl.so'
port = 80

s.connect((host,port))

request = b"GET /pentesterlab HTTP/1.1\r\nHost: ptl-9b5aaa21-3c530e74.libcurl.so\r\nContent-Type: key/please\r\nConnection: close\r\n\r\n"
s.sendall(request)

while True:
    data = s.recv(1024)

    if not data:
        break

    print(data.decode())
