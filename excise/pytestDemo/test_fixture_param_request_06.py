# 参数化与数据驱动相同
# 可以使用fixture中的params进行数据驱动，执行多次
import pytest


@pytest.fixture(params=[1, 2, 3, 'linda'])
def test_data(request):
    return request.param


def test_one(test_data):
    print('\ntest data: %s' % test_data)

