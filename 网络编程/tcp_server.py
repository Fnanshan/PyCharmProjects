import socket
import threading
import time
# 服务器程序
# 每个连接必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接


def tcplink(newSocket, newAddress):
    print('Accept new connection from %s:%s...' % newAddress)
    # send(data[, flags]) -> count
    #         Send a data string to the socket.
    newSocket.send(b'Welcome!')
    while True:
        data = newSocket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        newSocket.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    newSocket.close()
    print('Connection from %s:%s closed.' % newAddress)


socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
socketServer.bind(('127.0.0.1', 9999))
# 监听端口
socketServer.listen(5)
print('Waiting for connection...')
while True:
    # accept() -> (socket object, address info)
    #         Wait for an incoming connection.  Return a new socket
    #         representing the connection, and the address of the client.
    #         For IP sockets, the address info is a pair (hostaddr, port).
    # 接收一个新连接
    newSocket, newAddress = socketServer.accept()
    print('newAddress :', newAddress)
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(newSocket, newAddress))
    t.start()