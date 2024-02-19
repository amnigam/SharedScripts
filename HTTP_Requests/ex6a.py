#!/usr/bin/env python3

import socket

host = 'ptl-8812fd89-84d14223.libcurl.so'
port = 80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

body = b'key=please'
conLength = len(body)   # Compute the length of the body that needs to be provided in the header

# Making a POST request
headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Content-Type: application/x-www-form-urlencoded\r\n"    #Content-Type has to be provided in a PUT or POST request. 
headers += f"Content-Length: {conLength}\r\n"
headers += "Host: ptl-8812fd89-84d14223.libcurl.so\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

print(b"Headers -->" +bytes(headers,'utf-8'))

payload = bytes(headers,'utf-8') + body
print(b"Final Payload -->" +payload)
s.sendall(payload)

while True:
    data = s.recv(1024)

    if not data:
        break

    print(data.decode())


#Note: 2 headers are critical for sending POST request. 1. Content-Type and 2. Content-Length
#Note: I spent a lot of time not being able to send a POST request cos the content-type was wrong. Always check for these values!
