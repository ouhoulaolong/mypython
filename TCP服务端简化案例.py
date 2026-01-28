from socket import *


server_socket = socket(AF_INET, SOCK_STREAM)  #建立TCP套接字
server_socket.bind(('127.0.0.1',8899))         #本机监听8899端口
server_socket.listen(5)
print("等待接收链接！")
client_socket, client_into = server_socket.accept()
recv_data = client_socket.recv(1024)
print(f"收到信息:{recv_data.decode('gbk')},来自:{client_into}")
client_socket.close()
server_socket.close()