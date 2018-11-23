print('-------文件读写--------')
# 文件使用完毕后必须关闭，即f.close()。
# 因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
# with语句自动调用close()
# with open('D:/test.txt', 'r') as f:
    # 'rb'：读取二进制
    # with open('D:/test.txt', 'rb') as f:
    # print(f.read())
    # print(f.read(2))
    # print(f.readline())
    # print(f.readlines())
    # for line in f.readlines():
    #     print(line.strip())

# fpath = r'C:\Windows\system.ini'
#
# with open(fpath, 'r') as f:
#     s = f.read()
#     print(s)

print('-----------StringIO和BytesIO-----------')

# # 把str写入StringIO
# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())

# # 读取StringIO
# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# # BytesIO
# # StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# # BytesIO实现了在内存中读写bytes
# # 写入
# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# # getvalue()用于获得写入后的str
# print(f.getvalue())
# # 读取
# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.getvalue())

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

# # 别人的一些问题: seek() / tell()的用法
# from io import StringIO
# f = StringIO()
# print('f-> ', f.tell())     # 其steam position 为0,
# f.write('Hello World')
# print('f-> ', f.tell())     # 其steam position 为11，
# print('f :', f.getvalue())  # getvalue(): Retrieve the entire contents of the object （收回对象的全部内容）
# print('f-> ', f.tell())     # 既是getvalue()之后，steam position 还是11，
# s = f.readline()
# print('s :', s)             # s为空是有道理的，f->11
# f.seek(0)                   # seek(): Change stream position.
# print('f-> ', f.tell())     # 其steam position 为0，

print('----------操作文件和目录---------')
import os

# print(os.name)  # posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
# # print(os.uname())  # uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
#
# # 环境变量
# print(os.environ)
# # 获取某个环境变量的值
# print(os.environ.get('path'))
# print(os.environ.get('x', 'default'))

# 操作文件和目录的函数在os模块、os.path模块里

# # 1.目录操作
# # 查看当前目录的绝对路径:
# print(os.path.abspath('.'))
# # 把新目录的完整路径表示出来；os.path.join()可以正确处理不同操作系统的路径分割符。
# # 在posix中，返回part-1/part-2；在nt中，返回part-1\part-2
# newPath = os.path.join('D:\GitProjects\PyCharmProjects', 'testDir3')
# # 创建一个目录
# os.mkdir(newPath)
# # 删除一个目录
# os.rmdir(newPath)
# # os.path.split() :拆分路径，后一部分是最后级别的目录或文件名
# print(os.path.split(newPath))
# # os.path.splitext() :得到文件扩展名
# print(os.path.splitext(newPath))

# # 2.文件操作
# os.rename('testNS.txt', 'testNS.py')
# os.remove('***.py')

# # 列出当前目录下的所有目录
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# # 列出所有的.py文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# # 练习
# # 利用os模块编写一个能实现dir -l输出的程序
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# waitDelDir = input(str('Please enter the name of the directory to be deleted ：'))
# try:
#     # 不用使用绝对路径就可以删除目录
#     os.rmdir(waitDelDir)
#     print('os.remdir() OK!')
# except FileNotFoundError as e:
#     print('系统找不到指定的文件。')

# 练习2
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。


def findFile(findPath='.', findType=''):
    fileList = []
    for i in os.listdir(findPath):
        # print('i :', i)
        curPath = os.path.join(findPath, i)
        if os.path.isfile(curPath):
            print('curPath :', curPath)
            if findType == '':
                fileList.append(curPath)
            elif os.path.splitext(curPath)[1][1:] == findType:
                '''
                    确保文件后缀完全匹配
                    findType = 'xls'则必须匹配到.xls，如后缀为.xlsx则不匹配
                '''
                fileList.append(curPath)
        elif os.path.isdir(curPath):
                print('isdir :', curPath)
                fileList += findFile(curPath, findType)
    return fileList


# try:
#     rst = findFile(findType='py')
#     print(rst)
# except FileNotFoundError as e:
#     print('System can not find the route.')


# # os.curdir : .
# def scanDir(path=os.curdir):
#     path = os.path.realpath(path)
#     __list = []
#     for i in os.listdir(path):
#         # 这个时候，i仅仅是文件、路径的相对名称，例如shopping/Student.py
#         i = os.path.join(path, i)
#         # @todo 查找、过滤等
#         if os.path.isdir(i):
#             __list += scanDir(i)
#         else:
#             __list.append(i)
#     return __list


# print(scanDir())
print('------------序列化-----------')
'''
pickle() Functions:
    dump(object, file)          # 把对象序列化后写入一个file-like Object
    dumps(object) -> string     # 把任意对象序列化成一个bytes
    load(file) -> object        # 从一个file-like Object中直接反序列化出对象
    loads(string) -> object     # 把一个bytes反序列化出对象
'''
# import pickle
# d = dict(name='Daemon', age=23, score=99)
# pickle.dumps(d)
# f = open('D:/test.txt', 'wb')
# pickle.dump(d, f)
# f.close()
# with open('D:/test.txt', 'rb') as f:
#     print(pickle.load(f))

# JSON
# python对象序列化为JSON
import json
d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d))

# JSON反序列化为Python对象
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))

# JSON进阶
# 用class表示对象，然后序列化
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # def __str__(self):
    #     print('name :', self.__name, ' age :', self.__age, ' score :', self.__score)
    #     return '...'
    #
    # __repr__ = __str__


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 98)
# Student对象s 不是一个可序列化为JSON的对象
# 默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数
# print(json.dumps(s, default=student2dict))
# class实例的__dict__属性用来存储实例变量
# print(json.dumps(s, default=lambda obj: obj.__dict__))
# s.__repr__()


# 反序列化class对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
