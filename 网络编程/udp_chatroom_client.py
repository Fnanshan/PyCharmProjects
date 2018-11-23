import socket, threading, os

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sendto(data[, flags], address) -> count
#         Like send(data, flags) but allows specifying the destination address. 允许指定目标地址
#         For IP sockets, the address is a pair (hostaddr, port).
socketClient.sendto(b'pong', ('127.0.0.1', 6666))


def myinput():
    while True:
        try:
            msg = input('>>>')
            yield msg
        except Exception as e:
            os._exit(0)


def getMsg(socketClient):
    while True:
        try:
            r = socketClient.recv(1024)
            print('\n', r.decode('utf-8'), '\n>>>', end='')
        except Exception as e:
            print(e)


c = myinput()


def sendMsg(msg):
    while True:
        msg = next(c)
        socketClient.sendto(msg.encode('utf-8'), ('127.0.0.1', 6666))


threading.Thread(target=sendMsg, args=(socketClient,)).start()
threading.Thread(target=getMsg, args=(socketClient,)).start()
