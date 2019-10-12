import pytest


@pytest.fixture
def equipments(request):
    r = []
    for port in ('C1', 'C3', 'C28'):
        equip = connect(port)
        request.addfinalizer(equip.disconnect)
        r.append(equip)
    return r
