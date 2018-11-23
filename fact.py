# Python内置的“文档测试”（doctest）模块
# 可以直接提取'''注释中的代码并执行测试。


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: are error
    '''
    if n > 1:
        return n * fact(n-1)
    elif n == 1:
        return 1
    else:
        raise ValueError('are error')


if __name__ == '__main__':
    import doctest
    doctest.testmod()