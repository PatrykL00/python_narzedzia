import sys, argparse
from pathlib import Path
import typer

def policz(sciezka: str) -> int|None:
    try:
        i = 0
        with open(sciezka, "r") as file:
            for linia in file:
                i += len(linia.split())
        return i
    except FileNotFoundError:
        print("nie znaleziono pliku")
        return None


def main(folder: str):
    folder_path = Path(folder)
    with open("raport.txt", "w") as raport:
        for sciezka in folder_path.glob("*.txt"):
            wynik = policz(sciezka)
            raport.write(f"Plik: {sciezka} linie: {wynik}\n")

if __name__ == "__main__":
    typer.run(main)

