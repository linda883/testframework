import pytest


# 单个测试中多次需要这个结果的情况下提供帮助。
# 而不是直接返回数据，而是返回一个生成数据的函数。然后可以在测试中多次调用此函数。
@pytest.fixture
def make_customer_record():

    def _make_customer_record(name):
        return {
            "name": name,
            "orders": []
        }

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")

    print(customer_3,customer_2,customer_1)

