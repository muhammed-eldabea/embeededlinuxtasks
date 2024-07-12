import socket as skt
import threading as thr 
import time as tm
import sys as sys 


# Create a socket object
client = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.1.1', 5000))

# Function to handle user input
def send_message():
    while True:
        message = input()
        client.send(message.encode())

# Create a new thread to handle user input
send_thread = thr.Thread(target=send_message)
send_thread.start()

# Receive messages from the server
while True:
    try:
        data = client.recv(1024).decode()
        if data:
            print(data)
    except:
        break

client.close()
print("Client disconnected")