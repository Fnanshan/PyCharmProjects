
#-*- conding:utf-8 -*-
import socket

sk = socket.socket()

sk.bind(("127.0.0.1",8080))

sk.listen(2)

conn,addr = sk.accept()
while True:
    ret = conn.recv(1024).decode()#byte类型  解码
    print(ret)
    if ret == "bye":
        conn.send(b"by")
        conn.close()
    info = input(">>").encode("utf-8")#以utf-8的格式进行编码  生成byte类型对象
    conn.send(info)

sk.close()