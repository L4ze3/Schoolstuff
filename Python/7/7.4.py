seats = [["x" for _ in range(25)] for _ in range(15)]

loop = True

for i in range(25):
    print(i, end=" ")

for i in seats:
    print(*i)

while loop:

    print("Reservierung:")
    row = int(input("Reihe: "))
    column = int(input("Platz: "))

    seats[row - 1][column - 1] = "o"

    for i in seats:
        print(*i)

    userInput = int(input("Weitere Tickets bestellen (0), beenden (1) > "))
    if userInput == 1:
        loop = False


