from email.parser import Parser
from email.utils import parseaddr, formataddr

print('# 最简单的纯文本邮件')

from email.mime.text import MIMEText
from email.header import Header


# 通过SMTP发送
# 输入Email地址和口令
from_addr = input('From : ')
password = input('Password :')
# 输入收件人地址
to_addr = input('To :')
# 输入SMTP服务器地址
smtp_server = input('SMTP server :')


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
#

# 构造一个最简单的纯文本邮件
msg = MIMEText('天王盖地虎，宝塔镇河妖。', 'plain', 'utf-8')
# Q :554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件
# A :msg的From、To、Subject不填99%可能被判定为垃圾邮件
#    注意msg的From、To不会自动填的
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自你大爷的问候......', 'utf-8').encode()  # ---------------成功
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
#
#
# import smtplib
# server = smtplib.SMTP(smtp_server, 25)
# # smtp.163.com SSL协议端口号465/994；非SSL协议端口号25
# # set_debuglevel() :设置调试输出级别；1:印出和SMTP服务器交互的所有信息
# server.set_debuglevel(1)
# # 登录SMTP服务器
# server.login(from_addr, password)
# # as_string() :Return the entire formatted message as a string. 将整个格式化的消息作为字符串返回
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

print('# 完整的邮件')

# '''
# 邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，
# 而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件
# '''
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
#
# import smtplib
#
#
# # 格式化邮件地址
# # 不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
# def _format_addr(s):
#     # parseaddr(addr) :
#     #   Parse addr into its constituent realname and email address parts. 将addr解析为其组成部分realname和电子邮件地址部分。
#     name, addr = parseaddr(s)
#     print('name :', name)
#     print('addr :', addr)
#     # name : Python爱好者  addr : 634635262@qq.com
#     # name : 管理员        addr : daemonnnn@163.com
#     # formataddr(pair, charset='utf-8'):
#     #   The inverse of(逆向) parseaddr(), this takes a 2-tuple of the form
#     #       (realname, email_address) and returns the string value suitable
#     #       for an RFC 2822 From, To or Cc header.
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
#
# # ------------------fanshuangshuai@foxmail.com 授权码------------rfayqrebpakxbbig---------------------
# from_addr = input('From :')
# password = input('Password :')
# to_addr = input('To :')
# smtp_server = input('SMTP server :')
#
# msg = MIMEText('你TM折磨了我一天，终于好使了', 'plain', 'utf-8')
# msg['From'] = from_addr
# msg['To'] = to_addr
# # msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# # msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可
# # msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自你大爷的关爱......', 'utf-8').encode()  # ---------------成功
# # msg['Subject'] = Header('来自你大爷的问候......', 'utf-8').encode()  # ---------------成功
# # msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()-----------------失败
# # msg['Subject'] = Header('来自English的问候......', 'utf-8').encode()----------------失败
# # msg['Subject'] = Header('i have no idea......', 'utf-8').encode() # ----------------失败
# # msg['Subject'] = Header('i have no idea......', 'utf-8').encode()  # ----------------失败
#
#
#
# # msg['From'] = 'daemonnnn@163.com'  # 这样写必错，不要问我为什么
# # msg['To'] = 'fanshuangshuai@foxmail.com'     # 这样写必错，不要问我为什么
#
# # msg['From'] = from_addr
# # msg['To'] = to_addr
#
# server = smtplib.SMTP(smtp_server, 25)
# server.starttls()
# server.set_debuglevel(1)
# server.login(from_addr, password)
# print('msg.as_string() :', msg.as_string())
# server.sendmail(from_addr, to_addr, msg.as_string())
# server.quit()

print('# 发送HTML邮件')

print('# 发送附件')

# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.utils import parseaddr, formataddr
#
# import smtplib
#
#
# # 格式化邮件地址
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
#
# from_addr = input('From :')
# password = input('Password :')
# to_addr = input('To :')
# smtp_server = input('SMTP server :')
#
# # 邮件对象
# msg = MIMEMultipart()
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自你大爷的问候......', 'utf-8').encode()
#
# # 邮件正文是MIMEText
# msg.attach(MIMEText('发送附件发送附件发送附件', 'plain', 'utf-8'))
#
# # 添加附件就是加上一个MIMEBase，从本地读取一个图片
# with open('D:\Picture/伊涅斯塔.jpg', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是jpg类型
#     mime = MIMEBase('image', 'jpg', filename='伊涅斯塔.jpg')
#     # 加上必要的头信息
#     mime.add_header('Content-Disposition', 'attachment', filename='伊涅斯塔.jpg')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来
#     mime.set_payload(f.read())
#     # 用base64编码
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart
#     msg.attach(mime)
#
# server = smtplib.SMTP(smtp_server, 25)
# # encrypt the rest of the SMTP session.  加密SMTP会话的其余部分
# server.starttls()
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

print('# 通过POP3下载邮件')

# from email.parser import Parser
# import poplib
#
# # 输入邮件地址，口令和POP3服务器地址
# # email = input('Email :')
# # password = input('Password :')
# # pop3_server = input('POP3 server :')
#
# # email = 'www.884523205@qq.com'
# # email = 'fanshuangshuai@foxmail.com'
# email = '634635262@qq.com'
# password = 'rfayqrebpakxbbig'
# pop3_server = 'pop.qq.com'
#
# # email = 'daemonnnn@163.com'
# # password = 'daemonnnn163'
# # pop3_server = 'pop.163.com'
#
#
# # 连接到POP3服务器
# # server = poplib.POP3(pop3_server)
# # qq邮箱pop3得使用SSL安全连接才可以登录,不然就会报错的。
# server = poplib.POP3_SSL(pop3_server, port=995)
# # 打开调试信息
# server.set_debuglevel(1)
# # 可选：打印POP3服务器的欢迎文字
# print(server.getwelcome().decode('utf-8'))
#
# # 身份认证
# server.user(email)
# server.pass_(password)
#
# # stat()返回邮件数量和占用空间
# print('Messages : %s. Size : %s' % server.stat())
# response, mails, octets = server.list()
# # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
# print('mails :', mails)
#
# # 获取最新的一封邮件，注意索引号从1开始
# index = len(mails)
# print('index :', index)
# response, lines, octets = server.retr(index)
#
# # lines存储了邮件的原始文本的每一行
# # 可以获得整个邮件的原始文本
# msg_content = b'\r\n'.join(lines).decode('utf-8')
# # 稍后解析出邮件
# msg = Parser().parsestr(msg_content)
#
# # 可以根据邮件索引号直接从服务器删除邮件
# # server.dele(index)
# # 关闭连接
# server.quit()
#
# print('# 解析邮件')
#
# from email.parser import Parser
# from email.header import decode_header
# from email.utils import parseaddr
#
# import poplib
#
#
# # 递归地打印出Message对象的层次结构
# # indent用于缩进显示
# def print_info(msg, indent=0):
#     if indent == 0:
#         for header in ['From', 'To', 'Subject']:
#             value = msg.get(header, '')
#             if value:
#                 if header == 'Subject':
#                     value = decode_str(value)
#                 else:
#                     hdr, addr = parseaddr(value)
#                     name = decode_str(hdr)
#                     value = u'%s <%s>' % (name, addr)
#             print('%s%s: %s' % ('  ' * indent, header, value))
#     if (msg.is_multipart()):
#         parts = msg.get_payload()
#         for n , part in enumerate(parts):
#             print('%spart %s' % ('   ' * indent, n))
#             print('%s---------------------------' % ('   ' * indent))
#             print_info(part, indent + 1)
#     else:
#         content_type = msg.get_content_type()
#         if content_type == 'text/plain' or content_type == 'text/html':
#             content = msg.get_payload(decode=True)
#             charset = guess_charset(msg)
#             if charset:
#                 content = content.decode(charset)
#             print('^%sText: %s' % ('   ' * indent, content + '...'))
#         else:
#             print('%sAttachment: %s' % ('   ' * indent, content_type))
#
#
# # 邮件的Subjecy或者Email中包含的名字都是经过编码后的str,要正常显示，就必须decode.
# def decode_str(s):
#     value, charset = decode_header(s)[0]
#     if charset:
#         value = value.decode(charset)
#     return value
#
#
# # 文本邮件的内容也是str，需要检测编码
# def guess_charset(msg):
#     charset = msg.get_charset()
#     if charset is None:
#         content_type = msg.get('Content-Type', '').lower()
#         pos = content_type.find('charset=')
#         if pos >= 0:
#             charset = content_type[pos + 8:].strip()
#     return charset
#
#
# print_info(msg)
#
