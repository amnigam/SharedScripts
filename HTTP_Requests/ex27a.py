#!/usr/bin/env python3

import socket

# In this challenge, your goal is to send a GET request to /pentesterlab#pentesterlab.
# By default, curl will not send the fragment (everything after # included) and only send /pentesterlab.
# However, there is an option to prevent this behaviour (and it's different from the one used in http_25).
# This type of request is extremely useful when testing application with multiple layers of reverse proxies.

host = 'ptl-46d4d3ff-1b681f4e.libcurl.so'
port = 80

headers = "GET /pentesterlab#pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-46d4d3ff-1b681f4e.libcurl.so\r\n"
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


