#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following JSON: {"key": "[VALUE]"} with [VALUE] set to please". The request should also set the header Content-Type to application/json.

host = 'ptl-eaa872dd-c7434967.libcurl.so'
port = 80

body = "{\"key\":\"please\\\"\"}"
conLen = len(bytes(body,'utf-8'))

headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-eaa872dd-c7434967.libcurl.so\r\n"
headers += "Content-Type: application/json\r\n"
headers += f"Content-Length: {conLen}\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

payload = bytes(headers,'utf-8') + bytes(body,'utf-8')
print(payload.decode())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())
