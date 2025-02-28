from abc import ABC, abstractmethod

class MenuComponent(ABC):

    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @abstractmethod
    def print_menu(self):
        pass

class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price):
        super().__init__(name, description)
        self.__vegetarian = vegetarian
        self.__price = price

    @property
    def vegetarian(self):
        return self.__vegetarian

    @property
    def price(self):
        return self.__price

    def print_menu(self):
        print(f'{self.name} ({self.description}) - {self.__price}')

    def __repr__(self):
        return f'{self.name} ({self.description}) - {self.__price}'

class Iterator(ABC):

    @abstractmethod
    def next_item(self):
        pass

    @abstractmethod
    def has_more_items(self) -> bool:
        pass


class Menu(MenuComponent):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.__menu_components = []

    def add_menu_component(self, menu_component):
        self.__menu_components.append(menu_component)

    def print_menu(self):
        print(f'== Menu: {self.name} ==')
        it_menu = self.create_iterator()
        while it_menu.has_more_items():
            menu_item = it_menu.next_item()
            menu_item.print_menu()

    def create_iterator(self) -> Iterator:
        return MenuIterator(self.__menu_components)

class MenuIterator(Iterator):
    def __init__(self, menu_items):
        self.__menu_items = menu_items
        self.__position = 0
    
    def next_item(self) -> Menu:
        next_item = self.__menu_items[self.__position]
        self.__position += 1
        return next_item

    def has_more_items(self):
        return self.__position < len(self.__menu_items)


class BreakfastMenu(Menu):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.add_menu_component(MenuItem('pancake', 'the best', True, 10.0))
        self.add_menu_component(MenuItem('waffle', 'the best', True, 9.0))
        self.add_menu_component(MenuItem('kiwi', 'healthy and yellow', True, 2.0))


class LunchMenu(Menu):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.add_menu_component(MenuItem(name = 'burger', vegetarian=False, description='the best', price=10.0))
        self.add_menu_component(MenuItem('chicken', 'cotcot', False, 12.0))
        self.add_menu_component(MenuItem('tomato', 'sun and red', True, 2.0))


class DinerMenu(Menu):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.add_menu_component(MenuItem(name = 'salad', vegetarian=True, description='the best', price=10.0))
        self.add_menu_component(MenuItem('soup', 'miam miam', True, 8.0))
        self.add_menu_component(MenuItem('burgundy', 'very good', False, 22.0))

class Waiter:
    
    def __init__(self, breakfast_menu: Menu, lunch_menu: Menu, diner_menu: Menu):
        self.__menus = Menu('Tous les menus', '')
        self.__menus.add_menu_component(breakfast_menu)
        self.__menus.add_menu_component(lunch_menu)
        self.__menus.add_menu_component(diner_menu)

    def display_menu(self):
        self.__menus.print_menu()

    # def print_menu(self, menu : Menu):
    #     it_menu = menu.create_iterator()
    #     while it_menu.has_more_items():
    #         menu_item = it_menu.next_item()
    #         print(menu_item)

if __name__ == '__main__':
    jerome = Waiter(BreakfastMenu('Breakfast', 'the most important'), LunchMenu('Lunch Menu', 'middle of the day'), DinerMenu('Diner Menu', 'go to bed'))
    jerome.display_menu()