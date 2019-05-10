import pytest
import time


def test_baidu(driver):
    driver.get('https://www.baidu.com/s?wd=pytest')
    time.sleep(1)
    title = driver.title
    print("测试结果：%s" % title)
    assert 'pytest' in title


if __name__ == '__main__':
    pytest.main(['-v', 'test_driver2.py'])
