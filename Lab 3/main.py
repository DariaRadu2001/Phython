
import datetime
from IPython.display import clear_output
import gast
import gastmanager
import zimmer
import zimmermanager
import reservierung
import reservierungmanager

GM = gastmanager.GastManager()
ZM = zimmermanager.ZimmerManager()
RV = reservierungmanager.ReservierungManager(GM,ZM)

def askint(mi,ma):
    while True:
        try:
            val = int(input("Bitte ein integer einfugen "))
        except:
            print("Ein integer bitte!")
            continue
        else:
            if val > ma or val < mi:
                print("Integer war zu gross oder zu klein")
                continue
            return val


def show_main_menu():
  #  clear_output()
    print("1. Menu Gaste")
    print("2. Menu Zimmer")
    print("3. Menu Gemeinsam")
    print("4. Exit")
    #option = int(input("Bitte ein integer einfugen um die option zu benutzen: "))
    option = askint(1,4)
    if option == 1:
        show_menu_gaste()
    if option == 2:
        show_menu_zimmern()
    if option == 3:
        show_menu_gemeinsam()
    if option == 4:
        return False
    return True

def show_menu_gaste():
    clear_output()
    print("1. Fuge ein neuer Gast hin")
    print("2. Actualisierung der Nachname eines Gastes")
    print("3. Loschung eines Gastes")
    print("4. Anzeige die Liste von Gasten")
    print("5. Main Menu")
    #option = int(input("Bitte ein integer einfugen um die option zu benutzen: "))
    option = askint(1,5)
    if option == 1:
        GM.neue_gast()
    elif option == 2:
        GM.actualisierung_nachname()
    elif option == 3:
        GM.losch_gast()
    elif option == 4:
        GM.zeig_gaste()
    elif option == 5:
        show_main_menu()

def show_menu_zimmern():
    clear_output()
    print("1. Fuge ein Zimmer hin")
    print("2. Actualisierung des Preises eines Zimmers")
    print("3. Loschung eines Zimmers")
    print("4. Anzeige die Liste von Zimmern")
    print("5. Main Menu")
    #option = int(input("Bitte ein integer einfugen um die option zu benutzen: "))
    option = askint(1,5)
    if option == 1:
        ZM.neue_zimmern()
    elif option == 2:
        ZM.actualisierung_preis()
    elif option == 3:
        ZM.losch_zimmer()
    elif option == 4:
        ZM.zeig_zimmern()
    elif option == 5:
        show_main_menu()

def show_menu_gemeinsam():
    clear_output()
    print("1. Mach eine Reservierung")
    print("2. Anzeige die Liste von Gasten die aktuelle Reservierungen haben")
    print("3. Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien")
    print("4. Anzeige alle Zimmer , die heute frei sind")
    print("5. Main Menu")
    #option = int(input("Bitte ein integer einfugen um die option zu benutzen: "))
    option = askint(1,5)
    if option == 1:
        RV.neue_reservierung()
    elif option == 2:
        RV.zeig_gaste_mit_reservierung()
    elif option == 3:
        ZM.filt_zimmern()
    elif option == 4:
        ZM.zeig_frei()
    elif option == 5:
        show_main_menu()

while show_main_menu() != False:
    pass
       