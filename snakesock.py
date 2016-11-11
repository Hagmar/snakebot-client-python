import socket
import json

class Snakesock:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host="localhost", port=8080):
        self.sock.connect((host, port))

    def sent(self, msg):
        sent = self.sock.send(msg)
        if sent == 0:
            raise Exception

    def recv(self, max_length):
        msg = self.sock.recv(2048) #NOTE: Arbitrary number
        if msg == b'':
            raise Exception("socket connection broken")
        return msg
