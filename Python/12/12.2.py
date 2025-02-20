with open("alphabet.txt", "r") as file:
    while True:
        char = file.read(1)
        if not char:
            break
        print(f"{char} -> {ord(char)}")
