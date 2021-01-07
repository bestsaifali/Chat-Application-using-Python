import socket
import sys
import time


s = socket.socket()
host = input(str("Kindly enter the hostname of the server:-"))
port = 1234
try:
	s.connect((host, port))
	print("Connected to chat server..")
except:
	print("Connection failed with server..")
while True:
	incoming_message = s.recv(1024)  #1024 byte
	incoming_message = incoming_message.decode()
	print("Server:- ", incoming_message)

	message = input(str("You:-"))
	message = message.encode()
	s.send(message)