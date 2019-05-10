import requests
import pytest
import os
import yaml
import allure


def _base_data(file_name):

    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml1 = os.path.join(cur_path, file_name)

    f1 = open(yaml1)  # 打开yaml文件
    data = yaml.load(f1)  # 使用load方法加载
    return data


@pytest.fixture(autouse=True)
def get_base_data():
    base_data = _base_data('test_search.yml')
    for v in base_data.values():
        return v


test_user_data2 = [{"q": "中国平安", "count": 3, "page": 1},
                  {"q": "阿里巴巴", "count": 2, "page": 2},
                  {"q": "pdd", "count": 3, "page": 1}]


@pytest.fixture(scope="module", autouse=True)
def query_param(request):
    # q = request.param['q']
    # count = request.param['count']
    # page = request.param['page']
    # print("查询的搜索词：%s" % q)
    return request.param


@allure.description_html("""
<h1>这是一个调试的测试内容，查看一下人名和断言</h1>
<table style="width:100%">
{get_base_data}
</table>
""")
@allure.description("一个是调用，一个是数据")
@allure.title("参数化: adding {query_param} 到请求中")
@pytest.mark.parametrize("query_param", test_user_data2, indirect=True)
def test_search(get_base_data, query_param):

    method = get_base_data.get('method')
    url = get_base_data.get('url')
    headers = get_base_data.get('header')
    # print(method)
    params = query_param
    search_text = params['q']
    res = requests.request(method=method, url=url, headers=headers, params=params)
    assert search_text in res.text





