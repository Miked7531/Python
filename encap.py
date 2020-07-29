class Protected:
    def __init__(self):
        self._protectedpie = 0

obj = Protected()
obj._protectedpie = 40
print(obj._protectedpie)

class Protprivate:
    def __init__(self):
        self.__privatepie = 30

    def getpie(self):
        print(self.__privatepie)

    def setpie(self, private):
        self.__privatepie = private


obj = Protprivate()
obj.getpie()
obj.setpie(30)
obj.getpie()
