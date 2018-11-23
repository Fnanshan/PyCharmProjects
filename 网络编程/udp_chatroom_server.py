import socket

socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketServer.bind(('127.0.0.1', 6666))
# set() -> new empty set object
clients = set()
print('server bind 127.0.0.1:6666')

while True:
    try:
        # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
        data, addr = socketServer.recvfrom(1024)
        print('data :', data)
        print('addr :', addr)
        clients.add(addr)
        if not data or data.decode('utf-8') == 'pong':
            continue
        print('%s:%s >>> %s' % (addr[0], addr[1], data.decode('utf-8')))
        print('clients :', clients)
        for usr in clients:
            # 如果客户端>1时，把信息给usr发过去
            if usr != addr:
                print('usr :', usr)
                print('addr :', addr)
                socketServer.sendto(('%s:%s >>> %s' % (addr[0], addr[1], data.decode('utf-8'))).encode('utf-8'), usr)
    except Exception as e:
        print(e)