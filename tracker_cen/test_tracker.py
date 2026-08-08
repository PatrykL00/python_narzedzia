import pytest
from main import pobierz

def test_pobierz():
    cena = pobierz("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    assert cena > 0