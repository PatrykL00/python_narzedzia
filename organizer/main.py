import os
from pathlib import Path
import shutil
import typer

def index(folder: str, zdjecia: str, dokumenty: str):
    counter = 0
    try:
        for plik in os.listdir(folder):
            _, rozszerzenie = os.path.splitext(plik)
            sciezka = os.path.join(folder, plik)
            rozszerzenie = rozszerzenie.lower()
            print(rozszerzenie)
            if rozszerzenie in [".jpg", ".png", ".jpeg"]:
                shutil.move(sciezka, zdjecia)
                counter += 1
            elif rozszerzenie in [".pdf", ".txt", ".docx"]:
                shutil.move(sciezka, dokumenty)
                counter += 1
        print(f"Przeniesiono: {counter} plikow")
    except FileNotFoundError:
        print("Nie znaleziono pliku ")

def main(folder: str, zdjecia: str, dokumenty: str):
    index(folder, zdjecia, dokumenty)

if __name__ == "__main__":
    typer.run(main)


