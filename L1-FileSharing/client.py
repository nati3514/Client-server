import sys, os
import socket

HOST = "127.0.0.1"
PORT = 8080
BUFFER_SIZE = 1024

CLIENT_DIR = "/home/the/Documents/BiT/2015/Distributed/Labs/Lab 1/L1-FileSharing"

def get_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to port %s and server %s" % (PORT,HOST))
    server_socket.connect((HOST, PORT))
    ack = server_socket.recv(BUFFER_SIZE)
    if ack == "ACK":
        print("Connected to server and got acknowledgments: ",ack)
        return server_socket


def upload_file(filename, connection):
    connection.send("UPLOAD " + filename)
    filepath = CLIENT_DIR + filename 
    if os.path.isfile(filepath):
        with open(filepath, 'rb') as f_send:
            print("Sending data..")
            data = f_send.read()
            connection.send(data)
            print("Sent.....")
        connection.close()
        #success = connection.recv(BUFFER_SIZE)
        print("Uploaded file successfully: ", filename)
    else:
        print("File not found")
    connection.close()
    return

def rename_file(old_name, new_name, connection):
    connection.send("RENAME " + old_name + " " + new_name)
    success = connection.recv(BUFFER_SIZE)
    print("Server Message: ", success)
    #print "Closing connection.."
    connection.close()
    return

def delete_file(filename, connection):
    #connection = get_socket()
    connection.send("DELETE " + filename)
    message = connection.recv(BUFFER_SIZE)
    print("Server Message: ", message)
    #print "Closing connection.."
    connection.close()
    return

def download_file(filename, connection):
    #connection = get_socket()
    connection.send("DOWNLOAD "+ filename)
    message = connection.recv(BUFFER_SIZE)
    filepath = CLIENT_DIR + filename
    if message == "prep":
        with open(filepath, 'wb') as f_write:
            while True:
                print("receiving data..")
                data = connection.recv(BUFFER_SIZE)
                if not data:
                    break
                f_write.write(data)
            f_write.close()
        print ("File Downloaded successfully")
    else:
        print("Error in Download")
    connection.close()
    return

def client_option():

    #connection = get_socket()

    while True:
        connection = get_socket()
        menu = input("Enter your choices: upload, download, rename, delete, exit: ")
        if menu == "upload":
            filename = input("Enter File name to upload: ")
            upload_file(filename, connection)
        elif menu == "rename":
            old_name = input("Old file name: ")
            new_name = input("New file name: ")
            rename_file(old_name, new_name, connection)
        elif menu == "delete":
            filename = input("File name to delete: ")
            delete_file(filename, connection)
        elif menu == "download":
            filename = input("File name to download: ")
            download_file(filename, connection)
        elif menu == "exit":
            connection.send("exit ")
            break
        else:
            print("Invalid choices, choose again")
    print("Closing connection...")
    connection.close()


client_option()