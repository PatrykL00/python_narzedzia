import time, requests, typer
from plyer import notification

def strazuj(url: str):
    latest_stan = None
    while True:
        try:
            response = requests.get(url)
            aktualny_stan = "Działa" if response.status_code == 200 else "nie działa"
        except requests.exceptions.ConnectionError:
            aktualny_stan = "nie dziala"
        if aktualny_stan != latest_stan:
            notification.notify(title="Straznik", message=f"{aktualny_stan}", timeout=5)
            print("dziala")
        latest_stan = aktualny_stan
        time.sleep(5)

def main(url: str):
    strazuj(url)

if __name__ == "__main__":
    typer.run(main)