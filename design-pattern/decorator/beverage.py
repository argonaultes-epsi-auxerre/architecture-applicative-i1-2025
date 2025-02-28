from abc import ABC, abstractmethod

class Beverage(ABC):

    def __init__(self, description, initial_cost):
        self.__description = description
        self.__milk = False
        self.__soy = False
        self.__mocha = False
        self.__sugar = False
        self.__initial_cost = initial_cost

    def cost(self):
        total_cost = self.__initial_cost

        if self.milk:
            total_cost += 0.2

        if self.soy:
            total_cost += 0.1

        if self.mocha:
            total_cost += 10

        if self.sugar:
            total_cost += 0.15

        return total_cost

    @property
    def sugar(self):
        return self.__sugar

    @sugar.setter
    def sugar(self, value):
        self.__sugar = value

    @property
    def milk(self):
        return self.__milk

    @milk.setter
    def milk(self, value):
        self.__milk = value

    @property
    def soy(self):
        return self.__soy

    @soy.setter
    def soy(self, value):
        self.__soy = value

    @property
    def mocha(self):
        return self.__mocha

    @mocha.setter
    def mocha(self, value):
        self.__mocha = value


class Deca(Beverage):

    def __init__(self):
        super().__init__('deca', 1.0)



class Americano(Beverage):

    def __init__(self):
        super().__init__('americano', 2.0)

class Espresso(Beverage):

    def __init__(self):
        super().__init__('espresso', 1.5)
        self.soy = True


class Chocolate(Beverage):

    def __init__(self):
        super().__init__('chocolate', 3.0)
        self.mocha = True

