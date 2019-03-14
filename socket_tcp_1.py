#!/usr/bin/python3


import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))

tcpSocket.listen(2)

(client, (ip, port)) = tcpSocket.accept()

data = "hello"
while(len(data)):
	data = client.recv(2048)
	print("Recived data: " + str(data))
	client.send(data)


