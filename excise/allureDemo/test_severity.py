import allure
import logging
import pytest


def test_with_no_severity_label():
    logging.debug("这是测试没有severity标签的日志")
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    logging.info("这是测试severity标签-trivial的日志info")
    pass


@allure.severity(allure.severity_level.BLOCKER)
def test_with_normal_severity():
    logging.error("这是测试severity标签-BLOCKER的日志info")
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass


if __name__ == '__main__':
    pytest.main(['--alluredir', './result', 'test_severity.py'])

