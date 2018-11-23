print('--------debug---------')


# # assert
# # 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
# def foo(s):
#     n = int(s)
#     # 表达式n != 0应该是True；断言失败，assert语句抛出AssertionError
#     assert n != 0, 'n is zero'
#     return 10 / n
#
#
# def main():
#     foo('0')
#
#
# main()


# # logging
# # logging不会抛出错误，而且可以输出到文件
# import logging
# # 记录信息的级别： DEBUG/INFO/WARNING/ERROR
# logging.basicConfig(level=logging.INFO)
#
# s = '0'
# n = int(s)
# # logging.info()输出一段文本
# logging.info('n = %d' % n)
# print(10 / n)


# pdb（python的调试器，让程序以单步方式运行，可以随时查看运行状态）
# s= '0'
# n = int(s)
# print(10 / n)

print('----------unit test--------')
# import mydict
# d = mydict.Dict(a=1, b=2)
# print(d)
# print(d['a'])
# print(d.a)
print('---------document test---------')
import re
m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))
