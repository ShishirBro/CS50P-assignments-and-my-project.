import pytest
from fuel import convert, gauge
def test_percentage():
    assert convert("4/5") == 80
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(80) == "80%"
#def test_convert_numeratorgreaterthan_denominator():
 #   with pytest.raises(ValueError) as e:
  #      convert("3/2")
   # assert str(e.value) == "Value incorrect"
#def test_zerodiv():
 #   with pytest.raises(ZeroDivisionError) as e:
  #      convert("1/0")
   # assert str(e.value) == "denominator cannot be zero"


