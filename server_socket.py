import socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind the socket to a public host and a known port
#gethostname() allows the socket to be visible to the outside world
try:
	serversocket.bind((socket.gethostname(),6000))
except socket.error as e:
	print(str(e))	
#become a server socket, since the server has to listen to requests
serversocket.listen(5)

while True:
	conn,addr=serversocket.accept()

print('connected to:' + addr[0] + str(addr[1]))