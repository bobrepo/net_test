import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sd:
    sd.connect(("localhost", 8000))

    sd.send(b"hello world")
