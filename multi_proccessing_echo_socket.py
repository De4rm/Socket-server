import socket
import multiprocessing

tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSock.bind(("0.0.0.0", 8000))

def sock_conn(client, client_data):
	data = client.recv(2048)
	print(client_data[0] + " {" + str(client_data[1]) + "} :" + str(data))
	client.send(data)

tcpSock.listen(4)

while True:
	(client, client_data) = tcpSock.accept()
	p = multiprocessing.Process(target = sock_conn, args=(client, client_data))
	p.start()