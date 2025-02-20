lager = {
    "Bourbon": 0,
    "Schokolade": 5,
    "Erdbeeren": 3,
    "Hopfenblütentee": 1,
    "Lasagne": 0,
    "Himbeeren": 4,
    "Eis": 7,
    "Litschi": 0
}

for key, value in lager.items():
    if value == 0:
        print(key, end=" ")
print("bitte nachbestellen")

bestand = input("Welchen Bestand möchten Sie wissen? ")

print(lager[bestand])
