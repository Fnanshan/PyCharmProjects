# -*- coding: GBK -*-
print('-------------datetime------------')
from datetime import datetime

print('# 当前日期和时间')
# 当前日期和时间
# now = datetime.now()
# print(now)
# print(type(now))

print('# 指定日期和时间')
# 指定日期和时间
# dt = datetime(1970, 1, 3, 0, 0)
# print(dt)

print('# datetime 转换为 timestamp（时间戳）--- timestamp()')
# datetime 转换为 timestamp（时间戳）
# epoch time（纪元时间）=0: 1970年1月1日 00:00:00 UTC+00:00时区的时刻
# 当前时间就是相对于epoch time的秒数，称为timestamp（时间戳）
# timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# print(now)
# print(now.timestamp())

print('# timestamp 转换为 datetime --- fromtimestamp()')
# timestamp 转换为 datetime
# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间（当前操作系统设定的时区）做转换。
# t = 1541753943.510553
# print(datetime.fromtimestamp(t))
# # 格林威治标准时间与北京时间差了8小时
# print(datetime.utcfromtimestamp(t))

print('# str 转换为datetime ---- datetime.strptime()')
# str 转换为datetime，转换后的datetime是没有时区信息的。
# str = '2015-5-12 18:29:59'
# toDatetimeFormat = '%Y-%m-%d %H:%M:%S'
# cday = datetime.strptime(str, toDatetimeFormat)
# print(cday)

print('# datetime 转换为 str ---- strftime()')
# datetime 转换为 str
# toStrFormat = '%a, %b %d %H:%M'
# print(now.strftime(toStrFormat))

print('# datetime加减 ---- timedelta class')
# datetime加减
# from datetime import datetime, timedelta
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))
# print(now + timedelta(days=2, hours=12))

print('# 本地时间转换为UTC时间 --- tzinfo property')
# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
# from datetime import datetime, timedelta, timezone
# now = datetime.now()
# tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
# dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
# print('now :', now, ' type :', type(now))
# print('tz_utc_8 :', tz_utc_8, ' type :', type(tz_utc_8))
# print('dt :', dt, ' type :', type(dt))


print('# 时区转换 --- utcnow() --- astimezone()')
# 时区转换
# 先通过utcnow()拿到当前的UTC时间，再用astimezone()转换为任意时区的时间：
# from datetime import datetime, timedelta, timezone
# # 拿到UTC时间，并强制设置时区为UTC+0:00
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print('utc_dt :', utc_dt)
# # astimezone()将转换时区为北京时间
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print('bj_dt :', bj_dt)
# # astimezone()将转换时区为东京时间
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print('tokyo_dt :', tokyo_dt)
# # astimezone()将bj_bt转换时区为tokyo_dt
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print('tokyo_dt2 :', tokyo_dt2)

# summary
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

print('# 练习')
# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
# 思路： 1.str -> datetime；
#        2.datetime -> timezone
#             2.1 set UTC+0:00
#             2.2 'UTC+7:00' -> '7'
#             2.3 astimezone(timezone(timedelta(hours=7))
#        3.datetime -> timestamp
# from datetime import datetime, timezone, timedelta
#
#
# def to_timestamp(dt_str, tz_str):
#     toDatetimeFormat = '%Y-%m-%d %H:%M:%S'
#     cday = datetime.strptime(dt_str, toDatetimeFormat)
#     print('cday :', cday)
#     tz_str2 = int(tz_str.split()[0][3:6])
#     tz_utc_some = timezone(timedelta(hours=tz_str2))  # 创建时区UTC+8:00
#     dt = cday.replace(tzinfo=tz_utc_some)  # 强制设置为UTC+8:00
#     return dt.timestamp()
#
#
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+07:00')
# assert t1 == 1433121030.0, t1
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
#
# print('ok')

print('-------------collections------------')

print('# namedtuple')
# from collections import namedtuple
# # namedtuple('名称', [属性list]):
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x)
# print(p.y)

print('# deque')
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)

print('# defaultdict')
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值。
# 默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# from collections import defaultdict
# dd = defaultdict(lambda : 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

print('# OrderedDict')
# from collections import OrderedDict
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)])
# print(od)


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
# class LastUpdateOrderedDict(OrderedDict):
#     def __init__(self, capacity):
#         super(LastUpdateOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove :', last)
#         else:
#             print('add :', (key, value))
#         OrderedDict.__setitem__(self, key, value)


print('# ChainMap')
# # ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# from collections import ChainMap
# import os, argparse
#
# # 构造缺省参数
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }
#
# # 构造命令行参数
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k: v for k, v in vars(namespace).items() if v}
#
# # 组合成ChainMap
# combined = ChainMap(command_line_args, os.environ, defaults)
#
# # pring arguments
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])

print('# Counter')
# # Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)

print('# base64')
# # # base64可以直接进行base64的编解码
# import base64
# encodeStr = base64.b64encode(b'binary\x00string')
# print(encodeStr)
# decodeStr = base64.b64decode(b'YmluYXJ5AHN0cmluZw====')
# print(decodeStr)
# # # 标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
# encodeStr2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print(encodeStr2)
# encodeStr2Urlsafe = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print(encodeStr2Urlsafe)


# 练习
# 写一个能处理去掉=的base64解码函数：
import base64, re


# 思路一，根据传入参数s 是bytes还是str进行判断
# 思路二，根据传入参数s 有无=号进行判断
#   if type(s) == bytes:
#       s.decode()
def safe_base64_decode(s):
    print('s :', s, 'type :', type(s))
    # 如果 s 是bytes类型，无论有无=号，解码
    if type(s) == bytes:
        str = s.decode()
        str += '=='
    # 如果 s 是字符串，无论有无=号，都给你加上两个=号
    else:
        str = s
        str += '=='
    decodeStr = base64.b64decode(str)
    print(decodeStr)
    return decodeStr


# 测试
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# print('ok')
# safe_base64_decode(b'YWJjZA==')
# safe_base64_decode('YWJjZA==')
# safe_base64_decode(b'YWJjZA')
# safe_base64_decode('YWJjZA')

print('# struct')
import struct
# # help(struct)
# pack : 相应的数据类型--->bytes
# print(struct.pack('>I', 10240099))
# unpack :bytes--->相应的数据类型
# I:unsigned int; H:unsigned short;
# '>IH' 后面的bytes依次变为I：4字节无符号整数、H：2字节无符号整数
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# 用struct分析位图文件（.bmp）
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# print(struct.unpack('<ccIIIIIIHH', s))

# 练习
# 编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


def bmp_info(data):
    print('data :', data)
    result = struct.unpack('<ccIIIIIIHH', data[0:30])
    print('result ', result)
    return {
        'width': result[6],
        'height': result[7],
        'color': result[9]
    }


# # 测试
# bi = bmp_info(bmp_data)
# assert bi['width'] == 28
# assert bi['height'] == 10
# assert bi['color'] == 16
# print('ok')

# 通过读取文件来获取文件的信息
import struct


def image_info(image_path):
    with open(image_path, 'rb') as file:
        image_header = file.read(30)
        image_info = struct.unpack('<ccIIIIIIHH', image_header)
        return {
            'size': image_info[2],
            'width': image_info[6],
            'height': image_info[7],
            'color': image_info[9]
        }


file_paths = (
    r"C:\Users\Daemon\Desktop\test_0.bmp",
    r"C:\Users\Daemon\Desktop\test_16.bmp",
    r"C:\Users\Daemon\Desktop\test_256.bmp",
    r"C:\Users\Daemon\Desktop\test_24.bmp"
)
# for file_path in file_paths:
#     print(file_path, '\t', image_info(file_path))

print('# hashlib')
# import hashlib
#
# md5 = hashlib.md5()
# test = 'how to use md5 in python hashlib?'.encode('utf-8')
# print(test)
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print('md5.digest() :', md5.digest())
# print('md5.hexdigest() :', md5.hexdigest())
#
# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print('sha1.hexdigest() :', sha1.hexdigest())

# print('-------# 练习------')

#
# # 练习
# # 根据用户输入的口令，计算出存储在数据库中的MD5口令：
# # 用户输入的口令--->计算MD5口令
# # 计算的MD5口令 == 数据库中存储的MD5口令 ?
# def calc_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     return md5.hexdigest()
#
#
# # db = {
# #     'michael': 'e10adc3949ba59abbe56e057f20f883e',
# #     'bob': '878ef96e86145580c38c87f0410ad153',
# #     'alice': '99b1c2188db85afee403b1536010c2c9'
# # }
#
#
# def login(user, password):
#     try:
#         if db[user] == calc_md5(password):
#             return True
#         else:
#             return False
#     except KeyError as e:
#         print('KeyError :', e)
#
#
# # 测试:
# # assert login('michael', '12345655') 口令填写错误，Python有的时候识别不到assert错误
# # assert login('michael', '123456')
# # assert login('bob', 'abc999')
# # assert login('alice', 'alice2008')
# # assert not login('michael', '1234567')
# # assert not login('bob', '123456')
# # assert not login('alice', 'Alice2008')
# # assert not login('alice', 'Alice2008')
# # print('ok')
#
# # 练习
# # 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
# db = {}
#
#
# def register(username, password):
#     print('---register start---')
#     db[username] = User(username, password)
#     # db[username] = get_md5(password + username + 'the-Salt')
#     print('---register end---')
#
#
# # 然后，根据修改后的MD5算法实现用户登录的验证：
# import hashlib, random
#
#
# def get_md5(s):
#     return hashlib.md5(s.encode('utf-8')).hexdigest()
#
#
# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = get_md5(password + self.salt)
#
#
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
#     }
#
#
# def login(username, password):
#     print('---login start---')
#     user = db[username]
#     print('login()--->user :', user.__dict__)
#     print('---login end---')
#     return user.password == get_md5(password + user.salt)
#
#
# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# register('daemon', '123456')
# print('register after db is :', db)
# assert login('daemon', '123456')

print('# hmac')
# import hmac
# message = b'Hello, world!'
# key = b'secret'
# # new()传入的key, massage都是bytes类型,str类型需要首先编码为bytes.
# # new() :Create a new hashing object and return it.
# h = hmac.new(key, message, digestmod='MD5')
# # 如果消息很长，可以多次调用h.update(msg)
# print(h.hexdigest())

# print('# Exercise')
# import hmac, random
#
#
# def hmac_md5(key, s):
#     print('hmac_md5 return :', hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest())
#     return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()
#
#
# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = hmac_md5(self.key, password)
#
#
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
#
#
# def login(username, password):
#     user = db[username]
#     return user.password == hmac_md5(user.key, password)
#
#
# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

print('# itertools')
# import itertools
# # count()创建一个无限的迭代器
# natuals = itertools.count(1)    # 将1赋给start
# for n in natuals:
#     print(n)

# # cycle() 会把传入的一个序列无限重复下去；# Then repeat the sequence indefinitely. 无限期地重复该序列
# cs = itertools.cycle('ABC') # str也是序列的一种
# for c in cs:
#     print(c)

# # repeat(object [,times]) :create an iterator which returns the object for the specified number of times.
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

# # 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列。
# """
# takewhile(predicate谓语, iterable) --> takewhile object
#
# Return successive连续的 entries条目 from an iterable as long as只要 the
# predicate evaluates评定 to true for each entry.
# """
# natuals = itertools.count(1)                            # count()创建一个无限的迭代器
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))
# ns = itertools.takewhile(lambda x: x % 2 != 0, natuals)  # 我以为ns将会变成[1, 3, 5, 7, 9, ...]，然而结果却是[1]
# print(list(ns))

# # chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
# 只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
# """
# groupby(iterable[, keyfunc]) -> create an iterator which returns
# (key, sub-iterator) grouped by each value of key(value).
# """
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))

# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print(key, list(group))


# Exercise
# 计算圆周率可以根据公式：
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
# import math


# def indexFunc(i):
#         if i % 2 == 0:    # 如果i是偶数，返回1
#             # print(1)
#             return 1
#         else:
#             # print(-1)
#             return -1   # 如果i是奇数，返回-1
#
#
# def pi0(N):
#     # ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     natuals = itertools.count(start=1, step=2)
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     ns = itertools.takewhile(lambda x: x <= N, natuals)
#     # 因为ns 是 itertools.takewhile类型的对象，不能用于ns[i]这种写法，所以将ns 赋值给ts
#     ts = list(ns)
#     print('ts :', list(ts))
#     singleResult = 0.0
#     sumResult = 0
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     for i in range(len(ts)):
#         root = indexFunc(i)
#         singleResult = root * 4 / ts[i]
#         # step 4: 求和:
#         sumResult += singleResult
#
#     print('singleResult : ', singleResult)
#     print('{1:.2f}%'.format(singleResult))
#     print('sumResult :', sumResult)
#     # return 3.14
#     return sumResult
#
#
# def pi1(N):
#     oddNum = itertools.count(1, 2)
#     oddNum_N = itertools.takewhile(lambda x: x < (2*N), oddNum)
#     divisor = itertools.cycle([4, -4])
#     sum = 0
#     for d, n in zip(divisor, oddNum_N):
#         sum += d / n
#     return sum
#
#
# def pi(N):
#     result = 0
#     j = 0
#     natuals = itertools.count(start=1, step=2)
#     ns = itertools.takewhile(lambda x: x <= 2*N-1, natuals)
#     for i in ns:
#         result = result + pow(-1, j)*4/i
#         j += 1
#     return result

# # 测试:
# print(pi(10))
# print(pi(100))
# print(pi(1000))
# print(pi(10000))
# assert 3.04 < pi(10) < 3.05
# assert 3.13 < pi(100) < 3.14
# assert 3.140 < pi(1000) < 3.141
# assert 3.1414 < pi(10000) < 3.1415
# print('ok')

print('# contextlib')


# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin...')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print('Error...')
#         else:
#             print('End...')
#
#     def query(self):
#         print('Query info about %s ...' % self.name)


# with Query('Bob') as q:
#     q.query()


# from contextlib import contextmanager
#
#
# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print('Query info about %s ...' % self.name)
#
#
# @contextmanager
# def create_query(name):
#     print('Begin...')
#     q = Query(name)
#     yield q
#     print('End ...')
#
#
# # @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
# with create_query('Daemon') as q:
#     q.query()


# @contextmanager
# def tag(name):
#     print('<%s>' % name)
#     yield
#     print('</%s>' % name)
#
#
# with tag('h1'):
#     print('hello')
#     print('world')

# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
# closing也是一个经过@contextmanager装饰的generator
# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('https://www.python.org')) as page:
#     print('print line ...')
#     for line in page:
#         print(line)
#
#
# @contextmanager
# def closing(thing):
#     try:
#         print('run thing...')
#         yield thing
#     finally:
#         print('run over...')
#         thing.close()


print('# urllib')

# # 对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：
# # f.gethdeaders() :Return list of (header, value) tuples.
# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))


# # 模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
# from urllib import request
#
# req = request.Request('https://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status :', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s : %s' % (k, v))
#     print('Data :', data.decode('utf-8'))


# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入
# parse(解析)
# from urllib import request, parse
#
# print('Login to weibo.cn...')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# # request.urlopen((url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, *, cafile=None, capath=None, cadefault=False, context=None)
# # url, which can be either a string or a Request object. url是字符串或者一个Request对象
# # *data* must be an object specifying additional data to be sent to the server. data必须是一个对象，这个对象要确定发送给服务器的其他数据
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     data = f.read()
#     print('Status :', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s : %s ' % (k, v))
#     print('Data :', data.decode('utf-8'))

# 这个练习没做
# # 利用urllib读取JSON，然后将JSON解析为Python对象：
# from urllib import request
# import json
#
#
# def fetch_data(url):
#     with request.urlopen(url) as f:
#         urldata = f.read().decode('utf-8')
#         return json.loads(urldata)
#
#
# # 测试
# # URL = 'https://api.douban.com/v2/book/2129650'
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
# data = fetch_data(URL)
# print(data)
# # assert data['query']['results']['channel']['location']['city'] == 'Beijing'
# # print('ok')

print('# XML')

from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax : start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax : end_element: %s' % name)

    def char_data(self, text):
        print('sax : char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol name="my is ol name">我是ol
    <li>我是li_1<a href="/python">Python</a></li>
    <li>我是li_2<a href="/ruby">Ruby</a></li>    
</ol>
'''

# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)
# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。


# # 生成XML
# def createXML():
#     L = []
#     L.append(r'<?xml version"1.0"?>')
#     L.append(r'<root>')
#     # L.append(encode('some % data'))
#     L.append('some % data')
#     L.append(r'</root>')
#     # join作用：S.join(iterable) -> str
#     return ''.join(L)
#
#
# var = createXML()
# print(var)


# # 抓取聚合-天气预报
# from urllib import parse, request
#
# textmod = {
#     'cityname': '长春',
#     'dtype': 'json',
#     'format': 1,
#      'key': '47f9c593c92ab6ef83eb54372ff65a53'
# }
# # 如果 'cityname': '长春::--//'    : /都会被编码，-不会
# textmod = parse.urlencode(textmod)
# print('request parameter :', textmod)
# header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
# url = 'http://v.juhe.cn/weather/index'
# req = request.Request(url='%s%s%s' % (url, '?', textmod), headers=header_dict)
# res = request.urlopen(req, timeout=5)
# data = res.read()
# print(data.decode('utf-8'))

print('# HTMLParser')

# from html.parser import HTMLParser
#
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s:' % name)
#
#     def handle_charref(self, name):
#         print('&#%s:' % name)
#
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

# 练习没有做

print('---------------------常用第三方模块----------')
print('# Pillow')

# # 图片缩放、更改后缀名、模糊处理
# from PIL import Image
# from PIL import ImageFilter
#
#
# # open .jpg，当前路径
# im = Image.open('伊涅斯塔.jpg')
# # width, height
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # # 缩放到50%
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w // 2, h // 2))
# # 把缩放后的图像用jpeg格式保存
# im.save('伊涅斯塔thumbnail.jpg', 'jpeg')
# # 模糊处理
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('伊涅斯坦blur.jpg', 'jpeg')


# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
#
# import random
#
#
# # 随机字母
# def rndChar():
#     return chr(random.randint(65, 90))
#
#
# # 随机颜色
# def rndColor():
#     return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)
#
#
# # 随机颜色2
# def rndColor2():
#     return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)
#
#
# # 240 * 60
# width = 60 * 4
# height = 60
# # new(mode, size, color=0) : Creates a new image with the given mode and size.
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象（字形）
# font = ImageFont.truetype('arial.ttf', 36)
# # 创建Draw对象
# # Draw(im, mode=None):  A simple 2D drawing interface for PIL images.
# draw = ImageDraw.Draw(image)
# # 填充每个像素
# for x in range(width):
#     for y in range(height):
#         # point(self, xy, fill=None):  Draw one or more individual pixels. 绘制一个或多个单个像素
#         draw.point((x, y), fill=rndColor())
# # 输出文字
# for t in range(4):
#     # text(self, xy, text, fill=None, font=None, anchor=None,
#     #              *args, **kwargs):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊
# # filter(self, filter):   Filters this image using the given filter.  使用给定的过滤器过滤此图像
# image = image.filter(ImageFilter.BLUR)
# # save(self, fp, format=None, **params):  Saves this image under the given filename.  将此图像保存在给定的文件名下
# image.save('code.jpg', 'jpeg')  # fp='code.jpg', format='jpeg'

print('# use requests')

# # 通过GET访问一个URL
# import requests
# r = requests.get('https://douban.com/')
# print(r.status_code)
# print(r.text)


# # 通过GET访问一个带参数的URL
# import requests
#
# headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
# url = 'http://v.juhe.cn/weather/index'
# params = {
#     'cityname': '长春',
#     'dtype': 'json',
#     'format': 1,
#     'key': '47f9c593c92ab6ef83eb54372ff65a53'
# }
# res = requests.get(url, params=params, headers=headers)
# print('url :', res.url)
# print('text :', res.text)
# # requests自动检测编码
# print('encoding :', res.encoding)
# # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
# print('content :', res.content)
# # 直接获取JSON
# print('json :', res.json())

# # 发送POST请求-登录豆瓣
# import requests
# postUrl = 'https://accounts.douban.com/login'
# login_data = {
#     'form_email': 'abc@xeample.com',
#     'form_password': '123456'
# }
# req = requests.post(postUrl, data=login_data)
# print('req status_code :', req.status_code)
# print('req headers :', req.headers)
# print('req encoding :', req.encoding)
# print(req.text)


# 发送POST请求-登录新浪微博
# import requests
# import chardet
#
# postUrl = 'https://weibo.com/?topnav=1&mod=logo#_loginLayer_1542372000354'
# login_data = {
#     'username': '1531534205',
#     'password': 'FanLiang520.wei'
# }
# req = requests.post(postUrl, data=login_data)
# print('status_code :', req.status_code)
# print('headers :', req.headers)
# print('req encoding :', req.encoding)
# print('req text :', req.text)


# # chardet: GBK 编码------经试验，和字数有关系，字数越多越容易识别出来
# import chardet
# data = '天王盖地虎,小鸡炖蘑菇,宝塔镇河妖'.encode('GBK')
# print(chardet.detect(data))

print('# psutil')

# # 获取CPU信息
# import psutil
#
# print('cpu_count :', psutil.cpu_count(logical=False))
# print('cpu_times :', psutil.test())