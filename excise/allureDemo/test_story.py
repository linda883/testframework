import pytest
import allure


@allure.feature('购物车功能')  # feature定义功能
class TestShoppingTrolley(object):
    @allure.story('加入购物车')  # story定义用户场景
    def test_add_shopping_trolley(self):
        login('linda', '88888')  # 调用“步骤函数”
        with allure.step("浏览商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤2
            allure.attach('商品1', '三星')  # attach可以打印一些附加信息
            allure.attach('商品2', 'linda')
        with allure.step("点击商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤3
            pass
        with allure.step("校验结果"):
            allure.attach('期望结果', '添加购物车成功')
            allure.attach('实际结果', '添加购物车失败')
            assert 'success' != 'failed'

    @allure.story('修改购物车')
    def test_edit_shopping_trolley(self):
        pass

    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('删除购物车')
    def test_delete_shopping_trolley(self):
        pass


@allure.step('用户登录')  # 还可以将一个函数作为一个步骤，调用此函数时，报告中输出一个步骤，步骤名字通常是函数名，我把这样的函数叫“步骤函数”
def login(user, pwd):
    print(user, pwd)


if __name__ == '__main__':
    pytest.main(["--allure_features='购物车功能' --allure_stories='加入购物车"])
