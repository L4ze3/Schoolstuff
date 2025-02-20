from mensch import Mensch

def print_mensch(mensch):
    print(mensch.get_Vorname(), mensch.get_Nachname(), "ist", mensch.get_Alter(), "Jahre alt und ist", mensch.get_Familienstand())

ich = Mensch("Max", "Mustermann", 40)

print(ich.get_Vorname())
print(ich.get_Alter())
print(ich.get_Vorname(), ich.get_Nachname(), "ist", ich.get_Alter(), "Jahre alt")

max = Mensch("Max", "Mustermann", 20)
print_mensch(max)

max.Geburtstag()
max.Heirat("Schmitt")

print_mensch(max)

if (max.Heirat("Schmitt")):
    print_mensch(max)
else:
    print("Ist schon verheiratet")

print(ich)
print(max)