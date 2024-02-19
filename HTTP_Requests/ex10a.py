#!/usr/bin/env python3

import socket

host = 'ptl-fd23a130-8b8f6b36.libcurl.so'
port = 80

body = b'key=please&key=please'
conLength = len(body)

headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Content-Type: application/x-www-form-urlencoded\r\n"
headers += f"Content-Length: {conLength}\r\n"
headers += "Host: ptl-fd23a130-8b8f6b36.libcurl.so\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

payload = bytes(headers,'utf=8') + body

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(payload)

while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())
