from abc import ABC, abstractmethod

class MenuItem:

    def __init__(self, name, description, vegetarian, price):
        self.__name = name
        self.__description = description
        self.__vegetarian = vegetarian
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def vegetarian(self):
        return self.__vegetarian

    @property
    def price(self):
        return self.__price

    def print_menu(self):
        return f'{self.__name} ({self.__description}) - {self.__price}'

    def __repr__(self):
        return f'{self.__name} ({self.__description}) - {self.__price}'



class Iterator(ABC):

    @abstractmethod
    def next_item(self):
        pass

    @abstractmethod
    def has_more_items(self) -> bool:
        pass

class IterableCollection(ABC):

    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

class BreakfastMenuIterator(Iterator):
    
    def __init__(self, breakfast_menu_items):
        self.__breakfast_menu_items = breakfast_menu_items
        self.__position = 0
    
    def next_item(self):
        next_item = self.__breakfast_menu_items[self.__position]
        self.__position += 1
        return next_item

    def has_more_items(self):
        return self.__position < len(self.__breakfast_menu_items)

class BreakfastMenu(IterableCollection):

    def __init__(self):
        self.__menu_items = []
        self.add_item('pancake', 'the best', True, 10.0)
        self.add_item('waffle', 'the best', True, 9.0)
        self.add_item('kiwi', 'healthy and yellow', True, 2.0)

    def add_item(self, name, description, vegetarian, price):
        self.__menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self) -> Iterator:
        return BreakfastMenuIterator(self.__menu_items)

class LunchMenuIterator(Iterator):
    def __init__(self, lunch_menu_items):
        self.__lunch_menu_items = lunch_menu_items
        self.__position = len(self.__lunch_menu_items) - 1
    
    def next_item(self):
        next_item = self.__lunch_menu_items[self.__position]
        self.__position -= 1
        return next_item

    def has_more_items(self):
        return self.__position >= 0

class LunchMenu(IterableCollection):

    def __init__(self):
        self.__menu_items = []
        self.add_item(name = 'burger', vegetarian=False, description='the best', price=10.0)
        self.add_item('chicken', 'cotcot', False, 12.0)
        self.add_item('tomato', 'sun and red', True, 2.0)

    def add_item(self, name, description, vegetarian, price):
        self.__menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self):
        return LunchMenuIterator(self.__menu_items)


class Waiter:
    
    def __init__(self, breakfast_menu: BreakfastMenu, lunch_menu: LunchMenu):
        self.__breakfast_menu = breakfast_menu
        self.__lunch_menu = lunch_menu

    def display_menu(self):
        it_breakfast_menu = self.__breakfast_menu.create_iterator()
        print("==== Breakfast Menu ====")
        while it_breakfast_menu.has_more_items():
            menu_item = it_breakfast_menu.next_item()
            print(menu_item)

        it_lunch_menu = self.__lunch_menu.create_iterator()
        print("==== Lunch Menu ====")
        while it_lunch_menu.has_more_items():
            menu_item = it_lunch_menu.next_item()
            print(menu_item)

if __name__ == '__main__':
    jerome = Waiter(BreakfastMenu(), LunchMenu())
    jerome.display_menu()