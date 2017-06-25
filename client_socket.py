import socket
clientsocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Enter the server IP\n")
host=input()
port=6000
clientsocket.connect((host,port))

