import socket
import sys
# create a socket
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input('Enter the server IP->')
port=9000
#connect to the server
clientsocket.connect((host,port))
#receive some data from the server
data=clientsocket.recv(2048)
print(data.decode('utf-8'))
#keep the connection alive
while True:
	message= input('->')
	clientsocket.send(str.encode(message))

clientsocket.close()


