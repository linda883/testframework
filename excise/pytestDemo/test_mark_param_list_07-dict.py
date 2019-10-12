import pytest

test_input ={'name':'linda','password':'123456'}

expected ={'statuscode':200,'info':'ok'}
# 参数化，前面两个变量，后面是对应的数据；3+5--->test_input,8-->expected


@pytest.mark.parametrize("test_input,expected",[test_input,expected])
def test_eval(test_input, expected):
    # eval将字符串str当成有效的表达式来求值并返回计算结果
    print(test_input,expected)


if __name__ == '__main__':
    pytest.main()
