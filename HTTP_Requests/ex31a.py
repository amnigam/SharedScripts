#!/usr/bin/env python3

import socket 

# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing: <key><value>please</value></key>.
# Note, the value being sent in the body is an XML. You can also try this with multi-part stuff and have an XML file being sent over.

host ='ptl-323be71a-1763ac74.libcurl.so'
port = 80

body = "<key><value>please</value></key>"
conLen = len(bytes(body,'utf-8'))

headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-323be71a-1763ac74.libcurl.so\r\n"
headers += "Content-Type: application/x-www-form-urlencoded\r\n"
headers += f"Content-Length: {conLen}\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

payload = bytes(headers,'utf-8') + bytes(body,'utf-8')
print(payload.decode())

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())
