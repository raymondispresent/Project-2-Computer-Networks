import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECTFROMTHESERVERLOL"
SERVER = "192.168.0.66"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode('utf-8'))

print("Please input 'start' to send test message to server")
input("start")
send("test!")
print("Please input 'disconnect' to send disconnect message to server")
input("disconnect")

send(DISCONNECT_MESSAGE)
