# Python Narzędzia

Zbiór małych narzędzi CLI napisanych w Pythonie — każde rozwiązuje jeden konkretny, praktyczny problem: pracę z plikami, monitoring stron internetowych, porządkowanie dysku i pobieranie danych z API.

## Narzędzia

###  licznik_linijek
Liczy linijki w plikach `.txt` w podanym folderze i wypisuje wynik na ekranie.

```bash
cd licznik_linijek
python main.py <folder>
```

###  licznik_slow
Liczy słowa w plikach `.txt` w podanym folderze i zapisuje wyniki do `raport.txt`.

```bash
cd licznik_slow
python main.py <folder>
```

###  kurs_walut
Pobiera aktualny kurs wybranej waluty z publicznego API Narodowego Banku Polskiego (NBP).

```bash
cd kurs_walut
python main.py <kod_waluty>
# np. python main.py usd
```

###  straznik
Monitoruje wybraną stronę internetową w czasie rzeczywistym i wysyła powiadomienie systemowe, gdy zmieni się jej status (działa / nie działa).

```bash
cd straznik
python main.py <url>
# np. python main.py https://github.com
```

###  organizer
Sortuje pliki z folderu (np. Downloads) do wskazanych podfolderów na podstawie rozszerzenia — zdjęcia i dokumenty trafiają w osobne miejsca.

```bash
cd organizer
python main.py <folder_zrodlowy> <folder_zdjecia> <folder_dokumenty>
```

###  PC_cleaner
Skanuje wskazany folder (np. Temp), pokazuje ile plików i miejsca na dysku można zwolnić, i po potwierdzeniu przez użytkownika usuwa zawartość.

```bash
cd PC_cleaner
python main.py --sciezka <folder>
```

 To narzędzie **trwale usuwa pliki**. Używaj ostrożnie i tylko na folderach, których jesteś pewny (np. Temp).

## Wymagania

Każde narzędzie korzysta z bibliotek zewnętrznych. Zainstaluj je przed uruchomieniem:

```bash
pip install requests typer plyer
```

## Czego się nauczyłem, budując te narzędzia

- Praca z plikami i folderami (`pathlib`, `os`, `shutil`)
- Budowanie interfejsów CLI (`argparse`, `typer`)
- Obsługa błędów (`try/except`)
- Komunikacja z API przez HTTP (`requests`, parsowanie JSON)
- Pętle działające w tle i śledzenie zmiany stanu (`time.sleep`, powiadomienia systemowe)
- Dobre praktyki: type hints, rozdzielanie logiki od pobierania danych wejściowych, `if __name__ == "__main__"`

## Autor

Patryk — projekt tworzony w ramach nauki Pythona, backend developmentu i pisania narzędzi automatyzujących codzienne zadania.
