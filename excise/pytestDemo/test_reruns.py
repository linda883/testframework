import time
import random


def test_rerun():
    time.sleep(1)
    a = random.randint(1, 3)
    print(a)
    assert 3 == a

