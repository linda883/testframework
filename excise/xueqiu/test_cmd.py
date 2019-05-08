import pytest


def test_salmple(cmdopt):
    if cmdopt == 'web_test':
        print("web test")
    elif cmdopt == "api_test":
        print("api test")
    assert 1


