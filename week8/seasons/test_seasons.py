from seasons import get_min as M
import pytest
def test_input():
    with pytest.raises(TypeError):
        M(12-12-2012)=='Invalid date'
def test_in():
    assert M(2012-13-12) == 'Invalid date'
def test-format():
    assert M(2012-322-12)=='Invalid date'
