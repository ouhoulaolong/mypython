from socket import *
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1',8899))
client_socket.send('Hello world'.encode('gbk'))
client_socket.close()