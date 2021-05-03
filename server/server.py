import socket
import config

socket_ = socket.socket()
print("socket has been created")

socket_.bind((config.IP, config.PORT))

# listening to config.LISTEN_CONNECTIONS_NUM connections,
# If there are connections greater then config.LISTEN_CONNECTIONS_NUM then
# thouse connections will be refused
socket_.listen(config.LISTEN_CONNECTIONS_NUM)
print(f"Connections in the same time: {config.LISTEN_CONNECTIONS_NUM}")


# Main server loop
while True:
	# Accepting connection from a client
	client, client_address = socket_.accept()

	print(f"The connection with {client_address} has been established")	
	client.send(bytes("Hello from server!", 'utf-8'))
	
	# Close connection with the client
	client.close()
