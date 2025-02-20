wort = input("Wort: ")

for i in wort:
    print(ord(i.lower()) - 96, end=" ")
print()
