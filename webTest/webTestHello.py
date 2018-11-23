

# 定义WSGI接口（为了响应HTTP请求，HTTP处理函数），application由WSGI服务器来调用。
# environ : 包含所有HTTP请求信息的dict对象；
# start_response : 发送HTTP响应的函数，Header只能发送一次
# return作为HTTP响应的Body也要发送给浏览器
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:].encode('utf-8') or 'web')
    # return [b'<h1>Hello, web!</h1>']
    return [body.encode('utf-8')]
