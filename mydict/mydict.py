# 单元测试
class Dict(dict):

    # **kw 是关键字参数;
    # 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict(key-value)
    def __init__(self, **kw):
        super().__init__(**kw)

    # __getattr__()作用：调用类的方法或属性时，如果不存在，动态返回一个属性/函数；
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value