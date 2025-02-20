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
    op = input("Operator: ")
    print(calc(zahl1, zahl2, op))
except ValueError:
    print("Nur Zahlen!")
except ZeroDivisionError:
    print("Teilen durch 0 nicht moeglich!")
except UnboundLocalError:
    print("Falscher Operator")

