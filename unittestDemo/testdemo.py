import unittest


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这是测试整个类前要执行的方法")

    def setUp(self):
        print("这是每一个测试方法前面运行的方法")

    def tearDown(self):
        print("这是每一个测试方法后面运行的方法")

    def test_first(self):
        print("这是测试方法1")

    # @unittest.skip("这次不想执行这个测试")
    def test_second(self):
        print("这是测试方法2")
        assert 1 == 1
        assert 1 != 1

    @classmethod
    def tearDownClass(cls):
        print("这是测试整个类后要执行的方法")


if __name__ == '__main__':
    unittest.main(verbosity=2)

