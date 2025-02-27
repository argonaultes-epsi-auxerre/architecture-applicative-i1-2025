from abc import abstractmethod, ABC

class Swimable(ABC):

    @abstractmethod
    def swim(self):
        pass

class Quackable(ABC):

    @abstractmethod
    def quack(self):
        pass

class Flyable(ABC):

    @abstractmethod
    def fly(self):
        pass

class FlyableInSky(Flyable):

    def fly(self):
        print('I can fly')

class FlyableNone(Flyable):

    def fly(self):
        print('Unable to fly')

class Duck(ABC):
    
    def __init__(self, fly_behavior: Flyable = FlyableNone()):
        self.__fly_behavior = fly_behavior

    def perform_fly(self):
        self.__fly_behavior.fly()

    def set_fly_behavior(self, fly_behavior: Flyable):
        self.__fly_behavior = fly_behavior

    @abstractmethod
    def display(self):
        pass

class MallardDuck(Duck, Swimable, Quackable):

    def __init__(self):
        super().__init__(FlyableInSky())

    def display(self):
        print("I'm a mallard duck!")

    def swim(self):
        print("Swim slow")

    def quack(self):
        print("Coin coin")

    def fly(self):
        print("I can fly")

class GoldenEyeDuck(Duck, Swimable, Quackable, Flyable):

    def __init__(self):
        super().__init__(FlyableInSky())

    def display(self):
        print("GoldenEyyyye")

    def swim(self):
        print("Swim fast !!!!")

    def quack(self):
        print("Coin coin")

    def fly(self):
        print("I can fly")



class RubberDuck(Duck, Swimable, Quackable):

    def display(self):
        print("Rubber Duck")

    def swim(self):
        print("Swim slow")

    def quack(self):
        print("Plasticoin")


if __name__ == '__main__':

    mld = MallardDuck()
    mld.display()
    mld.perform_fly()
    ged = GoldenEyeDuck()
    ged.display()
    ged.perform_fly()
    ged.quack()
    yellow = RubberDuck()
    yellow.quack()
    mld.set_fly_behavior(FlyableNone())
    mld.perform_fly()
