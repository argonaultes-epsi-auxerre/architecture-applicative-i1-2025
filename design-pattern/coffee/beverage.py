from abc import ABC, abstractmethod

class Beverage(ABC):

    def __init__(self, description):
        self.__description = description
        self.__milk = False
        self.__soy = False
        self.__mocha = False

    @abstractmethod
    def cost(self):
        pass

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
        super().__init__('deca')
        self.__initial_cost = 1.0

    def cost(self):
        total_cost = self.__initial_cost

        if self.milk:
            total_cost += 0.2

        if self.soy:
            total_cost += 0.1

        if self.mocha:
            total_cost += 10

        return total_cost

class Americano(Beverage):

    def __init__(self):
        super().__init__('americano')
        self.__initial_cost = 2.0

    def cost(self):
        total_cost = self.__initial_cost

        if self.milk:
            total_cost += 0.2

        if self.soy:
            total_cost += 0.1

        if self.mocha:
            total_cost += 10

        return total_cost

class Espresso(Beverage):

    def __init__(self):
        super().__init__('espresso')
        self.__initial_cost = 1.5

    def cost(self):
        total_cost = self.__initial_cost

        if self.milk:
            total_cost += 0.2

        if self.soy:
            total_cost += 0.1

        if self.mocha:
            total_cost += 10

        return total_cost

class Chocolate(Beverage):

    def __init__(self):
        super().__init__('chocolate')
        self.__initial_cost = 3.0

    def cost(self):
        total_cost = self.__initial_cost

        if self.milk:
            total_cost += 0.2

        if self.soy:
            total_cost += 0.1

        if self.mocha:
            total_cost += 10

        return total_cost
