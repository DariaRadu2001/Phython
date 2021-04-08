import reservierung
import datetime
class ReservierungManager:
    
    def __init__(self,gm,zm):
        self.reservierungen = []
        self.gm = gm
        self.zm = zm
           
        
    def neue_reservierung(self):
        nreservierung = reservierung.Reservierung()
        noch_eine_gast = True
        while noch_eine_gast:
            self.gm.zeig_gaste()
            index = input("Bitte Gast selectieren: " )
            nreservierung.add_gast(self.gm.gaste[int(index)])
            nochgast = ""
            while nochgast != "Y" and nochgast != "N":
                nochgast = input("Bitte sagen ob noch ein Gast in dieser Reservierung ist?(Y/N): ")
            if nochgast == "N":
                noch_eine_gast = False
        self.zm.zeig_zimmern()
        index = input("Bitte Zimmer selectieren: " )
        nreservierung.set_zimmer(self.zm.zimmern[int(index)])
        while True: 
            try:
                checkin_tag = int(input("Bitte checkin Tag eingeben(dd): "))
                checkin_monat = int(input("Bitte checkin Monat eingeben(mm): "))
                checkin_jahr = int(input("Bitte checkin Jahr eingeben(yyyy): "))
                checkintag = datetime.date(checkin_jahr,checkin_monat,checkin_tag)
                nreservierung.set_checkindate(checkintag)
            except:
                print("Es war ein error, bitte nochmal!")
                continue
            else:
                break
        while True:
            try:
                checkout_tag = int(input("Bitte checkout Tag eingeben(dd): "))
                checkout_monat = int(input("Bitte checkout Monat eingeben(mm): "))
                checkout_jahr = int(input("Bitte checkout Jahr eingeben(yyyy): "))
                checkouttag = datetime.date(checkout_jahr,checkout_monat,checkout_tag)   
                nreservierung.set_checkoutdate(checkouttag)
            except:
                print("Es war ein error, bitte nochmal!")
                continue
            else:
                break
            
        if checkintag <= datetime.date.today() <= checkouttag:
            self.zm.zimmern[int(index)].set_frei(False)
        
        nreservierung.reset_zeitraum()
        
        self.reservierungen.append(nreservierung)
        
    def zeig_gaste_mit_reservierung(self):
        for res in self.reservierungen:
            for gast in res.gaste:
                print(gast)