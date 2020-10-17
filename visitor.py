'''
like a house

HAVC specialist: Type1
Electrician: Type2


new operations
various elements of an existing class hierarchy
'''

import abc

class House: #The class being visited
    def accept(self, visitor):
        # Trigger the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self):
        return self.__class__.__name__


class Visitor(metaclass=abc.ABCMeta):
    def __str__(self):
        return self.__class__.__name__

    @abc.abstractmethod
    def visit(self, house):
        pass



class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


hv = HvacSpecialist()
e = Electrician()

home = House()

home.accept(hv)
home.accept(e)

