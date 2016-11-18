import websocket

class Snakesock:
    def __init__(self):
        self.ws = websocket.WebSocket()

    def connect(self, host="localhost", port=8080, venue="training"):
        self.ws.connect("ws://{}:{}/{}".format(host, port, venue))

    def send(self, msg):
        self.ws.send(msg)

    def recv(self, max_length=2048): #NOTE: Arbitrary number
        msg = self.ws.recv()
        return msg

    def close(self):
        self.ws.close()

    def connected(self):
        return self.ws.connected
