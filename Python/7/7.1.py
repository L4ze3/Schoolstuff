code = [1, 2, 3, 4]
user = []

for i in range(4):
    zahl = int(input("Zahl: "))
    user.append(zahl)

if code == user:
    print("Access granted")
else:
    print("Access denied")
