import pytest

# 在整个模块(文件)只做一次的事类似setupClass，范围是模块级别的。
# yield是调用第一次返回结果，第二次执行它下面的语句返回。


@pytest.fixture(scope="module")
def open_browser():
    print("\n打开浏览器，打开百度首页")

    yield

    print('执行teardown')
    print('最后关闭浏览器')


def test_search(open_browser):
    print('用例7，搜索关键字测试执行')


def test_tieba(open_browser):
    print('用例8，进入贴吧功能')


def test_news(open_browser):
    print('用例9，进入资讯功能')


if __name__ == '__main__':
    pytest.main(['-s','test_fixture_cyeild_04.py'])
