from beverage import Deca, Americano, Espresso, Chocolate, Milk, Soy, Mocha, Sugar


if __name__ == '__main__':
    # serve 2 americano, 1 espresso
    # calculate the total cost
    americano_1 = Americano()
    americano_2 = Milk(Americano())
#    americano_2.sugar = True
    espresso_1 = Sugar(Soy(Espresso()))
    print(f'total cost: {americano_1.cost() + americano_2.cost() + espresso_1.cost(): .2f} €')
    print(f'{americano_1.cost()}')