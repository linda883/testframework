import os
import yaml
import pytest


def base_data(file_name):

    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml1 = os.path.join(cur_path, file_name)

    f1 = open(yaml1)  # 打开yaml文件
    data = yaml.load(f1)  # 使用load方法加载
    return data


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt",action="store", default="web_test", help="有两个选项web，api"
    )


@pytest.fixture()
def cmdopt(request):
    return request.config.getoption("--cmdopt")

