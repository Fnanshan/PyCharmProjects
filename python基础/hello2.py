#!/usr/bin/env python3 　　　　　　　　　　　　　　　　# 让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-　　　　　　　　　　　　　　　　# 使用标准UTF-8编码

' a test module '   # 任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Michael Liao' # 源码作者

import sys  # 导入sys模块后，我们就有了变量sys指向该模块


def test():
    args = sys.argv # argv变量，用list存储了命令行的所有参数。argv至少有一个元素，第一个参数永远是该.py文件的名称
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__=='__main__':
    test()
    print('__name__ is :', __name__, '---', '__author__ is :', __author__)

# 在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
