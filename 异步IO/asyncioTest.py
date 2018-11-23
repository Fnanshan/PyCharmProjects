print('# 从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。')
# # 从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
# import asyncio
#
#
# async def hello():
#     print('hello world')
#     # 异步调用asyncio.sleep(1)
#     r = await asyncio.sleep(5)
#     print('hello again!')
#
#
# # 获取EventLoop
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

print('# # 用Task封装两个coroutine （两个coroutine是由同一个线程并发执行的。）')
# # 用Task封装两个coroutine （两个coroutine是由同一个线程并发执行的。）
# import threading
# import asyncio
#
#
# async def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     await asyncio.sleep(10)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

print('# # 用asyncio的异步网络连接来获取sina、sohu和163的网站首页')
# # 用asyncio的异步网络连接来获取sina、sohu和163的网站首页
# import asyncio
#
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()