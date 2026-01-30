from socket import *
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1',8899))
while True:
    #给服务端发消息
    msg = input(">")
    client_socket.send(msg.encode('gbk'))
    if msg == "end":
        break
    recv_data = client_socket.recv(1024)
    print(f"服务点说{recv_data.decode('gbk')}")
client_socket.close()