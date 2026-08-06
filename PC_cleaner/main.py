from pathlib import Path
import os
import shutil
import argparse
import typer

parser = argparse.ArgumentParser()
parser.add_argument("--sciezka", required=True)
args = parser.parse_args()
def index(sciezka: str) -> None:
    folder = Path(sciezka)
    suma = 0
    miejsce = 0
    for element in folder.rglob("*"):
        try:
            if element.is_file():
                suma += 1
                miejsce += element.stat().st_size
        except OSError:
            pass
    print(f"Znalezione pliki: {suma}")
    print(f"Miejsce do zwolnienia: {format_size(miejsce)}")
    choose  = input("Czy zwolnic dane? (y/n)")
    if choose == "y":
        delete_data(sciezka)
    else:
        print("anulowano")


def format_size(size):
    if size >= 1024**3:
        return f"{size / 1024**3:.2f} GB"
    elif size >= 1024**2:
        return f"{size / 1024**2:.2f} MB"
    else:
        return f"{size / 1024:.2f} KB"

def delete_data(sciezka: str)-> None:
    folder = Path(sciezka)
    delete_file = 0
    delete_folder = 0
    miejsce = 0
    skipped_element = 0
    for element in folder.rglob("*"):
       if element.is_file():
            try:
                miejsce += element.stat().st_size
                element.unlink()
                delete_file += 1

            except OSError:
                skipped_element += 1

    foldery = [e for e in folder.rglob("*") if e.is_dir()]

    foldery.sort(key= lambda x: len(x.parts), reverse=True)
    for element in foldery:
        try:
            element.rmdir()
            delete_folder += 1
        except OSError:
            skipped_element += 1
    print(f"Usuniete pliki: {delete_file}")
    print(f"Usuniete foldery: {delete_folder}")
    print(f"Zwolnione miejsce: {format_size(miejsce)}")
    print(f"Pominiete pliki: {skipped_element}")


if __name__ == "__main__":
    index(args.sciezka)
