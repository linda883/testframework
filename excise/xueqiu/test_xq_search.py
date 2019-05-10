import os
import requests
import yaml
import pytest


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


@pytest.fixture(scope="module",autouse=True)
def query_param(request):
    return request.param


@pytest.mark.parametrize("query_param", test_user_data2, indirect=True)
def test_search(get_base_data, query_param):
    method = get_base_data.get('method')
    url = get_base_data.get('url')
    headers = get_base_data.get('header')
    param = query_param
    res = requests.request(method=method, url=url, headers=headers, params=param)
    print(res.text)
