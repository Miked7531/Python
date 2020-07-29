from abc import ABC, abstractmethod
class pie(ABC):
    def pieSlice(self, amount):
        print("Your slice of the pie is: ",amount)
        
    @abstractmethod
    def piethief(self, amount):
        pass

class Totalpieslices(pie):
    def piethief(self, amount):
        print('You have stolen {} slices of pie!!'.format(amount))

obj = Totalpieslices()
obj.pieSlice("0")
obj.piethief("4")
