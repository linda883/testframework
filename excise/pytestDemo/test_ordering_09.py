import pytest


def test_01():
    print('test01')


@pytest.mark.last
def test_02():
    print('test02')
    assert(4==1)


@pytest.mark.skip
def test_03():
    print('test03')


@pytest.mark.run(order=1)
def test_04():
    print('test04')
    # assert(4==1)

