class Zimmer:
    
    def __init__(self):
        self.nr = -1
        self.maxanzahl = -1
        self.preis = -1
        self.farbe = ""
        self.meerblick = False
        self.frei = True
        
    def __str__(self):
        return f"Zimmer nr.: {self.nr},maximum anzahl von gaste: {self.maxanzahl},preis: {self.preis},meerblick: {self.meerblick},farbe:{self.farbe},ist frei: {self.frei}."
    
    def set_nummer(self,neue_nummer):
        self.nr = neue_nummer
    
    def set_maxanzahl(self,neue_maxanzahl):
        self.maxanzahl = neue_maxanzahl
    
    def set_preis(self,neue_preis):
        self.preis = neue_preis
        
    def set_farbe(self,neue_farbe):
        self.farbe = neue_farbe
        
    def set_meerblick(self,neue_meerblick):
        self.meerblick = neue_meerblick
        
    def set_frei(self,neue_frei):
        self.frei = neue_frei