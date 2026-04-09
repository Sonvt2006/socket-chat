import socket
import threading

def start_server():
    server_ip = ""
    server_port = 5555

    server_socket = socket.socket()

    server_socket.bind((server_ip, server_port))

    server_socket.listen(10)
    print("Server is listening for request!")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target = connect, args = (conn, addr))
        client_thread.start()

def connect(conn, addr):
    try:
        while True:
            msg = conn.recv(2048).decode()
            if msg == "exit" or msg == "":
                conn.close()
                print("Connection with " + str(addr) + " was closed")
                break
            print(str(addr) + ": " + msg)
            conn.send("message received!".encode())
    except Exception as e:
        print("Connection with " + str(addr) + " was closed due to: " + e)

if __name__ == "__main__":
    start_server()