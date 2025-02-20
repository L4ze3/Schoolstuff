coins = {
    "2 EUR:": 200,
    "1 EUR:": 100,
    "Cent 50:": 50,
    "Cent 20:": 20,
    "Cent 10:": 10,
    "Cent 5:": 5,
    "Cent 2:": 2,
    "Cent 1:": 1,
}

rechnung = float(input("Rechnungsbetrag: "))*100
gezahlt = float(input("gezahlter Betrag: "))*100

change = gezahlt - rechnung

print("====================")
print(f"Rückgeld: {change} EUR")
print("====================")

cents = change * 100
print(cents)

for key, value in coins.items():
    print(f"{key} {(change / value)} ")
    change = (change % value)
