#!/usr/bin/env python3

import websockets
import asyncio

# In this challenge, your goal is to connect to the websocket /pentesterlab and send the string key.

url = 'ws://ptl-7003145b-ae3cda4f.libcurl.so/pentesterlab'      # The address of the target socket
data = "key"                    # Data to be sent in the socket
async def connect():
    async with websockets.connect(url) as websocket:
        await websocket.send(data)
        print(f">>> {data}")            # To simulate a prompt we are sending >>>

        resp = await websocket.recv()
        print(f"<<< {resp}")


asyncio.run(connect())

