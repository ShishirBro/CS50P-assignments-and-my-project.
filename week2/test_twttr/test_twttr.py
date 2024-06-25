from twttr import shorten

def test_no_vowels():
    assert shorten("hll") == "hll"
def test_all_vowels():
    assert shorten("AEIOUaeiou") == ""
def test_mixed_case():
    assert shorten("shishir") == "shshr"

