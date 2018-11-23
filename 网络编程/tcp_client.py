import socket
# 客户端程序
import time

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
socketClient.connect(('127.0.0.1', 9999))
# 接收server发送的welcome
# recv(buffersize[, flags]) -> data
#         Receive up to buffersize bytes from the socket. 接收来自套接字的缓冲区字节
print(socketClient.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    socketClient.send(data)
    print('# 循环中...')
    # 接收server发送的'Hello ...'
    print(socketClient.recv(1024).decode('utf-8'))
socketClient.send(b'exit')
socketClient.close()