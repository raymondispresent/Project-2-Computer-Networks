import socket
import os
import threading

SERVER_HOST = "192.168.0.66"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_HOST, SERVER_PORT))

def handle_client(conn, addr):
    print(f"[+] {addr} is connected.")
    received = conn.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    with open(filename, "wb") as f:
        while True:
            bytes_read = conn.recv(BUFFER_SIZE)
            if not bytes_read:
                print("File finished receiving")
                break
            f.write(bytes_read)

    conn.close()

def start():
    s.listen()
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections {threading.activeCount() - 1}")


print("Server monitoring greater estate energy consumption is starting...")
start()