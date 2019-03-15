

import socket

sk = socket.socket()
ip_port = ('127.0.0.1',8080)

sk.connect(ip_port)
while True:
    info = input(">>").encode("utf-8")
    sk.send(info)
    ret = sk.recv(1024).decode()
    print(ret)
    if ret == "bye":
        sk.close()