# regularExpression
'''
\d  匹配一个数字
\w  匹配一个字母或数字
\s  可以匹配一个空格（也包括Tab等空白符）
\s+ 表示至少有一个空格
.   匹配任意字符（数字、字母、符号）
*   表示任意个字符（包括0个）
+   表示至少一个字符
?   表示0个或1个字符
{n} 表示n个字符
    \d{3}表示匹配3个数字
{n,m}表示n-m个字符
    \d{3,8}表示3-8个数字
'''

# 进阶
'''
[]  表示范围
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线
[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束
'''



# re模块
# Python的字符串本身也用\转义；Python的r前缀，就不用考虑转义的问题
s = 'ABC\\-001'
print(s)
s1 = r'ABC\-001'
print(s1)

import re
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
# 常用的判断方法
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 用空格切分字符串
re.split(r'\s+', 'a b   c')
# ['a', 'b', 'c']
re.split(r'[\s\,]+', 'a,b, c   d')
# ['a', 'b', 'c', 'd']
re.split(r'[\s\,\;]+', 'a,b;;  c    d')
# ['a', 'b', 'c', 'd']

# 分组-Group
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group())
# group(0)永远是原始字符串
print(m.group(0))
# group(1)第1个字符串
print(m.group(1))
print(m.group(2))
# 提取字符串2
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 匹配出数字后面的0:
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# 让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 编译-Compile
# Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。
import re
# Compile
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# use
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

print('---------练习-----------')
# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#   someone@gmail.com
#   bill.gates@microsoft.com
import re


def is_valid_email(addr):
    # re_email = re.compile(r'^[a-zA-Z0-9-]+@[a-zA-Z0-9-]+(.[a-zA-Z0-9-]+)+$')
    if re.match(r'^([a-zA-Z0-9.]{0,13})\@.([a-z]{0,3})$', str(addr)):
        print(addr)
        return True
    else:
        print('input error!')
        return False


assert is_valid_email('someone@gmial.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')