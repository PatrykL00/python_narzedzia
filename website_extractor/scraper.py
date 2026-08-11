import requests
from bs4 import BeautifulSoup

def scraperweb(url: str, arg: str, autor: str = None):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Nie udało się połączyć ze stroną")
        return []
    web = response.text
    soup = BeautifulSoup(web, "html.parser")
    if autor is not None:
        teksty = []
        autorzy = []
        wynik = []
        for element in soup.select(arg):
            teksty.append(element.get_text(strip=True))
        for element in soup.select(autor):
            autorzy.append(element.get_text(strip=True))
        for x, y in zip(teksty, autorzy):
            wynik.append({"tekst: ": x, "autor: ": y})
        return wynik
        
        
    wynik = []
    for element in soup.select(arg):
        wynik.append(element.get_text(strip=True))
    return wynik