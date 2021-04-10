from entities.Gast import Gast
from entities.Zimmer import Zimmer
from repository.Gaste_repo import GastRepository
from repository.Zimmer_repo import ZimmerRepository
from tools.datum import *
from tkinter import messagebox
import datetime
import ast


class GemRepository:
    def __init__(self, fileG = "hotel_data/Gaste.txt", fileZ = "hotel_data/Raume.txt"):
        self.__GastfName = fileG  # file name
        self.__ZimmerfName = fileZ  # file name
        self.__Gastdata = []  # list of gaste
        self.__Zimmerdata = []  # list of gaste

        self.__GastloadFromFile()
        self.__ZimmerloadFromFile()

    def add(self, gast, zimmernummer, datum):
        ResGast = None
        for e in self.__Gastdata:
            if gast.Vorname == e.Vorname and gast.Nachname == e.Nachname:  # cauta dupa numele de familie si prenume
                ResGast = e

        if ResGast is None:
            raise ValueError('Gast not found')

        datumstr = [datum[0].strftime("%d.%m.%Y"), datum[1].strftime("%d.%m.%Y")]
        ResGast.AddRes(datumstr)

        index = None
        for i in range(len(self.__Zimmerdata)):
            if self.__Zimmerdata[i].Nummer == zimmernummer:
                index = i

        if not self.__Zimmerdata[index].AddReservirung(datumstr):
            raise ValueError

        self.__GaststoreToFile()
        self.__ZimmerstoreToFile()


    def aktueleres(self):
        data = []
        for gast in self.__Gastdata:
            if gast.ListeR:
                data.append(gast)
        return data

    def freizimmer(self, strdatum):
        zimmern = []
        datum = StringToDatum(strdatum)
        verif = True
        for Zimmer in self.__Zimmerdata:
            ok = True
            for Res in Zimmer.Freiperiode:
                if not VerifyDate(datum, datum, Res[0], Res[1]):
                    ok = False
                    break
            if ok:
                zimmern.append(Zimmer)
                verif = False

        if verif:
            raise ValueError

        return zimmern


    def __GaststoreToFile(self):
        f = open(self.__GastfName, 'w')

        for el in self.__Gastdata:
            f.write(str(el) + '\n')

        f.close()

    def __GastloadFromFile(self):
        f = open(self.__GastfName, 'r')

        for line in f:
            data = line.strip().split(';')
            gast = Gast(data[0], data[1], ast.literal_eval(data[2]))
            self.__Gastdata.append(gast)

    def __ZimmerstoreToFile(self):
        f = open(self.__ZimmerfName, 'w')

        for el in self.__Zimmerdata:
            f.write(str(el) + '\n')

        f.close()

    def __ZimmerloadFromFile(self):
        f = open(self.__ZimmerfName, 'r')

        for line in f:
            data = line.strip().split(';')
            zimmer = Zimmer(data[0], data[1], data[2], data[3], data[4], ast.literal_eval(data[5]))
            self.__Zimmerdata.append(zimmer)