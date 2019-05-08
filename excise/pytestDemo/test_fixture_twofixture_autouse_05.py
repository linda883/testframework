import pytest


# fixture可以嵌套使用
# autouse=True 不用要测试方法中传参调用，默认全使用，如果想某个模块不使用就要显示声明
@pytest.fixture(autouse=True)
def login(open_browser):
    print('这是个登陆模块！')


@pytest.fixture()
def open_browser():
    print('打开首页！')


def test_soso():
    print('case1: 登际后执行搜索')


def test_cakan():
    print('case2:不登陆就看')


def test_cart():
    print('case3,登陆，加购物车')

