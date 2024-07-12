"""
As a Server  the next sequence need to be followed 
1- Creat a socket 
2 -  bind
3- lisent 
4- conect 
5- accept 
6- read 
7- write 
8- close 
"""

import socket as skt 
import time as tm 


"""
creat the socket 
 AF_INET  = standard internet addresses you're familiar with, like 192.168.1.100. 
SOCK_STREAM = 
STREAM: This indicates that your socket will use a stream-oriented protocol.
What Does Stream-Oriented Mean?

Think of a stream like a continuous flow of data. Here's how it works:

Connection: A stream socket establishes a persistent connection between two endpoints (like a server and a client).
Data Flow: Data is sent in a continuous stream, like a river flowing.
Ordered Delivery: Data is delivered in the order it was sent.
Reliable Transmission: Stream sockets typically provide mechanisms for error detection and retransmission, ensuring reliable data delivery.

"""
serversocket=skt.socket(skt.AF_INET,skt.SOCK_STREAM) 


#get the Current IP using the skt function 
ServerIP = skt.gethostbyname(skt.gethostname()) 
print(ServerIP)


#bind the socket to the address and port 
serversocket.bind((ServerIP,1234)) 

#listen for incoming connections 
# list(5) 5 >> the mmaximum number of the connection that Cna be queued 
# in case of more conection is requested it will be rejected 
serversocket.listen(5) 

clientsocket,address = serversocket.accept() 
while True: 

    #accept the connection 

    print(f"Connection from {address}")

    #read data from the client 
    data = clientsocket.recv(1024).decode('utf-8') 

    print(f"Client sent: {data}")

    #send data to the client 
    clientsocket.send("Hello from the server!".encode('utf-8'))

    tm.sleep(1)
    if data == "exit":
        #send data to the client 
        clientsocket.send("exit".encode('utf-8'))
        clientsocket.close() 
        serversocket.close() 
 
        break 

 
 


