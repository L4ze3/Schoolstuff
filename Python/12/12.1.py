poem = input("Gib das Gedicht ein: ")

try:
    with open(poem + ".txt", "r") as file:
        data = file.read()
        print(data)
        lines = data.split()
        words = len(lines)
        print(words)
        
except FileNotFoundError:
    print("Diese Datei gibts nicht!")
