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

class BreakfastMenuIterator:
    pass

class BreakfastMenu:

    def __init__(self):
        self.__menu_items = []
        self.add_item('pancake', 'the best', True, 10.0)
        self.add_item('waffle', 'the best', True, 9.0)
        self.add_item('kiwi', 'healthy and yellow', True, 2.0)

    def add_item(self, name, description, vegetarian, price):
        self.__menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self) -> BreakfastMenuIterator:
        pass

    @property
    def menu_items(self):
        return self.__menu_items

class LunchMenu:

    def __init__(self):
        self.__menu_items = []
        self.add_item(name = 'burger', vegetarian=False, description='the best', price=10.0)
        self.add_item('chicken', 'cotcot', False, 12.0)
        self.add_item('tomato', 'sun and red', True, 2.0)

    def add_item(self, name, description, vegetarian, price):
        self.__menu_items.append(MenuItem(name, description, vegetarian, price))

    @property
    def menu_items(self):
        return self.__menu_items


class Waiter:
    
    def __init__(self, breakfast_menu: BreakfastMenu, lunch_menu: LunchMenu):
        self.__breakfast_menu = breakfast_menu
        self.__lunch_menu = lunch_menu

    def display_menu(self):
        breakfast_menu = self.__breakfast_menu.menu_items
        print("==== Breakfast Menu ====")
        for menu_item in breakfast_menu:
            print(menu_item)

        lunch_menu = self.__lunch_menu.menu_items
        print("==== Lunch Menu ====")
        for menu_item in lunch_menu:
            print(menu_item)

if __name__ == '__main__':
    jerome = Waiter(BreakfastMenu(), LunchMenu())
    jerome.display_menu()