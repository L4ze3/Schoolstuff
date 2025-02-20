def is_prime(x):
    for i in range(2, x+1):
        if x % i == 0:
            return False
        return True

for i in range(1, 20):
    if is_prime(i):
        print(i, end=" ")
print()
