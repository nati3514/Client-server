import socket
c =socket.socket()

c.connect((socket.gethostname(), 1111))
name=input("Enter the client name:\n")
msg= c.recv(2048)
print("Message from server:\n",msg.decode())


