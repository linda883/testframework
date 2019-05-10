import pytest


test_user_data = ["linda", "servenruby"]


@pytest.fixture(params=test_user_data)
def login_r(request):
    user = request.param
    print("\n打开首页准备登陆，登陆用户:%s" % user)
    return user


def test_login_s(login_r):
    print(login_r)


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture_request_06.py'])
