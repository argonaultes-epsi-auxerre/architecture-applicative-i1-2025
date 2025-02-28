class Chevre:
    pass

# variable de classe
# methode de classe

class BergerNaive:
    __berger = None

    @classmethod
    def get_instance(cls):
        if cls.__berger is None:
            cls.__berger = Berger()
        return cls.__berger


class SingletonBerger(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):

        print(f'_instances: {cls._instances}')
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Berger(metaclass=SingletonBerger):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...



class Troupeau:

    def __init__(self):
        self.__chevres = []


    def add_chevre(self, chevre):
        self.__chevres.append(chevre)

if __name__ == '__main__':
    troupeau = Troupeau()
    for _ in range(10):
        troupeau.add_chevre(Chevre())
    berger_1 = Berger()
    print(f'berger_1: {berger_1}')

    berger_2 = Berger() # est-ce que berger_2 est bien identique à berger_1 ?
    print(f'berger_2: {berger_2}')
    assert berger_1 == berger_2