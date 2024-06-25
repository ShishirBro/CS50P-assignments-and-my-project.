from numb3rs import validate
def test_valid_ipv4():
    assert validate("192.168.0.1") == True
def test_invalid_ipv4():
    assert validate("275.3.5.28") == False

