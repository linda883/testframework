import pytest
import time


def test_testerhome(driver):
    driver.get('https://testerhome.com')
    time.sleep(1)
    title = driver.title
    print("测试结果：%s" % title)
    assert 'tester' in title


if __name__ == '__main__':
    pytest.main(['-v', 'test_driver1.py'])
