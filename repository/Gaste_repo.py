from entities.Gast import Gast


class GastRepository:
    def __init__(self, file="hotel_data/Gaste.txt"):
        self.__fName = file  # file name
        self.__data = []  # list of gaste

        self.__loadFromFile()

    def add(self, gast):
        self.__data.append(gast)
        self.__storeToFile()

    def find(self, gast):
        for e in self.__data:
            if gast.Vorname == e.Vorname and gast.Nachname == e.Nachname:  # cauta dupa numele de familie si prenume
                return e

        return None

    def update(self, gast, neu):
        el = self.find(gast)

        if el is None:
            raise ValueError('Gast not found')

        idx = self.__data.index(el)
        self.__data.pop(idx)
        # self.__data.remove(el)
        gast2 = Gast(gast.Vorname, neu)
        self.__data.insert(idx, gast2)
        # self.__data.insert(-1, uni)

        self.__storeToFile()

    def delete(self, gast):
        el = self.find(gast)

        if el is None:
            raise ValueError('Gast not found')

        idx = self.__data.index(el)
        self.__data.pop(idx)

        self.__storeToFile()

    def __storeToFile(self):
        f = open(self.__fName, 'w')

        for el in self.__data:
            f.write(str(el) + '\n')

        f.close()

    def __loadFromFile(self):
        f = open(self.__fName, 'r')

        for line in f:
            data = line.strip().split(';')

            gast = Gast(data[0], data[1])
            self.__data.append(gast)
