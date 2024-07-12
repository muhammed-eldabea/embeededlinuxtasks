import socket as sktk
import threading as thrd
import time as tm
from inputimeout import inputimeout as intimout

clinets = []
UserNames = []
addresses = []
ServerISRunning = "R"

def ClientNewHadling(clientsoket, add):
    clientsoket.send("send the UserName to server".encode('utf-8'))
    UserName = clientsoket.recv(1024).decode('utf-8')  # Receive username
    UserNames.append(UserName.strip())
    clinets.append(clientsoket)
    addresses.append(add)

def clientDataSwitch(client_skt, address):
    while True:
        try:
            data = client_skt.recv(1024).decode('utf-8')
            if data:
                # Split the data into sender and message
                sender, message = data.split(":", 1)  # Correct splitting
                sender = sender.strip()
                message = message.strip()

                # Find the receiver's index
                try:
                    receiverIndex = UserNames.index(sender)
                except ValueError:
                    client_skt.send("The receiver is not logged to the server".encode('utf-8'))
                else:
                    # Send the message to the receiver
                    clinets[receiverIndex].send(f"[{sender}] >> {message}".encode('utf-8'))
        except ConnectionResetError:
            # Handle client disconnection
            print(f"Client at {address} disconnected.")
            clinets.remove(client_skt)
            UserNames.remove(sender)
            break

ServerSoket = sktk.socket(sktk.AF_INET, sktk.SOCK_STREAM)
ServerIP = sktk.gethostbyname(sktk.gethostname())
ServerSoket.bind((ServerIP, 51234))
ServerSoket.listen(5)

def ServerStateseitch():
    global ServerISRunning
    # Use a simple input to check for shutdown
    ServerISRunning = intimout( prompt= "Enter 'q' to quit the server: ",timeout=30)
    if ServerISRunning.lower() == 'q':
        ServerISRunning = "Q"

while ServerISRunning == "R":
    clinet, address = ServerSoket.accept()
    ClientNewHadling(clinet, address)
    thread = thrd.Thread(target=clientDataSwitch, args=(clinet, address))
    threadServerHandle = thrd.Thread(target=ServerStateseitch)
    threadServerHandle.start()
    thread.start()
else:
    ServerSoket.close()
