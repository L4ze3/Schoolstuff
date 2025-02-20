import random

rand_num = random.randint(0, 100)
print(rand_num)
guess = -1

while guess != rand_num:
    guess = int(input("Zahl: "))
    if guess < rand_num:
        print("Die gesuchte Zahl ist größer")
    elif guess > rand_num:
        print("Die gesuchte Zahl is kleiner")




