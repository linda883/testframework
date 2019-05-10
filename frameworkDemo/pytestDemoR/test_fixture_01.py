import pytest


@pytest.fixture()
def open_browser():
    print("\n打开浏览器，打开百度首页")

    yield

    print('执行teardown')
    print('最后关闭浏览器')


@pytest.mark.usefixtures('open_browser')
def test_soso():
    print('case1: 登际后执行搜索')


def test_cakan():
    print('case2:不登陆就看')


@pytest.mark.usefixtures('open_browser')
def test_cart():
    print('case3,登陆，加购物车')


if __name__ == '__main__':
    pytest.main(['-s','test_fixture.py'])

