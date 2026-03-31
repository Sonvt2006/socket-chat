import socket
import threading

def start_server():
    server_ip = "localhost"
    server_port = 5555

    server_socket = socket.socket()

    server_socket.bind((server_ip, server_port))

    server_socket.listen(2)
    print("Server is listening for request!")

    conn1, addr1 = server_socket.accept()
    client_thread_1 = threading.Thread(target=connect, args=(conn1, ))
    client_thread_1.start()

    conn2, addr2 = server_socket.accept()
    client_thread_2 = threading.Thread(target=connect, args=(conn2, ))
    client_thread_2.start()


    client_thread_1.join()
    client_thread_2.join()


    server_socket.close()

def connect(conn):
    while True:
        msg = conn.recv(2048).decode()
        print("Client: " + msg)

        if msg.lower() == "exit":
             break
    conn.close()

if __name__ == "__main__":
    start_server()