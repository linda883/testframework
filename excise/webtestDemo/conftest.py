import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome(
        executable_path='/Users/lindafang/PycharmProjects/testframework/excise/driver/chromedriver')

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)
    return driver
