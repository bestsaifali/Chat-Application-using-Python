import socket
import sys
import time


s = socket.socket()
host = socket.gethostname()	
print("Server will start on host:-",host)
port = 1234  # Any port number you want to give
s.bind((host, port))
print()
print("Sever done binding to host and port successfully...")
print()
print("Sever is waiting for incoming connection..")
s.listen(1)
conn, addr = s.accept()      #connection and address
print(addr, "has connected to the sever and is now online.")
print()

while True:
	message = input(str("You:-"))
	message = message.encode()
	conn.send(message)

	incoming_message = conn.recv(1024)  #1024 byte
	incoming_message = incoming_message.decode()
	print("Client:- ", incoming_message)


