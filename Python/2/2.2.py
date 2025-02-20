kg = float(input("Gewicht (kg): "))
m = float(input("Größe (m): "))

bmi = kg / m ** 2

if bmi < 18.5:
    print("Untergewicht")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normalgewicht")
elif bmi >= 25.0 and bmi <= 29.9:
    print("Übergewicht.\n\nWarnung: Sie sind ein fetter Hurensohn")
elif bmi >= 30.0 and bmi <= 34.9:
    print("Adipositas Grad 1.\n\nWarnung!")
elif bmi >= 35.0 and bmi <= 39.9:
    print("Adipositas Grad 2.\n\nWarnung!")

