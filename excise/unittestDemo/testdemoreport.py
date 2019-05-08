import unittest
import requests
import os, time,sys
from HTMLTestRunner import HTMLTestRunner
from mathcaculate import *


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这是测试整个类前要执行的方法")

    def setUp(self):
        print("这是每一个测试方法前面运行的方法")

    def tearDown(self):
        print("这是每一个测试方法后面运行的方法")

    def test_first(self):
        print("这是测试方法1-进行接口测试demo")
        # 这是利用requests第三方库（进行发请求，收响应）向百度发个get请求
        res = requests.get('http://www.baidu.com')
        # 这是输出返回结果
        print(res.text)

    def test_second(self):
        print("这是测试方法2-研究一下python的断言")
        assert 1 == 1
        assert {'name': 'linda', 'age': 18} == {'name': 'linda', 'age': 188}
        a = 'hello'
        age = 35
        assert a in 'hello world'
        assert 20 < age < 80
        print("这是测试方法2-研究一下unittest的断言")
        self.assertGreater(1, 2, '这是不可能的')
        self.assertIn(a, ' world', msg='没有hello呀')

    def test_third(self):
        print("这是测试方法3-单元测试-测试开发写的计算器的代码功能是否能实现")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))
        self.assertEqual(1, minus(3, 2))
        self.assertEqual(6, multi(3, 2))
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2, divide(5, 2))

    @classmethod
    def tearDownClass(cls):
        print("这是测试整个类后要执行的方法")


if __name__ == '__main__':
    sys.path.append('/Users/lindafang/PycharmProjects/testframework/unittestDemo')
    # 设置报告的路径
    report_path = os.path.join(os.path.dirname(__file__), 'report')
    # 通过当前时间命名报告
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = report_path + "/" + now + "_result.html"
    # 建立一个套件-就是可以装多个用例
    suite = unittest.TestSuite()
    # 在这个套件中添加测试用例（可能通过类名,模块名等加载，这次用类名）
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClass))
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='测试用例')
        runner.run(suite)


