from abc import ABC, abstractmethod

class Beverage(ABC):

    def __init__(self, description):
        self.__description = description

    @property
    def description(self):
        return self.__description

    @abstractmethod
    def cost(self):
        pass

        # total_cost = self.__initial_cost

        # if self.milk:
        #     total_cost += 0.2

        # if self.soy:
        #     total_cost += 0.1

        # if self.mocha:
        #     total_cost += 10

        # if self.sugar:
        #     total_cost += 0.15

        # return total_cost

class Condiment(Beverage):

    def __init__(self, beverage: Beverage, description):
        super().__init__(description)
        self._beverage = beverage

class Soy(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, 'soy')

    def cost(self):
        return 0.1 + self._beverage.cost()

class Mocha(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, 'mocha')
    
    def cost(self):
        return 10 + self._beverage.cost()

class Milk(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, 'milk')
    
    def cost(self):
        return 0.2 + self._beverage.cost()

class Sugar(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, 'sugar')

    def cost(self):
        return 0.15 + self._beverage.cost()


class Deca(Beverage):

    def __init__(self):
        super().__init__('deca')

    def cost(self):
        return 1.0

class Americano(Beverage):

    def __init__(self):
        super().__init__('americano')

    def cost(self):
        return 2.0

class Espresso(Beverage):

    def __init__(self):
        super().__init__('espresso')

    def cost(self):
        return 1.5


class Chocolate(Beverage):

    def __init__(self):
        super().__init__('chocolate')

    def cost(self):
        return 3.0

