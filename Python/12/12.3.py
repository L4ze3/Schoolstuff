with open("Namen.txt", "r") as file:
    c = 1
    group = []
    groups = []
    lines = file.readlines()
    for line in lines:
        group.append(line.strip())
        if c == 4:
            groups.append(group)
            group = []
            c = 0
        c += 1
print(groups)
