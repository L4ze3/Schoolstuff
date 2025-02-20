vorname = input("Vorname: ")
nachname = input("Nachname: ")
strasse = input("Straße:")
hausnummer = int(input("Hausnummer: "))
plz = input("PLZ: ")
ort = input("Ort: ")

with open(vorname + nachname + ".txt", "w") as file:
    file.write(f"{vorname} {nachname}\n{strasse} {str(hausnummer)}\n{plz} {ort}\n")
