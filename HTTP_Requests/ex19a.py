#!/usr/bin/env python3

import socket

# Send a GET request to /pentesterlab with the following GET parameter: key as an array with the first element with the value key and the second element with the value please

host = 'ptl-7a295c2b-541712f9.libcurl.so'
port = 80

headers = "GET /pentesterlab?key[0]=key&key[1]=please HTTP/1.1\r\n"
headers += "Host: ptl-7a295c2b-541712f9.libcurl.so\r\n"
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


