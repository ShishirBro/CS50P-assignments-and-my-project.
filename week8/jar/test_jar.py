from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
def test_init_correct():
    jar = Jar(10)
    assert str(jar) == ''
def test_str():
    jar.deposit(1)
    assert str(jar)=='🍪'

