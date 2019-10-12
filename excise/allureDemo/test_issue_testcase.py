import pytest
import allure


@allure.issue('http://www.jira.com/id=19688')
@allure.testcase('http://www.testlink.com/id=19688')
def test_demo():
    print('this is test')
    with allure.step("im e 11"):
        allure.attach("p j wt kjfsl df")


if __name__ == '__main__':
    pytest.main()
