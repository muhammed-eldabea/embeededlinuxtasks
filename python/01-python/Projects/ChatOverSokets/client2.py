import socket as sktk
import threading as thrd
import time as tm

UserName = input("Enter Your Name :")
ReciverName = input("Enter the receiver Name: ")

clientSocket = sktk.socket(sktk.AF_INET, sktk.SOCK_STREAM)
clientSocket.connect(('127.0.1.1', 51234))

# Client Setup
data = clientSocket.recv(1024).decode('utf-8')
while data != "send the UserName to server":
    data = clientSocket.recv(1024).decode('utf-8')
    tm.sleep(1)
clientSocket.send(UserName.strip().encode('utf-8'))  # Send username once

# ... (rest of the client code) ...

def clientDataSwitch() : 
    while True :
        data = clientSocket.recv(1024).decode('utf-8')
        if data :
            print(data)
        else :
            pass

thread = thrd.Thread(target=clientDataSwitch)
thread.start()

while True : 
    Message = input()
    clientSocket.send(f"{ReciverName}:{Message}".encode('utf-8')) 
    tm.sleep(1)


clientSocket.close() 
