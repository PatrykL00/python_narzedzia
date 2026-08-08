import requests, typer, time
from bs4 import BeautifulSoup
import databse
from plyer import notification

def pobierz(url: str)-> float:
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("p", class_="price_color").text
    price = price.replace("£", "")
    cena = float(price)
    return cena

def monitoruj(url: str, nazwa: str, interwal: int = 5):
    latest_price = None
    while True:
        price = pobierz(url)
        if latest_price is not None and latest_price != price:
                databse.dodaj_cene(nazwa, price)
                notification.notify(title="zmiana ceny", message="Cena sie zmienila, wynik w bd", timeout=5)
        latest_price = price
        time.sleep(interwal)


def main(url: str, nazwa: str):
    monitoruj(url, nazwa)

if __name__ == "__main__":
    typer.run(main)


