from main import format_size

def test_formatu():
    wynik = format_size(2048)
    assert wynik == "2.00 KB"