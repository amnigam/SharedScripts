#!/usr/bin/env python3

import socket

host = 'ptl-9ded388f-2c156f80.libcurl.so'
port = 80

headers = "GET /pentesterlab?key=please&key=please HTTP/1.1\r\n"
headers += "Host: ptl-9ded388f-2c156f80.libcurl.so\r\n"
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
