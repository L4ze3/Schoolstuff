class Tier:
    __name = ""
    __art = ""
    __hungrig = False

    def __init__(self, name, art):
        self.__name = name
        self.__art = art
        self.__hungrig = True
    
    def __str__(self):
        return f"{self.__name}: {self.__art}"

    def get_Name(self):
        return self.__name
    def set_Name(self, name):
        self.__name = name
    def get_Art(self):
        return self.__art
    def get_Hungrig(self):
        return self.__hungrig
    
    def Fuettern(self):
        self.__hungrig = False

    def Spielen(self):
        self.__hungrig = True
        return "MauWauPiepFiep"

###########
##Program##
###########

cat = Tier("Maunzi", "Katze")
dog = Tier("Peter", "Hund")
print(cat)
print(f"{cat.get_Name()}: {cat.get_Art()} {cat.get_Hungrig()}")
cat.Fuettern()
print(f"{cat.get_Name()}: {cat.get_Art()} {cat.get_Hungrig()}")
cat.Spielen()
print(f"{cat.get_Name()}: {cat.get_Art()} {cat.get_Hungrig()}")
