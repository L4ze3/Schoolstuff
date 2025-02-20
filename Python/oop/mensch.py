class Mensch:
    __alter = 0
    __vorname = ""
    __nachname = ""
    __familienstand = "ledig"

    def __init__(self, vorn, nachn, age):
        self.__vorname = vorn
        self.__nachname = nachn
        self.__alter = age
        self.__familienstand = "ledig"

    def __str__(self):
        return f"{self.__nachname} ({self.__alter})"

    def get_Alter(self):
        return self.__alter
   # def set_Alter(self, value):
   #     self.__alter = value
    def get_Vorname(self):
        return self.__vorname
  #  def set_Vorname(self, value):
  #      self.__vorname = value
    def get_Nachname(self):
        return self.__nachname
 #   def set_Nachname(self, value):
 #       self.__nachname = value
    def get_Familienstand(self):
        return self.__familienstand
#    def set_Familienstand(self, value):
#        self.__familienstand = value

    def Geburtstag(self):
        self.__alter += 1
    
    def Heirat(self, name):
        if self.__familienstand == "ledig":
            self.__familienstand = "verheiratet"
            self.__nachname = name
            return True
        return False
