import requests
import yaml
import os
import pytest


def _base_data(file_name):

    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml1 = os.path.join(cur_path, file_name)

    f1 = open(yaml1)  # 打开yaml文件
    data = yaml.load(f1)  # 使用load方法加载

    return data


@pytest.fixture()
def get_base_data():
    base_data = _base_data('test_search.yml')
    for v in base_data.values():
        return v


@pytest.fixture()
def get_test_data():
    test_data = _base_data('test_search_data.yml')
    payload = test_data.get("payload")
    return payload


def test_search(get_test_data, get_base_data):

    method = get_base_data.get('method')
    url = get_base_data.get('url')
    headers = get_base_data.get('header')

    res = requests.request(method=method, url=url, headers=headers, params=get_test_data)
    print(res.text)





