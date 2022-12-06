from audioop import add
from concurrent.futures import thread
from multiprocessing.connection import Client
from signal import signal
import socket
import threading
from unittest.mock import CallableMixin

connections =[] #connections information
total_connections = 0

#client class for each connection instance with socket addresses
class client (threading.Thread):
    #constructor class
    def _init_(self,socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
    
    def __str__(self) -> str:
        return str(self.id) + "" + str(self.address)
    
    #attempt to get data from client, 
    # if not successful, assume it is disconnected and remove it from network
    #if succeed, print data to server and other clients
    
    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(32)
            except:
                print(f"Client {str(self.address)} has disconnected")
                self.signal = False
                connections.remove(self)
                break
            if data !="":
                print(f"ID {str(self.id)} : {str(data.decode('UTF-8'))}")
                for client in connections:
                    if client.id!= self.id:
                        client.socket.sendall(data)
    
def newConnections(socket):
        while True:
            sock, address = socket.accept()
            global total_connections
            connections.append(Client(sock, address,total_connections))
            connections[len(connections)-1].start()
            print(f"New connection at ID {str(connections[len(connections)-1])}")
            total_connections += 1
        
def main():
        host = input("Host :")
        port = int(input("Port: "))
        
        # create new server socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(5)
        
        # new thread to wait for new connection
        newConnectionThread = threading.Thread(target=newConnections, args=(sock,))
        newConnectionThread.start()
        
    
main()