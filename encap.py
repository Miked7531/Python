class Encaphype:
    def __init__(self):
        self.__privateHype = 50

    def getEncap(self):
        print(self.__privateHype)

    def setEncap(self, envap):
        self.__privateHype = envap

obj = Encaphype()
obj.getEncap()
obj.setEncap(50)
obj.getEncap()
