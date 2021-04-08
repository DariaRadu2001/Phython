class Gast:
    
    def __init__(self): 
        self.vorname = ""
        self.nachname = ""
        self.reservierungen = []
    
    def set_vorname(self,neu_vorname):
        self.vorname = neu_vorname
    
    def set_nachname(self,neu_nachname):
        self.nachname = neu_nachname
        
    def set_reservierungen(self,neue_reservierungen):
        self.reservierungen = neue_reservierungen
    
    def __str__(self):
        return f"{self.vorname} {self.nachname}"