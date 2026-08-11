import hashlib, json

dane = [
    {
        "nazwa": "laptop",
        "cena": "5000"
    }
]

with open("produkty.json", "w", encoding="utf-8") as file:
    json.dump(dane, file, indent=4, ensure_ascii=False)

with open("produkty.json", "r", encoding="utf-8") as file:
    dane = json.load(file)
print(dane["nazwa"])