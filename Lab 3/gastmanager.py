import gast

class GastManager:
    
    def __init__(self):
        self.gaste = []
    
    def neue_gast(self):
        ngast = gast.Gast()
        nvorname = input("Bitte Vorname einfuhren: ")
        nnachname = input("Bitte Nachname einfuhren: ")
        ngast.set_vorname(nvorname)
        ngast.set_nachname(nnachname)
        self.gaste.append(ngast)
    
    def actualisierung_nachname(self):
        for i in range(len(self.gaste)):
            print(str(self.gaste[i]) + f" ist gast nr. {i}")
        index = input("Bitte gast selectieren: " )
        nnachname = input("Bitte neue Nachname einfuhren: ")
        self.gaste[int(index)].set_nachname(nnachname)
        
    def losch_gast(self):
        for i in range(len(self.gaste)):
            print(str(self.gaste[i]) + f" ist gast nr. {i}")
        index = input("Bitte Gast selectieren: " )
        print(str(self.gaste.pop(int(index))) + " war geloscht" )
    
    def zeig_gaste(self):
        for i in range(len(self.gaste)):
            print(str(self.gaste[i]) + f" ist gast nr. {i}")
