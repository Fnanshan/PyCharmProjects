import socket
import time

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    socketClient.sendto(data, ('127.0.0.1', 9999))
    # 接收数据
    print(socketClient.recv(1024).decode('utf-8'))
    time.sleep(3)
socketClient.close()