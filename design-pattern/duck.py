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


class Duck(ABC):
    
    @abstractmethod
    def display(self):
        pass

class MallardDuck(Duck, Swimable, Quackable, Flyable):

    def display(self):
        print("I'm a mallard duck!")

    def swim(self):
        print("Swim slow")

    def quack(self):
        print("Coin coin")

    def fly(self):
        print("I can fly")

class GoldenEyeDuck(Duck, Swimable, Quackable, Flyable):

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
    mld.fly()
    ged = GoldenEyeDuck()
    ged.display()
    ged.fly()
    ged.quack()
    yellow = RubberDuck()
    yellow.quack()