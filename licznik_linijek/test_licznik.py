from main2 import policz

def test_goodvalue():
    wynik = policz("test.txt")
    assert wynik is None