import socket
import json
import threading
import Camera


class Client(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.camera = Camera.Camera()

    def send_data(self):
        print("Sending data")

        try:
            while True:
                camera_array = self.camera.encode_image()
                test = {"camera": camera_array, "sensors": [1, 2, 3]}

                self.sock.send(bytes(json.dumps(test), "utf-8"))
                self.sock.send(bytes("\n", "utf-8"))
        except ConnectionResetError:
            print("Connection lost")

    def receive(self):
        print("Awaiting message...")
        try:
            while True:
                message = self.sock.recv(4096)
                print(message)
        except ConnectionResetError:
            print("Connection lost")

    def receive_data(self):
        t = threading.Thread(target=self.receive)
        t.start()
        print("Started listening")


HOST = "localhost"  # Change to Raspberry accordingly
PORT = 8080

client = Client(HOST, PORT)
client.start()
client.receive_data()
client.send_data()
