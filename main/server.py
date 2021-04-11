import socket 
import threading
import time

HEADER = 64
PORT = 5050
SERVER = "192.168.0.66"
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "DISCONNECTFROMTHESERVERLOL"
REPORT_MESSAGE = "REPORTTHEVALUES"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("Disconnect message received from house ".encode('utf-8'))
            else:
                conn.send("Message received from house ".encode('utf-8'))
                print(f"[{addr}] {msg}")



    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections {threading.activeCount() - 1}")


print("Server monitoring home energy consumption is starting...")
start()