from abc import ABC, abstractmethod

class Animal(ABC):
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        self.ouaf()

    def ouaf(self):
        print("ouaf ouaf")

class Cat(Animal):

    def make_sound(self):
        self.meow()

    def meow(self):
        print("miaou")


def use_animal(animal : Animal):
    animal.make_sound()

rintintin = Dog()
felix = Cat()

use_animal(rintintin)
use_animal(felix)