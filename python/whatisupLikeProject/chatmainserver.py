import socket as skt
import threading
import time as tm
import sys as sys

# Define a function to handle client communication
def handle_client(client_socket, address):
    print(f"Client {address} connected")
    client_socket.send("Welcome to the chat server".encode())
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if data:
                print(f"Client {address}: {data}")
                # Broadcast the message to all connected clients
                for client in clients:
                    if client != client_socket:
                        client.send(f"Client {address}: {data}".encode())
            else:
                break
        except:
            break
    client_socket.close()
    clients.remove(client_socket)
    print(f"Client {address} disconnected")

# Create the server socket
ChatServer = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
ChatServerIP = skt.gethostbyname(skt.gethostname())

# Bind and listen
ChatServer.bind((ChatServerIP, 5000))
ChatServer.listen(5)

# List to store connected clients
clients =[] 

ClentDataBase = [] 


def HanldleNewCLient (client_socket, address) : 
    
    data = client_socket.
    
    Client = {Name :}




# Main server loop
while True:
    # Accept a new client connection 
    # Accept Function is a bllocking to the system 
    # Working as polling mode 
    client_socket, address = ChatServer.accept()
    
    #TODO : we Can have a function here that Can Assign the Clent soket and Address to A user Name make such Data Base in which we Can Save Data 
    clients.append(client_socket)
    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()

ChatServer.close()
print("Chat server closed")
