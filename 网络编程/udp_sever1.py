import socket

sk = socket.socket(type = socket.SOCK_DGRAM)

sk.bind(("127.0.0.1",8080))
while True:
    msg,addr = sk.recvfrom(1024)
    ret = msg.decode()
    print(ret)
    if ret == "bye":
        sk.sendto(b"bye",addr)
        sk.close()
    info = input(">>").encode("utf-8")
    sk.sendto(info,addr)