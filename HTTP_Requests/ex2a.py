#!/usr/bin/env python3

import socket

host = 'ptl-859adb41-fc1d0cc1.libcurl.so'
port = 80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
s.sendall(b'GET /pentesterlab?key=please HTTP/1.1\r\nHost: ptl-859adb41-fc1d0cc1.libcurl.so\r\nAccept: text/html\r\nConnection: close\r\n\r\n')

while True:
    data = s.recv(1024)

    if not data:
        break

    print(data.decode())
