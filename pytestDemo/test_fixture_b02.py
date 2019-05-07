import pytest


# 不带参数时scope="function"
# 有个依赖关系的可能通过fixture实现。
@pytest.fixture()
def login():
    print("\n输入用户名密码登陆！")


def test_cart(login):
    print('用例1，登陆后执行添加购物车功能操作')


def test_search():
    print('用例2，不登陆查询功能操作')


def test_pay(login):
    print('用例3，登陆后执行支付功能操作')


if __name__ == '__main__':
    # pytest.main()
    pytest.main(['-s', 'test_fixture_b02.py'])
