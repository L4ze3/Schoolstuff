def leap_year(year):
    if year % 4 == 0 or year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    return False

print(leap_year(2024))
