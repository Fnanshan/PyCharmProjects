from functools import reduce


def str2num(s):
    # 直接 return int(s)，报错：ValueError: invalid literal for int() with base 10: ' 7.6'
    try:
        return int(s)
    except ValueError as e:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    print(ss)
    ns = map(str2num, ss)
    print(ns)
    print('ns type :', type(ns))
    # print('list(ns) :', list(ns))
    # print('list(ns) type :', type(list(ns)))
    print('ns type :', type(ns))
    # 正常来说，没有 print(list(ns)) 的话，reduce(functions, ns) 不会报错
    # 因为list(iterable) -> new list initialized from iterable's items，我猜测，list(ns)是一个新的对象，不是原来的ns了
    return reduce(lambda acc, x: acc + x, list(ns))


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()