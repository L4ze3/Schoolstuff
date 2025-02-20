def pw_test(pw):
    p = 0
    if len(pw) >= 7:
        p += 1
    if any(char.isdigit() for char in pw):
        p += 1
    if any(not char.isalnum() for char in pw):
        p += 1
    if any(char.isupper() for char in pw and any(char.islower() for char in pw)):
        p += 1
    if len(set(pw)) > 6:
        p += 1
    return p

print(f"abc:{pw_test('abc')}")
print(f"abcabcabc:{pw_test('abcabcabc')}")
print(f"abcdefghij:{pw_test('abcdefghij')}")
print(f"Ab1122%%!!:{pw_test('Ab1122%%!!')}")
print(f"Ab1122%?!!:{pw_test('Ab1122%?!!')}")
