palindrom = input("Palindrom: ")

palindrom = palindrom.lower().replace(" ", "")

if palindrom == palindrom[::-1]:
    print("Es handelt sich um ein Palindrom")
