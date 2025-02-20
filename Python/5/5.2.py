input = int(input("Sample input: "))

height = 0
rows = 0
while height + (rows + 1) <= input :
    height = height + 1
    rows = rows + 1

print(f"Expected output: The height of the pyramid is {height}")
