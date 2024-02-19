#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "ptl-c594a03c-4ebc1920.libcurl.so"
port = 80

# First establish the connection to the website
s.connect((host,port))

# Next send the appropriate headers for a HTTP request. Note, that every header is followed by \r\n to move to next line.
s.sendall(b'GET /pentesterlab HTTP/1.1\r\nHost: ptl-c594a03c-4ebc1920.libcurl.so\r\nConnection: close\r\n\r\n')
# The last header is closed with double \r\n or \r\n\r\n

# While there is data being received it receives and then exits. 
while True:
    
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())



