#!/usr/bin/env python3

import socket

host = 'ptl-490ab3b2-65cba497.libcurl.so'
port = 80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

request = b"GET /pentesterlab HTTP/1.1\r\nHost: ptl-490ab3b2-65cba497.libcurl.so\r\nAccept: text/html\r\nCookie: key=please\r\nConnection: close\r\n\r\n"
s.sendall(request)

while True:
    data = s.recv(1024)

    if not data:
        break

    print(data.decode())
