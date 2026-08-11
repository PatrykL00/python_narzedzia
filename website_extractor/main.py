import typer
import scraper
import json

app = typer.Typer()

@app.command()
def pobierz(url: str, arg: str, autor: str = None):
    rezult = scraper.scraperweb(url, arg, autor)
    print(rezult)
    save_json(rezult)

def save_json(rezult: list):
    with open("wynik.json", "w", encoding="utf-8") as file:
        json.dump(rezult, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    app()