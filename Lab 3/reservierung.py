import datetime
class Reservierung:
    
    def __init__(self):
        self.gaste = []
        self.zimmer = -1
        self.checkindate = datetime.date.today()
        self.checkoutdate = datetime.date.today()
        self.zeitraum = self.checkindate - self.checkoutdate
    
    def add_gast(self,neue_gast):
        self.gaste.append(neue_gast)
    
    def set_zimmer(self,neue_zimmer):
        self.zimmer = neue_zimmer
    
    def set_checkindate(self,neue_checkindate):
        self.checkindate = neue_checkindate
        
    def set_checkoutdate(self,neue_checkoutdate):
        self.checkoutdate = neue_checkoutdate
    
    def reset_zeitraum(self):
        self.zeitraum = self.checkoutdate - self.checkindate