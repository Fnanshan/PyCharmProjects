# 编写单元测试，需要引入Python自带的unittest模块
import unittest

# from A import B : 从A中引入B，相当于 import A, b= A.b
from mydict.mydict import Dict


# 编写测试类，从unittest.TestCase继承
# self.assertEqual(abs(-1), 1)  # 断言函数返回的结果与1相等
# self.assertRaises(KeyError)   # 断言抛出KeyError
class TestDict(unittest.TestCase):

    # setUp()/setDown()分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')

        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 运行单元测试最简单的方式
if __name__ == '__main__':
    unittest.main()