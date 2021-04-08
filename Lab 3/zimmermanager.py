import zimmer

class ZimmerManager:
    
    def __init__(self):
        self.zimmern = []
    
    def neue_zimmern(self): 
        nzimmer = zimmer.Zimmer()
        while True:
            try:
                nnummer = int(input("Bitte Zimmer Nr eingeben: "))
            except:
                print("Ein integer bitte!")
                continue
            else:
                nzimmer.set_nummer(nnummer)
                break
        
        while True:
            try:
                nanzahl = int(input("Bitte maximale Nummer von Gaste eingeben: "))
            except:
                print("Ein integer bitte")
                continue
            else:
                nzimmer.set_maxanzahl(nanzahl)
                break
        
        while True:
            try:
                npreis = int(input("Bitte preis eingeben: "))
            except:
                print("Ein integer bitte")
                continue
            else:
                nzimmer.set_preis(int(npreis))
                break
        
        nfarbe = input("Bitte farbe eingeben: ")
        nzimmer.set_farbe(nfarbe)
        nmeerblick = ""
        while nmeerblick != "Y" and nmeerblick != "N":
            nmeerblick = input("Bitte sagen ob diese Zimmer ein Meerblick hat(Y/N): ")
        if nmeerblick == "Y":
            nzimmer.set_meerblick(True)
        self.zimmern.append(nzimmer)
        
    def actualisierung_preis(self):
        for i in range(len(self.zimmern)):
            print(str(self.zimmern[i]) + f" hat laufende Nummern: {i}")
        index = input("Bitte Zimmer selectieren: " )
        npreis = input("Bitte neue Preis eingeben")
        self.zimmern[int(index)].set_preis(npreis)
        
    def losch_zimmer(self):
        for i in range(len(self.zimmern)):
            print(str(self.zimmern[i]) + f" hat laufende Nummern: {i}")
        index = input("Bitte Zimmer selectieren: " )
        print(str(self.zimmern.pop(int(index))) + " war geloscht" )
        
    def zeig_zimmern(self):
        for i in range(len(self.zimmern)):
            print(str(self.zimmern[i]) + f" ist Zimmer mit laufende Nummern. {i}")
            
    def filt_zimmern(self):
        maxpreis = int(input("Bitte maximale Preis einfugen: "))
        meerblick = ""
        while meerblick != "Y" and meerblick != "N":
            meerblick = input("Bitte sagen ob diese Zimmer ein Meerblick hat(Y/N): ")
        if meerblick == "Y":
            meerblick = True
        else:
            meerblick = False
        for zimmer in self.zimmern:
            if(zimmer.preis < maxpreis and zimmer.meerblick == meerblick):
                print(zimmer)
    
    def zeig_frei(self):
        for zimmer in self.zimmern:
            if zimmer.frei:
                print(zimmer)