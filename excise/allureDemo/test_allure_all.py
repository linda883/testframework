import pytest
import allure
import logging


# 测试函数
@allure.step("测试步骤1：字符串相加：{0}，{1}")     # 测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print("hello",str1,str2)
    if not isinstance(str1, str):
        return "%s 不是字符串" % str1
    if not isinstance(str2, str):
        return "%s 不是字符串" % str2
    return str1 + str2


@allure.description("测试相加的各种情况")
@allure.severity("critical")               # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.feature("测试功能_demo1")           # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
@allure.story("测试模块_demo2")             # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
# @allure.issue("BUG号：123")                 # BUG编号，关联标识已有的问题，可为一个url链接地址
@allure.issue("http://www.jira.com/id=19688")   # BUG编号，关联标识已有的问题，可为一个url链接地址
@allure.testcase("用例名：测试字符串相等")      # 用例标识，关联标识用例，可为一个url链接地址
@pytest.mark.parametrize("para_one, para_two",              # 用例参数
                         [("hello world", "hello world"),   # 用例参数的参数化数据
                          ('4', '54'),
                          ("我不是超人", "我是超人"),
                            ("888", "我是超人")],
                         ids=["letter",          # 对应用例参数化数据的用例名
                              "decimal123",
                              "unicode",
                              "mix"])
def test_case_example(para_one, para_two):
    """用例描述：测试字符串相等
    :param para_one: 参数1
    :param para_two: 参数2
    """
    logging.info("这是测试的信息，在log中输出")
    # 获取参数
    paras = vars()
    # 关联的资料信息, 可在报告中记录保存必要的相关信息
    allure.attach("用例参数", "{0}".format(paras))
    # 调用测试函数
    res = str_add(para_one, para_two)
    # 对必要的测试中间结果数据做备份
    allure.attach("str_add返回结果", "{0}".format(res))
    # 测试步骤，对必要的测试过程加以说明
    with allure.step("测试步骤2，结果校验 {0} == {1}".format(res, para_one+para_two)):
        allure.attach('<html><head></head><body> 附加网页看效果 </body></html>', '这是错误页的结果信息', allure.attachment_type.HTML)
        assert res == para_one+para_two, res


if __name__ == '__main__':
    # 执行，指定执行测试模块_demo1, 测试模块_demo2两个模块，同时指定执行的用例优先级为critical,blocker
    pytest.main(['--allure_feature=测试功能_demo1', '--allure_stories=测试模块_demo2', '--allure_severities=critical, blocker'])
