#!/usr/bin/env python3

import socket

host = 'ptl-8ce13360-f3de5382.libcurl.so'
port = 80

body = b''
conLength = len(body)

headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Content-Type: application/x-www-form-urlencoded\r\n"
headers += f"Content-Length: {conLength}\r\n"
headers += "Host: ptl-8ce13360-f3de5382.libcurl.so\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

payload = bytes(headers,'utf-8') + body

s.sendall(payload)

while True:
    data = s.recv(1024)

    if not data:
        break

    print(data.decode())
