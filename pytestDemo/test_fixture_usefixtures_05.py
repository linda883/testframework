import pytest


@pytest.fixture(scope="function")
def start():
    print("\n----begin-登陆--")


@pytest.mark.usefixtures("start")
def test_soso():
    print('\ncase1: 登际后执行搜索')


def test_cakan():
    print('\ncase2:不登陆就看')


@pytest.mark.usefixtures("start")
def test_cart():
    print('\ncase3,登陆，加购物车')


@pytest.mark.skipif(reason="不想退出")
def test_quit():
    print('case3,登陆，退出')
