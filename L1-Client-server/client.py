from email import message
import socket, threading, sys

#wait for incoming data from server
def receive(socket,signal):
    while True:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8"))) # decode to printable format
        except:
            print("You have been disconnected from server")
            signal = False
            break

# get host and port
host = input("Host:")
port = (int(input("Port:")))

#connect to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

except:
    print("Failed to connnet")
    input("Press enter to quit")
    sys.exit(0)
    
# new thread to wait for data
receiveThread =  threading.Thread(target=receive, args=(sock,True))
receiveThread.start()

#send data to server
while True:
    message = input()
    sock.signalall(str.encode(message)) # encodestring to bytes
    
            