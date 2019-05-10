import allure
from selenium import webdriver
import time
import pytest


@allure.testcase("https://www.baidu.com的搜索功能")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step('step one:打开浏览器输入百度网址'):

        driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/testframework/excise/driver/chromedriver')
        driver.get('https://www.baidu.com')
    with allure.step('step two：在搜索栏输入allure,并点击百度一下'):

        driver.find_element_by_id('kw').send_keys(test_data1)
        time.sleep(1)
        driver.find_element_by_id('su').click()
        time.sleep(1)
    with allure.step('step three：截图保存到项目中'):

        driver.save_screenshot("./result/b.png")
        # f = open('./result/b.png', 'rb').read()
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body> 首页</body>', 'Attach with HTML type',
                      allure.attachment_type.HTML)

    with allure.step('step four：关闭浏览器，退出'):
        driver.quit()
