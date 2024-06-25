from plates import is_valid

def test_valid_plate():
    assert is_valid("AB123") == True
def test_plate_too_short():
    assert is_valid("A1") == False
def test_plate_too_long():
    assert is_valid("ABC1234") == False
def test_startswith_nonalpha():
    assert is_valid("123AB") == False
def test_plate_startswith_zero():
    assert is_valid("0AB12") == False
def test_plate_contains_lettersafternumber():
    assert is_valid("AB12C") == False
def test_empty_plate():
    assert is_valid("") == False

