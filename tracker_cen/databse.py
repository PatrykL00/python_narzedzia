import sqlite3
from datetime import datetime

def connect():
    conn = sqlite3.connect("ceny.db")
    conn.row_factory = sqlite3.Row
    return conn

def stworz():
    conn = connect()
    kursor = conn.cursor()
    kursor.execute("""
        CREATE TABLE IF NOT EXISTS ceny (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produkt TEXT,
            cena REAL,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

def dodaj_cene(produkt: str, cena: float):
    conn = connect()
    kursor = conn.cursor()
    teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    kursor.execute("INSERT INTO ceny (produkt, cena, data) VALUES (?, ?, ?)", (produkt, cena, teraz))
    conn.commit()
    conn.close()

stworz()