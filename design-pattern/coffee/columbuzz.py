from beverage import Deca, Americano, Espresso, Chocolate


if __name__ == '__main__':
    # serve 2 americano, 1 espresso
    # calculate the total cost
    americano_1 = Americano()
    americano_2 = Americano()
    espresso_1 = Espresso()
    print(f'total cost: {americano_1.cost() + americano_2.cost() + espresso_1.cost()} €')