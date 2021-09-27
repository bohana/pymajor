import pytest

from pymajor.core import Interval


@pytest.mark.parametrize('sz, res', [
    (0.0, 0.0),
    (1.5, 1.5),
    (1, 1.0),
    ('1', 0.0),
    ('1j', 0.0),
    ('5', 3.5),
    ('5j', 3.5),
    ('3M', 2.0)
])
def test_interval_sizes(sz, res):
    assert Interval(sz).size == res


@pytest.mark.parametrize('invalid_interval', [
    -1.0,
    8.0,
    '17',
    '0j',
    '2pi',
    '3Z'
])
def test_interval_valid(invalid_interval):
    with pytest.raises(ValueError):
        Interval(invalid_interval)
