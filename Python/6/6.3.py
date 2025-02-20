a = int(input("a = "))
b = int(input("b = "))
# start = int(input("startwert: "))
# end = int(input("endwert: "))

print(f"\ny = {a}*x+{b}\n")

for i in range(1, 100):
    print(f"{i} -> {a*i+b}")
