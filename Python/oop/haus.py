class Haus:
    __bezeichnung = ""
    __typ = ""
    __wohnflaeche = 0
    __bewohner = 0

    def __init__(self, bez, typ, flaeche):
        self.__bezeichnung = bez
        self.__typ = typ
        self.__wohnflaeche = flaeche
    
    def __str__(self):
        return f"Bezeichung: {self.__bezeichnung}\nTyp: {self.__typ}\nFlaeche: {self.__wohnflaeche}\nBewohner: {self.__bewohner}"

    def Zuzug(self, num):
        max_bewohner = self.__wohnflaeche // 20
        if (num < max_bewohner):
            self.__bewohner += num
            return True
        return False

    def Auszug(self, num):
        self.__bewohner -= num
        if (self.__bewohner < 0):
            self.__bewohner = 0

######################Programm###########################

haus = Haus("Villa", "Villa", 100)
haus.Zuzug(1)
print(haus)

haus2 = Haus("Holzhütte", "Hütte", 20)
haus2.Zuzug(2)
print(haus2)