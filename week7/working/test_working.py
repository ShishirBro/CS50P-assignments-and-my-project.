import pytest
from working import convert
def test_convert_with_minutes():
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
def test_convert_without_minutes():
    assert convert("9AM to 5PM")=="09:00 to 17:00"
def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:70 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:20 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:10 AM to 13:00 PM")

