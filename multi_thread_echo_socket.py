#!/usr/bin/python3

import thread
import socket

tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def socket_echo(client, client_data):
	data = client.recv(2048)
	print(str(client_data[0]) + " {"+ str(client_data[1]) + "}" + " : " + str(data))
	client.send(data)

tcpSock.bind(("0.0.0.0", 8000))

tcpSock.listen(3)

while True:
	(client, (ip, port)) = tcpSock.accept()
	thread.start_new_thread(socket_echo, (client, (ip, port)))



