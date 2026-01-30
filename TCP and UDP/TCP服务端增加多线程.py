from socket import *
from threading import Thread


def recv_data():
    while True:
        recv_data = client_socket.recv(1024)
        recv_content = recv_data.decode('gbk')
        print(f"收到信息:{recv_content},来自:{client_into}")
        if recv_data == "end":
            print("结束连接")
            break



def send_data():
    while True:
        msg = input(">")
        client_socket.send(msg.encode('gbk'))
        if msg == "end":
            print("结束连接")
            break



if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_STREAM)  # 建立TCP套接字
    server_socket.bind(('127.0.0.1', 8899))  # 本机监听8899端口
    server_socket.listen(5)
    print("等待接收链接！")
    client_socket, client_into = server_socket.accept()
    print("一个客户端建立链接！")


    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

client_socket.close()
server_socket.close()