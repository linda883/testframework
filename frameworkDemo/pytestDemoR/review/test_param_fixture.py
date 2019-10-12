import pytest


data1 = ['linda', 'sevenriby']


@pytest.fixture()
def data2(request):
    print("数据准备unpack")
    a = request.param
    print(a)
    return a


@pytest.mark.parametrize('data2', data1, indirect=True)
def test_data(data2):
    print(data2)


if __name__ == '__main__':
    pytest.main(['-s', 'test_param_fixture.py'])
