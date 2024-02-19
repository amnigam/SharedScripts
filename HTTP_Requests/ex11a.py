#!/usr/bin/env python3

import socket

host = 'ptl-9d54dbbb-487d3701.libcurl.so'
port = 80

body = b"key=please"
conLength = len(body)

headers = "POST /pentesterlab?key=please HTTP/1.1\r\n"
headers += "Host: ptl-9d54dbbb-487d3701.libcurl.so\r\n"
headers += "Content-Type: application/x-www-form-urlencoded\r\n"
headers += f"Content-Length: {conLength}\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

payload = bytes(headers,'utf-8')+body

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(payload)

while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())

