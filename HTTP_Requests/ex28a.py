#!/usr/bin/env python3

import socket
import os
import binascii

# In this challenge, your goal is to send a request to /pentesterlab using HTTP multipart. 

host = 'ptl-f968be36-6030bc2a.libcurl.so'
port = 80

boundary = binascii.hexlify(os.urandom(16)).decode('ascii')         # The value for boundary in the header
binSendFile = open("test.txt","r")          # Open the file in read mode. Since we are encoding later we don't have to open in "rb" mode.

body = f"--{boundary}\r\n"          # This boundary was randomly generated earlier. 
body += "Content-Disposition: form-data; name=\"file\"; filename=\"test.txt\"\r\n"      # Escape Quotes
body += "\r\n"
body += f"{binSendFile.read()}\r\n"         # Send the file. Read the file object that was opened earlier.
body += f"--{boundary}--\r\n"

conLength = len(bytes(body,'utf-8'))

headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-f968be36-6030bc2a.libcurl.so\r\n"
headers += f"Content-Type: multipart/form-data; boundary={boundary}\r\n"
headers += f"Content-Length: {conLength}\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

payload = bytes(headers,'utf-8') + bytes(body,'utf-8')      # Encode the payload before sending it in request.
print(payload.decode())             # Print the HEADERS before sending the request

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())



