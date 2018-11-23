import time

print('# TCP')
print('TCP---client')

# # 导入socket库
# import socket
#
# # 创建一个socket
# # AF_INET指定使用IPv4协议; SOCK_STREAM指定使用面向流的TCP协议
# socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 建立连接
# # 80端口是Web服务的标准端口
# # connect()参数是一个tuple，包含地址host和端口号port
# socket.connect(('www.baidu.com', 80))
#
# # 发送请求，要求返回首页的内容
# #         send(data[, flags]) -> count
# #
# #         Send a data string to the socket.  For the optional flags
# #         argument, see the Unix manual.  Return the number of（...的数量） bytes
# #         sent; this may be less than len(data) if the network is busy.
# socket.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
#
# # 接受数据
# buffter = []
# while True:
#     # 每次最多接收1K字节,直到recv()返回空数据，表示接收完毕，退出循环
#     d = socket.recv(1024)
#     if d:
#         buffter.append(d)
#     else:
#         break
# data = b''.join(buffter)
#
# # 关闭连接
# socket.close()
#
# # 分离data中的HTTP头、网页
# header, html = data.split(b'\r\n\r\n', 1)
# print('header :', header.decode('utf-8'))
# # 把接收的数据写入文件
# with open('baidu.html', 'wb') as f:
#     f.write(html)

print('TCP---server')
# 代码详见echo_server.py / tcp_client.py

