letters = {chr(i+64):0 for i in range(1, 27)}

with open("Namen.txt", "r") as file:
    names = []
    lines = file.readlines()
    for line in lines:
        names.append(line.strip())
    names = sorted(names)

for key, value in letters.items():
    for name in names:
        if name[0] == key:
            letters[name[0]] += 1

print(letters)
