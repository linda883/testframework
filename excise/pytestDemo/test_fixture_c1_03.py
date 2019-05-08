import pytest


def test_s1(login):
    print('用例1，登陆后执行其它功能操作c1')


def test_s2():
    print('用例2，不登陆后执行其它功能操作c2')


def test_s3(login):
    print('用例3，登陆后执行其它功能操作c3')


if __name__ == '__main__':
    pytest.main()
