import pytest
import sys
# scope=function


def test_soso(login):
    print('case1: 登际后执行搜索')
    assert 1 == 1
    assert {'name': 'linda', 'age': 18} == {'name': 'linda', 'age': 188}
    a = 'hello'
    age = 35
    assert a in 'hello world'
    assert 20 < age < 80


def f():
    return 3


@pytest.mark.skip
def test_cakan():
    print('case2:不登陆就看')
    assert f() == 4


environment = 'android'


@pytest.mark.skipif('environment=="android"', reason='android平台没有这个功能')
def test_cart_3(login):
    print('case3,登陆，点击苹果图标')


@pytest.mark.skipif(sys.platform =='win32', reason='不在windows下运行')
@pytest.mark.skipif(sys.version_info < (3,6), reason='3.6版本以下不执行，您需要更高版本')
def test_cart(login):
    print('case3,登陆，点击苹果图标，3.6以下版本无法执行')


@pytest.mark.xfail
def test_xfail():
    print(broken_fixture())


def broken_fixture():
    raise Exception("Sorry, it's 中断异常.")

