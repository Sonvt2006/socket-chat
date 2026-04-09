import socket

server_ip = "localhost"
server_port = 5555

client_socket = socket.socket()

try: 
    client_socket.connect((server_ip, server_port))
except Exception as e:
    print("Error: " + e)

print("Type your messages here:")
while True:
    msg = input()
    while msg == "":
        msg = input()
    client_socket.send(msg.encode())

    msg_cf = client_socket.recv(2048).decode()
    print(msg_cf)
    if msg.lower() == "exit":
        break
