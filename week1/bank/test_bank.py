from bank import value
def test_hello_greeting():
    assert value ("hello") ==0
def test_other_greetings():
    assert value ("what's up") ==100
    assert value ("goodbye") ==100
def test_h_greeting():
    assert value ("hi") ==20
