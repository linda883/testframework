import unittest


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这是测试整个类前要执行的方法")

    def setUp(self):
        print("这是每一个测试方法前面运行的方法，准备数据")

    def tearDown(self):
        print("这是每一个测试方法后面运行的方法")

    def test_one(self):
        print('测试方法1')
        assert 1 == 1
        self.assertIn('l', 'hello')

    def test_sencond(self):
        print('测试方法2')
        assert 1 != 1
        self.assertIn('l', 'hello')

    @classmethod
    def tearDownClass(cls):
        print("这是测试整个类后要执行的方法")


if __name__ == '__main__':
    unittest.main(verbosity=2)

