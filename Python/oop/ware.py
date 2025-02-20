class Ware:
    __bezeichnung = ""
    __menge = 0
    __preis = 0

    def __init__(self, bez, menge, preis):
        self.__bezeichnung = bez
        self.__menge = menge
        self.__preis = preis

    def Entnehmen(self, menge):
        return menge * self.__preis
    
    def Einlagern(self, menge):
        return menge