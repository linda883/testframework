import pytest
from selenium import webdriver
import time
import allure


# 利用feature之间调用，在模块层级module达到打开一次浏览器，测试执行多个测试方法
@allure.feature('打开浏览器')
@pytest.fixture(scope="module")
def driver(request):
    browser = webdriver.Chrome(
        executable_path='/Users/lindafang/PycharmProjects/testframework/excise/driver/chromedriver')

    def close_browser():
        browser.quit()

    request.addfinalizer(close_browser)
    return browser


class TestBaidu():

    @allure.feature('打开百度')
    @pytest.fixture(scope='function', autouse=True)
    def start(self,driver):
        with allure.step('step one:打开浏览器输入百度网址'):
            driver.get('http://www.baidu.com')
            time.sleep(1)

    @allure.feature('百度搜索功能')
    @allure.story('搜索验证-字母')
    def test_soso(self, driver):
        with allure.step('step two：在搜索栏输入allure,并点击百度一下'):
            driver.find_element_by_id('kw').send_keys('allure')
            driver.find_element_by_id('su').click()
            time.sleep(1)
            print(driver.title)
            assert 'allure' in driver.title

    @allure.feature('百度new功能')
    @allure.story('搜索打开新闻页')
    def test_news(self, driver):
        with allure.step('step three：点击新闻，验证是否跳转'):
            driver.find_element_by_link_text('新闻').click()
            print(driver.title)
            assert '新闻1' in driver.title


if __name__ == '__main__':
    pytest.main()
