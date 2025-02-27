from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def go(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(Movable, Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Movable):
    def go(self):
        print("Going")



