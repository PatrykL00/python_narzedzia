import requests, typer



def pobierz_walute(waluta: str)-> float|None:
    waluta = waluta.lower()
    URL = f"https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/?format=json"
    response = requests.get(URL)
    if response.status_code != 200:
        print(response.status_code)
        return None
    
    dane = response.json()
    a = dane["rates"][0]["mid"]
    return a

def main(waluta: str):
    wynik = pobierz_walute(waluta)
    print(wynik)

if __name__ == "__main__":
    typer.run(main)

