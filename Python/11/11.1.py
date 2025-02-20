def calc(n1, n2, op):
    if op == '+':
        erg = n1 + n2
    elif op == '-':
        erg = n1 - n2
    elif op == '*':
        erg = n1 * n2
    elif op == '/':
        erg = n1 / n2
    return erg

try:
    zahl1 = int(input("Erste Zahl: "))
    zahl2 = int(input("Zweite Zahl: "))
    op = input("Operand: ")
    print(calc(zahl1, zahl2, op))
except:
    print("Fehler!")

