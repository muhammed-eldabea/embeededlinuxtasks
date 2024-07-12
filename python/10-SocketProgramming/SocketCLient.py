"""
As a client  the next sequence need to be followed 
1- Creat a socket 
3- conect 
4- accept 
5- read 
6- write 
7- close

"""

import socket as skt 
import time as tm 


ClientSoket = skt.socket(skt.AF_INET,skt.SOCK_STREAM)


ServerADD = ('127.0.1.1',1234)

print(ServerADD) 

ClientSoket.connect(ServerADD) 

while True: 
    #send data to the server 
    message = input("Enter message to send: ")
    ClientSoket.send(message.encode('utf-8'))

    #read data from the server 
    data = ClientSoket.recv(1024).decode('utf-8') 
    print(f"Server sent: {data}")

    tm.sleep(1)
    if data == "exit":
        #send data to the client 
        ClientSoket.close() 
 
        break 
