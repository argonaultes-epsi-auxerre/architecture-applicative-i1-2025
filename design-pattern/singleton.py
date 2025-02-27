class Chevre:
    pass

# variable de classe
# methode de classe

class Berger:
    __berger = None

    @classmethod
    def get_instance(cls):
        if cls.__berger is None:
            cls.__berger = Berger()
        return cls.__berger


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

    berger_2 = Berger() # est-ce que berger_2 est bien identique à berger_1 ?
    assert berger_1 == berger_2