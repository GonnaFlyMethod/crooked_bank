import socket
import config
import time

socket_ = socket.socket()
print("socket has been created")
socket_.connect((config.IP_OF_SERVER_TO_CONNECT, config.PORT_OF_SERVER_TO_CONNECT))

# Receiving data from server
print(socket_.recv(1024).decode())
