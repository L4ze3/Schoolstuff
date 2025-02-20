zahl = int(input("Zahl: "))
i = 1
fak = 1

while i <= zahl:
    fak = fak * i
    i = i + 1

print(f"{zahl}! = {fak}")
