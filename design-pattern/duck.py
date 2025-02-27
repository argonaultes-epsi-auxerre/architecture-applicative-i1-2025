from abc import abstractmethod, ABC

class Duck(ABC):

    def fly(self):
        print('Flyiiiiing')

    def quack(self):
        print('Coin coin')
    
    @abstractmethod
    def display(self):
        pass

class MallardDuck(Duck):

    def display(self):
        print("I'm a mallard duck!")

class GoldenEyeDuck(Duck):

    def display(self):
        print("GoldenEyyyye")

    def swim(self):
        print("Swim fast !!!!")

class RuberDuck(Duck):

    def display(self):
        print("Rubber Duck")

    def fly(self):
        print("I can't fly")

if __name__ == '__main__':

    mld = MallardDuck()
    mld.display()
    mld.fly()
    ged = GoldenEyeDuck()
    ged.display()
    ged.fly()
    ged.quack()