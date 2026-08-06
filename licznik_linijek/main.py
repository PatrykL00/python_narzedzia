import sys
from pathlib import Path
import typer

def policz(sciezka: str) -> int|None:
    try:
        i = 0
        with open(sciezka, "r") as file:
            for linia in file:
                i += 1
        return i
    except FileNotFoundError:
        print("nie znaleziono pliku")
        return None

def main(folder: str):
    folder_path = Path(folder)
    for sciezka in folder_path.glob("*.txt"):
        wynik = policz(sciezka)
        print(f"plik: {sciezka}, liczba linijek: {wynik}")

if __name__ == "__main__":
    typer.run(main)