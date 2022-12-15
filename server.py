import socket
s =socket.socket()

s.bind((socket.gethostname(), 1111))
print("Enter the number of connections you want")
i = int(input())

s.listen(i)
print('Server is alive and waiting for connection from client')

while True:

    c, addr = s.accept()
    name = c.recv(2048).decode()
    print('server has written ', addr, name)
    msg="Welcome to a server. You are connected successfuly!"
    c.send(bytes(msg, "utf-8"))
    c.close()
