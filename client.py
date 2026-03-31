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
    client_socket.send(msg.encode())
    if msg.lower() == "exit":
        break
