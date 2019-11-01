# -*- coding: utf-8 -*-
import socket
import socketserver
import threading
import asyncio
import websockets

class MySelfServer(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            self.data = self.request.recv(655300).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)

            if not self.data:
                print(self.client_address, '的链接断开了！')
                break

            asyncio.get_event_loop().run_until_complete(ws_client('ws://192.168.110.120/11.ashx', self.data))
            #self.request.sendall(self.data.upper())

    async def ws_client(self, url, send_data):
        async with websockets.connect(url) as ws:
            await ws.send(data)
            resp_data = await ws.recv()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MySelfServer)

    server.serve_forever()