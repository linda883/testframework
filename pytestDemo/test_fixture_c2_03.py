import pytest


def test_s4(login):
    print('用例4，登陆后执行其它功能操作4c4')


def test_s5():
    print('用例5，不登陆后执行其它功能操作c5')


def test_s6(login):
    print('用例5，登陆后执行其它功能操作c6')


if __name__ == '__main__':
    pytest.main()
