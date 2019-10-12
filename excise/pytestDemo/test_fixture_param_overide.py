import pytest


@pytest.fixture
def username():
    return 'username'


@pytest.fixture
def other_username(username):
    return 'other-' + username


@pytest.mark.parametrize('username', ['directly-overridden-username'])
def test_username(username):
    assert username == 'directly-overridden-username'


@pytest.mark.parametrize('username', ['directly-overridden-username-other'])
def test_username_other(other_username):
    assert other_username == 'other-directly-overridden-username-other'

