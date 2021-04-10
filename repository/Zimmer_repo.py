from entities.Zimmer import Zimmer


class ZimmerRepository:
    def __init__(self, file='hotel_data/Raume.txt'):
        self.__fName = file  # file name
        self.__data = []  # list of zimmer

        self.__loadFromFile()

    def add(self, zimmer):
        el = self.find(zimmer.Nummer)

        if el is not None:
            raise ValueError('Zimmer schon existiert')

        self.__data.append(zimmer)
        self.__storeToFile()

    def find(self, nummer):  # cauta dupa index camera
        for e in self.__data:
            if e.Nummer == nummer:
                return e

        return None

    def delete(self, nummer):
        el = self.find(nummer)

        if el is None:
            raise ValueError('Zimmer not found')

        idx = self.__data.index(el)
        self.__data.pop(idx)
        self.__storeToFile()

    def update(self, nummer, preis):
        el = self.find(nummer)

        if el is None:
            raise ValueError('Zimmer not found')

        idx = self.__data.index(el)
        self.__data.pop(idx)
        zimmer = Zimmer(el.Nummer, el.Anzahl, preis, el.Farbe, el.Meerblick) # fac o noua camera si o inseresz pe aia
        # el.Preis(preis) nu merge asa idk why
        self.__data.insert(idx, zimmer)

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

            zimmer = Zimmer(data[0], data[1], data[2], data[3], data[4], data[5])
            self.__data.append(zimmer)
