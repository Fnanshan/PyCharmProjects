# -*- coding: GBK -*-
print('-------------datetime------------')
from datetime import datetime

print('# ��ǰ���ں�ʱ��')
# ��ǰ���ں�ʱ��
# now = datetime.now()
# print(now)
# print(type(now))

print('# ָ�����ں�ʱ��')
# ָ�����ں�ʱ��
# dt = datetime(1970, 1, 3, 0, 0)
# print(dt)

print('# datetime ת��Ϊ timestamp��ʱ�����--- timestamp()')
# datetime ת��Ϊ timestamp��ʱ�����
# epoch time����Ԫʱ�䣩=0: 1970��1��1�� 00:00:00 UTC+00:00ʱ����ʱ��
# ��ǰʱ����������epoch time����������Ϊtimestamp��ʱ�����
# timestamp��һ���������������С��λ��С��λ��ʾ��������
# print(now)
# print(now.timestamp())

print('# timestamp ת��Ϊ datetime --- fromtimestamp()')
# timestamp ת��Ϊ datetime
# ע�⵽timestamp��һ������������û��ʱ���ĸ����datetime����ʱ���ġ�����ת������timestamp�ͱ���ʱ�䣨��ǰ����ϵͳ�趨��ʱ������ת����
# t = 1541753943.510553
# print(datetime.fromtimestamp(t))
# # �������α�׼ʱ���뱱��ʱ�����8Сʱ
# print(datetime.utcfromtimestamp(t))

print('# str ת��Ϊdatetime ---- datetime.strptime()')
# str ת��Ϊdatetime��ת�����datetime��û��ʱ����Ϣ�ġ�
# str = '2015-5-12 18:29:59'
# toDatetimeFormat = '%Y-%m-%d %H:%M:%S'
# cday = datetime.strptime(str, toDatetimeFormat)
# print(cday)

print('# datetime ת��Ϊ str ---- strftime()')
# datetime ת��Ϊ str
# toStrFormat = '%a, %b %d %H:%M'
# print(now.strftime(toStrFormat))

print('# datetime�Ӽ� ---- timedelta class')
# datetime�Ӽ�
# from datetime import datetime, timedelta
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))
# print(now + timedelta(days=2, hours=12))

print('# ����ʱ��ת��ΪUTCʱ�� --- tzinfo property')
# ����ʱ��ת��ΪUTCʱ��
# ����ʱ����ָϵͳ�趨ʱ����ʱ�䣬���籱��ʱ����UTC+8:00ʱ����ʱ�䣬��UTCʱ��ָUTC+0:00ʱ����ʱ�䡣
# һ��datetime������һ��ʱ������tzinfo������Ĭ��ΪNone�������޷��������datetime�������ĸ�ʱ��������ǿ�и�datetime����һ��ʱ��
# from datetime import datetime, timedelta, timezone
# now = datetime.now()
# tz_utc_8 = timezone(timedelta(hours=8))  # ����ʱ��UTC+8:00
# dt = now.replace(tzinfo=tz_utc_8)  # ǿ������ΪUTC+8:00
# print('now :', now, ' type :', type(now))
# print('tz_utc_8 :', tz_utc_8, ' type :', type(tz_utc_8))
# print('dt :', dt, ' type :', type(dt))


print('# ʱ��ת�� --- utcnow() --- astimezone()')
# ʱ��ת��
# ��ͨ��utcnow()�õ���ǰ��UTCʱ�䣬����astimezone()ת��Ϊ����ʱ����ʱ�䣺
# from datetime import datetime, timedelta, timezone
# # �õ�UTCʱ�䣬��ǿ������ʱ��ΪUTC+0:00
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print('utc_dt :', utc_dt)
# # astimezone()��ת��ʱ��Ϊ����ʱ��
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print('bj_dt :', bj_dt)
# # astimezone()��ת��ʱ��Ϊ����ʱ��
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print('tokyo_dt :', tokyo_dt)
# # astimezone()��bj_btת��ʱ��Ϊtokyo_dt
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print('tokyo_dt2 :', tokyo_dt2)

# summary
# datetime��ʾ��ʱ����Ҫʱ����Ϣ����ȷ��һ���ض���ʱ�䣬����ֻ����Ϊ����ʱ�䡣
# ���Ҫ�洢datetime����ѷ����ǽ���ת��Ϊtimestamp�ٴ洢����Ϊtimestamp��ֵ��ʱ����ȫ�޹ء�

print('# ��ϰ')
# ��ϰ
# �������ȡ���û���������ں�ʱ����2015-1-21 9:01:30���Լ�һ��ʱ����Ϣ��UTC+5:00������str�����дһ����������ת��Ϊtimestamp
# ˼·�� 1.str -> datetime��
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
#     tz_utc_some = timezone(timedelta(hours=tz_str2))  # ����ʱ��UTC+8:00
#     dt = cday.replace(tzinfo=tz_utc_some)  # ǿ������ΪUTC+8:00
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
# # namedtuple('����', [����list]):
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x)
# print(p.y)

print('# deque')
# deque��Ϊ�˸�Чʵ�ֲ����ɾ��������˫���б��ʺ����ڶ��к�ջ
# deque����ʵ��list��append()��pop()�⣬��֧��appendleft()��popleft()�������Ϳ��Էǳ���Ч����ͷ����ӻ�ɾ��Ԫ��
# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)

print('# defaultdict')
# ʹ��dictʱ��������õ�Key�����ڣ��ͻ��׳�KeyError�����ϣ��key������ʱ������һ��Ĭ��ֵ��
# Ĭ��ֵ�ǵ��ú������صģ��������ڴ���defaultdict����ʱ���롣
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


# OrderedDict����ʵ��һ��FIFO���Ƚ��ȳ�����dict����������������ʱ����ɾ��������ӵ�Key
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
# # ChainMap���԰�һ��dict�����������һ���߼��ϵ�dict��ChainMap����Ҳ��һ��dict�����ǲ��ҵ�ʱ�򣬻ᰴ��˳�����ڲ���dict���β��ҡ�
# from collections import ChainMap
# import os, argparse
#
# # ����ȱʡ����
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }
#
# # ���������в���
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k: v for k, v in vars(namespace).items() if v}
#
# # ��ϳ�ChainMap
# combined = ChainMap(command_line_args, os.environ, defaults)
#
# # pring arguments
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])

print('# Counter')
# # Counterʵ����Ҳ��dict��һ�����࣬����Ľ�����Կ������ַ�'g'��'m'��'r'�����������Σ������ַ���������һ�Ρ�
# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)

print('# base64')
# # # base64����ֱ�ӽ���base64�ı����
# import base64
# encodeStr = base64.b64encode(b'binary\x00string')
# print(encodeStr)
# decodeStr = base64.b64decode(b'YmluYXJ5AHN0cmluZw====')
# print(decodeStr)
# # # ��׼��Base64�������ܳ����ַ�+��/����URL�оͲ���ֱ����Ϊ��������������һ��"url safe"��base64���룬��ʵ���ǰ��ַ�+��/�ֱ���-��_
# encodeStr2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print(encodeStr2)
# encodeStr2Urlsafe = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print(encodeStr2Urlsafe)


# ��ϰ
# дһ���ܴ���ȥ��=��base64���뺯����
import base64, re


# ˼·һ�����ݴ������s ��bytes����str�����ж�
# ˼·�������ݴ������s ����=�Ž����ж�
#   if type(s) == bytes:
#       s.decode()
def safe_base64_decode(s):
    print('s :', s, 'type :', type(s))
    # ��� s ��bytes���ͣ���������=�ţ�����
    if type(s) == bytes:
        str = s.decode()
        str += '=='
    # ��� s ���ַ�������������=�ţ��������������=��
    else:
        str = s
        str += '=='
    decodeStr = base64.b64decode(str)
    print(decodeStr)
    return decodeStr


# ����
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
# pack : ��Ӧ����������--->bytes
# print(struct.pack('>I', 10240099))
# unpack :bytes--->��Ӧ����������
# I:unsigned int; H:unsigned short;
# '>IH' �����bytes���α�ΪI��4�ֽ��޷���������H��2�ֽ��޷�������
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# ��struct����λͼ�ļ���.bmp��
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# print(struct.unpack('<ccIIIIIIHH', s))

# ��ϰ
# ��дһ��bmpinfo.py�����Լ�������ļ��Ƿ���λͼ�ļ�������ǣ���ӡ��ͼƬ��С����ɫ����
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


# # ����
# bi = bmp_info(bmp_data)
# assert bi['width'] == 28
# assert bi['height'] == 10
# assert bi['color'] == 16
# print('ok')

# ͨ����ȡ�ļ�����ȡ�ļ�����Ϣ
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

# print('-------# ��ϰ------')

#
# # ��ϰ
# # �����û�����Ŀ��������洢�����ݿ��е�MD5���
# # �û�����Ŀ���--->����MD5����
# # �����MD5���� == ���ݿ��д洢��MD5���� ?
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
# # ����:
# # assert login('michael', '12345655') ������д����Python�е�ʱ��ʶ�𲻵�assert����
# # assert login('michael', '123456')
# # assert login('bob', 'abc999')
# # assert login('alice', 'alice2008')
# # assert not login('michael', '1234567')
# # assert not login('bob', '123456')
# # assert not login('alice', 'Alice2008')
# # assert not login('alice', 'Alice2008')
# # print('ok')
#
# # ��ϰ
# # �����û�����ĵ�¼���Ϳ���ģ���û�ע�ᣬ�������ȫ��MD5��
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
# # Ȼ�󣬸����޸ĺ��MD5�㷨ʵ���û���¼����֤��
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
# # ����:
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
# # new()�����key, massage����bytes����,str������Ҫ���ȱ���Ϊbytes.
# # new() :Create a new hashing object and return it.
# h = hmac.new(key, message, digestmod='MD5')
# # �����Ϣ�ܳ������Զ�ε���h.update(msg)
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
# # ����:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

print('# itertools')
# import itertools
# # count()����һ�����޵ĵ�����
# natuals = itertools.count(1)    # ��1����start
# for n in natuals:
#     print(n)

# # cycle() ��Ѵ����һ�����������ظ���ȥ��# Then repeat the sequence indefinitely. �����ڵ��ظ�������
# cs = itertools.cycle('ABC') # strҲ�����е�һ��
# for c in cs:
#     print(c)

# # repeat(object [,times]) :create an iterator which returns the object for the specified number of times.
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

# # ����������Ȼ�������޵�����ȥ������ͨ�����ǻ�ͨ��takewhile()�Ⱥ������������ж�����ȡ��һ�����޵����С�
# """
# takewhile(predicateν��, iterable) --> takewhile object
#
# Return successive������ entries��Ŀ from an iterable as long asֻҪ the
# predicate evaluates���� to true for each entry.
# """
# natuals = itertools.count(1)                            # count()����һ�����޵ĵ�����
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))
# ns = itertools.takewhile(lambda x: x % 2 != 0, natuals)  # ����Ϊns������[1, 3, 5, 7, 9, ...]��Ȼ�����ȴ��[1]
# print(list(ns))

# # chain()���԰�һ������������������γ�һ������ĵ�������
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# groupby()�ѵ����������ڵ��ظ�Ԫ������������һ��
# ֻҪ�����ں���������Ԫ�ط��ص�ֵ��ȣ�������Ԫ�ؾͱ���Ϊ����һ��ģ�����������ֵ��Ϊ���key��
# """
# groupby(iterable[, keyfunc]) -> create an iterator which returns
# (key, sub-iterator) grouped by each value of key(value).
# """
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))

# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print(key, list(group))


# Exercise
# ����Բ���ʿ��Ը��ݹ�ʽ��
# ����Python�ṩ��itertoolsģ�飬����������������е�ǰN��ͣ�
# import math


# def indexFunc(i):
#         if i % 2 == 0:    # ���i��ż��������1
#             # print(1)
#             return 1
#         else:
#             # print(-1)
#             return -1   # ���i������������-1
#
#
# def pi0(N):
#     # ' ����pi��ֵ '
#     # step 1: ����һ����������: 1, 3, 5, 7, 9, ...
#     natuals = itertools.count(start=1, step=2)
#     # step 2: ȡ�����е�ǰN��: 1, 3, 5, 7, 9, ..., 2*N-1.
#     ns = itertools.takewhile(lambda x: x <= N, natuals)
#     # ��Ϊns �� itertools.takewhile���͵Ķ��󣬲�������ns[i]����д�������Խ�ns ��ֵ��ts
#     ts = list(ns)
#     print('ts :', list(ts))
#     singleResult = 0.0
#     sumResult = 0
#     # step 3: ����������Ų���4��: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     for i in range(len(ts)):
#         root = indexFunc(i)
#         singleResult = root * 4 / ts[i]
#         # step 4: ���:
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

# # ����:
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


# ʵ�������Ĺ�����ͨ��__enter__��__exit__����������ʵ�ֵ�
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
# # @contextmanager���decorator����һ��generator����yield����with ... as var�ѱ��������ȥ��Ȼ��with���Ϳ��������ع�����
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

# ���һ������û��ʵ�������ģ����ǾͲ��ܰ�������with��䡣���ʱ�򣬿�����closing()���Ѹö����Ϊ�����Ķ���
# closingҲ��һ������@contextmanagerװ�ε�generator
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

# # �Զ����һ��URLhttps://api.douban.com/v2/book/2129650����ץȡ����������Ӧ��
# # f.gethdeaders() :Return list of (header, value) tuples.
# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))


# # ģ�����������GET���󣬾���Ҫʹ��Request����ͨ����Request�������HTTPͷ�����ǾͿ��԰�����αװ�������
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


# ���Ҫ��POST����һ������ֻ��Ҫ�Ѳ���data��bytes��ʽ���롣
# ����ģ��һ��΢����¼���ȶ�ȡ��¼������Ϳ��Ȼ����weibo.cn�ĵ�¼ҳ�ĸ�ʽ��username=xxx&password=xxx�ı��봫��
# parse(����)
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
# # url, which can be either a string or a Request object. url���ַ�������һ��Request����
# # *data* must be an object specifying additional data to be sent to the server. data������һ�������������Ҫȷ�����͸�����������������
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     data = f.read()
#     print('Status :', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s : %s ' % (k, v))
#     print('Data :', data.decode('utf-8'))

# �����ϰû��
# # ����urllib��ȡJSON��Ȼ��JSON����ΪPython����
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
# # ����
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
<ol name="my is ol name">����ol
    <li>����li_1<a href="/python">Python</a></li>
    <li>����li_2<a href="/ruby">Ruby</a></li>    
</ol>
'''

# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)
# ��Ҫע����Ƕ�ȡһ����ַ���ʱ��CharacterDataHandler���ܱ���ε��ã�������Ҫ�Լ�������������EndElementHandler�����ٺϲ���


# # ����XML
# def createXML():
#     L = []
#     L.append(r'<?xml version"1.0"?>')
#     L.append(r'<root>')
#     # L.append(encode('some % data'))
#     L.append('some % data')
#     L.append(r'</root>')
#     # join���ã�S.join(iterable) -> str
#     return ''.join(L)
#
#
# var = createXML()
# print(var)


# # ץȡ�ۺ�-����Ԥ��
# from urllib import parse, request
#
# textmod = {
#     'cityname': '����',
#     'dtype': 'json',
#     'format': 1,
#      'key': '47f9c593c92ab6ef83eb54372ff65a53'
# }
# # ��� 'cityname': '����::--//'    : /���ᱻ���룬-����
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

# ��ϰû����

print('---------------------���õ�����ģ��----------')
print('# Pillow')

# # ͼƬ���š����ĺ�׺����ģ������
# from PIL import Image
# from PIL import ImageFilter
#
#
# # open .jpg����ǰ·��
# im = Image.open('����˹��.jpg')
# # width, height
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # # ���ŵ�50%
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w // 2, h // 2))
# # �����ź��ͼ����jpeg��ʽ����
# im.save('����˹��thumbnail.jpg', 'jpeg')
# # ģ������
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('����˹̹blur.jpg', 'jpeg')


# PIL��ImageDraw�ṩ��һϵ�л�ͼ�����������ǿ���ֱ�ӻ�ͼ������Ҫ������ĸ��֤��ͼƬ
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
#
# import random
#
#
# # �����ĸ
# def rndChar():
#     return chr(random.randint(65, 90))
#
#
# # �����ɫ
# def rndColor():
#     return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)
#
#
# # �����ɫ2
# def rndColor2():
#     return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)
#
#
# # 240 * 60
# width = 60 * 4
# height = 60
# # new(mode, size, color=0) : Creates a new image with the given mode and size.
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # ����Font�������Σ�
# font = ImageFont.truetype('arial.ttf', 36)
# # ����Draw����
# # Draw(im, mode=None):  A simple 2D drawing interface for PIL images.
# draw = ImageDraw.Draw(image)
# # ���ÿ������
# for x in range(width):
#     for y in range(height):
#         # point(self, xy, fill=None):  Draw one or more individual pixels. ����һ��������������
#         draw.point((x, y), fill=rndColor())
# # �������
# for t in range(4):
#     # text(self, xy, text, fill=None, font=None, anchor=None,
#     #              *args, **kwargs):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # ģ��
# # filter(self, filter):   Filters this image using the given filter.  ʹ�ø����Ĺ��������˴�ͼ��
# image = image.filter(ImageFilter.BLUR)
# # save(self, fp, format=None, **params):  Saves this image under the given filename.  ����ͼ�񱣴��ڸ������ļ�����
# image.save('code.jpg', 'jpeg')  # fp='code.jpg', format='jpeg'

print('# use requests')

# # ͨ��GET����һ��URL
# import requests
# r = requests.get('https://douban.com/')
# print(r.status_code)
# print(r.text)


# # ͨ��GET����һ����������URL
# import requests
#
# headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
# url = 'http://v.juhe.cn/weather/index'
# params = {
#     'cityname': '����',
#     'dtype': 'json',
#     'format': 1,
#     'key': '47f9c593c92ab6ef83eb54372ff65a53'
# }
# res = requests.get(url, params=params, headers=headers)
# print('url :', res.url)
# print('text :', res.text)
# # requests�Զ�������
# print('encoding :', res.encoding)
# # ������Ӧ���ı����Ƕ��������ݣ����Ƕ�������content���Ի��bytes����
# print('content :', res.content)
# # ֱ�ӻ�ȡJSON
# print('json :', res.json())

# # ����POST����-��¼����
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


# ����POST����-��¼����΢��
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


# # chardet: GBK ����------�����飬�������й�ϵ������Խ��Խ����ʶ�����
# import chardet
# data = '�����ǵػ�,С����Ģ��,���������'.encode('GBK')
# print(chardet.detect(data))

print('# psutil')

# # ��ȡCPU��Ϣ
# import psutil
#
# print('cpu_count :', psutil.cpu_count(logical=False))
# print('cpu_times :', psutil.test())