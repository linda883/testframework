import pytest


test_user_data = ["linda", "servenruby"]


@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收传入的参数，接收一个参数
    user = request.param
    print("\n打开首页准备登陆，登陆用户:%s" % user)
    return user


# 这是pytest的参数化数据驱动，indeirect=True 是把login_r当作函数去执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    # 登陆用例
    a = login_r
    print("测试用例中login的返回值：%s" % a)
    assert a != ""
