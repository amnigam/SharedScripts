#!/usr/bin/env python3

import os
import socket
import binascii

# In this challenge, your goal is to send a request to /pentesterlab using HTTP multipart with a file (at least one byte in size) using the parameter name: filename.

host = 'ptl-e6ffac50-e6a3aef7.libcurl.so'
port = 80

boundary = binascii.hexlify(os.urandom(16)).decode('ascii')
binSendfile = open("test.txt","r")

body = f"--{boundary}\r\n"
body += "Content-Disposition: form-data; name=\"filename\"; filename=\"test.txt\"\r\n"
body += "\r\n"
body += f"{binSendfile.read()}\r\n"
body += f"--{boundary}--\r\n"

conLength = len(bytes(body,'utf-8'))

headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-e6ffac50-e6a3aef7.libcurl.so\r\n"
headers += f"Content-Type: multipart/form-data; boundary={boundary}\r\n"
headers += f"Content-Length: {conLength}\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

payload = bytes(headers,'utf-8')+bytes(body,'utf-8')
print(payload.decode())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())

