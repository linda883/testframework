import pytest


@pytest.fixture()
def start():
    print("\n----begin-登陆--")


def test_soso():
    print('\ncase1: 登际后执行搜索')


def test_cakan():
    print('\ncase2:不登陆就看')


def test_cart():
    print('\ncase3,登陆，加购物车')


def test_quit():
    print('case3,登陆，退出')
