numbers = [3, 5, 1, 9, 6, 2, 4, 8, 0, 7]

zahl = int(input("Zahl zum suchen: "))

for i in range(len(numbers)):
    if numbers[i] == zahl:
        print(f"Die {zahl} steht an {i + 1}. Stelle im Array")
