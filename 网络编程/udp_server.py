import socket

# SOCK_DGRAM 制定了这个Socket的类型是UDP
socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketServer.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999')
while True:
    # 接收数据
    # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
    # recvfrom(buffersize[, flags]) -> (data, address info)
    #         Like recv(buffersize, flags) but also return the sender's address info.
    data, addr = socketServer.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # sendto(data[, flags], address) -> count
    #         Like send(data, flags) but allows specifying the destination address. 允许指定目标地址
    #         For IP sockets, the address is a pair (hostaddr, port).
    socketServer.sendto(b'Hello, %s!' % data, addr)