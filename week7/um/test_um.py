from um import count
def test_basic():
    assert count("um")==1
def test_case_insensitively():
    assert count("um Um UM uM")==4
def test_non_matches():
    assert count("yummy")==0

