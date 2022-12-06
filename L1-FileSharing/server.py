import sys, os
import socket
import threading

print_lock = threading.Lock()

SERVER_DIR = "/home/the/Documents/BiT/2015/Distributed/Labs/Lab 1/L1-FileSharing"

def upload_file(filename, connection, address):
    print(f"[ {str(address)} ] File Upload Operation..")
    filepath = SERVER_DIR + filename
    with open(filepath, 'wb') as f_write:
        while True:
            print("receiving data..")
            data = connection.recv(1024)
            if not data:
                break
            f_write.write(data)
        f_write.close()

    print("[ {str(address)} ] File Uploaded successfully: ", filename)
    connection.close()
    return

def rename_operation(old_name, new_name, connection, address):
    print(f"[ {str(address)} ] File Rename Operation..")
    
    old_name = SERVER_DIR + old_name
    new_name = SERVER_DIR + new_name

    if not os.path.isfile(old_name):
        print(f"[ {str(address)}] File not found")
        connection.send("File not found")
    else:
        os.rename(old_name, new_name)
        print(f"[ {str(address)} ] File renamed successfully:  {old_name}  -> {new_name}")
        connection.send("rename successfull")
    return

def delete_operation(filename, connection, address):
    print(f"[ {str(address)} ] File Deletion operation..")
    filepath = SERVER_DIR + filename
    if os.path.isfile(filepath):
        os.remove(filepath)
        print(f"[ {str(address)} ] File deleted successfully")
        connection.send("Deleted successfully")
    else:
        print(f"[ {str(address) }] File not found")
        connection.send("File not found")

    return

def download_operation(filename, connection, address):
    filename = SERVER_DIR + filename

    if os.path.isfile(filename):
        connection.send("prep")
        with open(filename, 'rb') as f_send:
            print(f"[ {str(address)}] Sending Data..")
            data = f_send.read()
            connection.send(data)
            print(f"[ {str(address)} ] Sent")

        print(f"[ {str(address)}] File sent succesfully")
    else:
        print(f"[{str(address)}] File not exists")
    
    return

#print_lock = threading.Lock()
BUFFER_SIZE = 1024

def threaded(connection, address):
    commands = connection.recv(BUFFER_SIZE)
    input_values = commands.split(' ')
    if input_values[0] == "UPLOAD":
        print_lock.acquire()
        upload_file(input_values[1], connection, address)
        print_lock.release()
    elif input_values[0] == "RENAME":
        print_lock.acquire()
        rename_operation(input_values[1], input_values[2], connection, address)
        print_lock.release()
    elif input_values[0] == "DELETE":
        delete_operation(input_values[1], connection, address)
    elif input_values[0] == "DOWNLOAD":
        download_operation(input_values[1], connection, address)
    elif input_values[0] == "exit":
        pass
    
    #print_lock.release()
    connection.close()
    print(f"[ {str(address)} ] Connection closed")

def main():
    HOST = "127.0.0.1"
    PORT = 8080
    
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Starting server on port %s and server %s"%(PORT,HOST))
    s_socket.bind((HOST, PORT))
    
    s_socket.listen(5)
    
    while True:
        print("waiting for connection..")
        connection, address = s_socket.accept()
        print("Got connection from ", address)
        print("Sending acknowledgment..")

        connection.send("ACK")
        # start_new_thread(threaded, (connection,address,))
        threading.Thread(threaded, (connection,address))
        
    s_socket.close()
if __name__ == '__main__':
    main()