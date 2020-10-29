# Imports
import os
import sys
import datetime
import time
import pygame

pygame.mixer.init()
os.system("")
os.system("cls")

#Kleur Codes
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

#Maak een Keuze Tekst
def MaakeenKeuze():
    lijn4 = style.UNDERLINE + style.GREEN + "Maak een Keuze.\n\n"
    for char in lijn4:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------

def VerDer20_23():
    lijn46 = style.GREEN + "Je hebt C gekozen.\n"
    lijn47 = style.GREEN + "Je vertelt aan je oom dat je liever in Turkije wilt blijven.\nHij vindt het goed en neemt alleen jouw broertje mee naar Ankara.\nJij hebt verder een gelukkig leven verder in Turkije.\n\n"
    lijn48 = style.YELLOW = "Dit is een van de eindes.\nWil je het programma opnieuw gebruiken?\n\n"
    keuze20A23 = style.UNDERLINE + style.CYAN + "A: Ja.\n\n"
    keuze20B23 = style.UNDERLINE + style.RED + "B: Nee.\n\n"
    for char in lijn46:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn47:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn48:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze20A23:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze20B23:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def Credits():
    lijn49 = style.GREEN + "Mede mogelijk gemaakt door:\n"
    lijn50 = style.UNDERLINE + style.GREEN + "Asya (Nieuwkomer)\nKaan Secen\nPygame (Geluid)\nRuben (Tekst naar spraak)\n\n"
    for char in lijn49:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn50:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def VerDer20_21():
    lijn51 = style.GREEN + "Je hebt A gekozen.\n"
    lijn52 = style.GREEN + "Je neemt afscheid van je familie.\nDaarna ging je in auto om samen met je broertje en je oom naar Ankara te gaan.\n\n"
    keuze20A21 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn51:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn52:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze20A21:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def VerDer20_22():
    lijn53 = style.GREEN + "Je hebt B gekozen.\n"
    lijn54 = style.GREEN + "Je gaat voordat je naar Nederland gaat afscheid nemen van je vrienden.\nZij vragen waar je naar toe gaat.\nWat zeg je?\n\n"
    keuze20A22 = style.UNDERLINE + style.CYAN + "A: Dat je naar Nederland gaat.\n\n"
    keuze20B22 = style.UNDERLINE + style.RED + "B: Liegen dat je even op vakantie in Turkije gaat.\n\n"
    for char in lijn53:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn54:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze20A22:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze20B22:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def VerDer22_25():
    lijn55 = style.GREEN + "Je hebt A gekozen.\n"
    lijn56 = style.GREEN + "Je zegt dat je naar Nederland gaat.\nDaarna neem je afscheid van je vrienden.\nEen uur later ging je in auto om samen met je broertje en je oom naar Ankara te gaan.\n\n"
    keuze22A25 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn55:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn56:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze22A25:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def VerDer22_24():
    lijn57 = style.GREEN + "Je hebt B gekozen.\n"
    lijn58 = style.GREEN + "Je liegt over dat je in Turkije naar vakantie gaat.\nJe vrienden wisten dat je aan het liegen bent.\nZe vertellen dat je oom het aan hun al hebben vertelt dat je naar Nederland gaat.\n\n"
    keuze22A24 = style.UNDERLINE + style.CYAN + "A: Sorry zeggen en toch vertellen dat je naar Nederland gaat.\n\n"
    for char in lijn57:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn58:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze22A24:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def VerDer20E():
    lijn44 = style.YELLOW + "Jaar: 1992\n\n"
    lijn45 = style.GREEN + "Op een dag heb je bezoek van je vader.\nHij is van Nederland naar Turkije gekomen.\nHet probleem is dat hij na een paar dagen weer is vertrokken naar Ankara (plaats in Turkije).\nDe volgende dag op school komt de directie binnen jouw klas om te vertellen dat je naar Nederland moet gaan.\nHet blijkt dat je vader een reis heeft geregeld naar Nederland.\nJe oom brengt je naar Ankara (Naar je vader).\nJe hebt een 1 uur daarna moet je gaan met je oom.\nWat doe je?\n\n"
    keuze20A21 = style.UNDERLINE + style.CYAN + "A: Afscheid nemen van je familieleden in Turkije.\n\n"
    keuze20B22 = style.UNDERLINE + style.RED + "B: Afscheid nemen van je vrienden in Turkije.\n\n"
    keuze20C23 = style.UNDERLINE + style.YELLOW + "C: In Turkije blijven en niet naar Nederland gaan.\n\n"
    for char in lijn44:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn45:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze20A21:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze20B22:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze20C23:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#VerhaalDer 20 tot 27
DerVerhaal = True
#Derde Verhaal-1
VerDer20 = True
#20 Naar 23 (HELEMAAL Einde 1)
VerDer20N23 = True
#20 Naar 21 Naar 27 (Einde)
VerDer20N21 = True
#20 Naar 27 (Eindes)
VerDer20N22 = True
VerDer22N24 = True
VerDer24N25 = True
VerDer22N25 = True
# Keuzes
VerDer20K23 = False
VerDer20K21 = False
VerDer20K22 = False
VerDer22K25 = False
VerDer22K24 = False
VerDer24K25 = False
#Credits
Credits1 = False
Credits2 = True

while DerVerhaal == True:
    while VerDer20 == True:
        os.system("cls")
        VerDer20E()
        VerDer20 = False
    MaakeenKeuze()
    Keuze17 = input()
    if Keuze17 == "A" or Keuze17 == "a":
        print(style.RESET + "")
        os.system("cls")
        DerVerhaal = False
        VerDer20K21 = True
    elif Keuze17 == "B" or Keuze17 == "b":
        print(style.RESET + "")
        os.system("cls")
        DerVerhaal = False
        VerDer20K22 = True
    elif Keuze17 == "C" or Keuze17 == "c":
        print(style.RESET + "")
        os.system("cls")
        VerDer20 = False
        VerDer20K23 = True
    else:
        print("Geen Antwoord ontvangen.\n")
    #20 Naar 23 Helemaal Einde 1
    while VerDer20K23 == True:
        while VerDer20N23 == True:
            os.system("cls")
            VerDer20_23()
            VerDer20N23 = False
        MaakeenKeuze()
        Keuze18 = input()
        if Keuze18 == "A" or Keuze18 == "a":
            print(style.RESET + "")
            os.system("cls")
            os.system('python "Main.py"')
        elif Keuze18 == "B" or Keuze18 == "b":
            print(style.RESET + "")
            os.system("cls")
            VerDer20K23 = False
            Credits1 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    while Credits1 == True:
        while Credits2 == True:
            Credits()
            Credits2 = False
            quit()
    # 20 Naar 21 Naae 27 (Einde deze kant)
    while VerDer20K21 == True:
        while VerDer20N21 == True:
            os.system("cls")
            VerDer20_21()
            VerDer20N21 = False
        MaakeenKeuze()
        Keuze19 = input()
        if Keuze19 == "A" or Keuze19 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerDer20K21 = False
            DerVerhaal = False
        else:
            print("Geen Antwoord ontvangen.\n")
    # Van 20 Naar 22 
    while VerDer20K22 == True:
        while VerDer20N22 == True:
            os.system("cls")
            VerDer20_22()
            VerDer20N22 = False
        MaakeenKeuze()
        Keuze20 = input()
        if Keuze20 == "A" or Keuze20 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerDer20K22 = False
            VerDer22K25 = True
        elif Keuze20 == "B" or Keuze20 == "b": #Deze ga ik nu maken
            print(style.RESET + "")
            os.system("cls")
            VerDer20K22 = False
            VerDer22K24 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    # Van 22 Naar 25 (Einde stuk 1)
    while VerDer22K25 == True:
        while VerDer22N25 == True:
            os.system("cls")
            VerDer22_25()
            VerDer22N25 = False
        MaakeenKeuze()
        Keuze21 = input()
        if Keuze21 == "A" or Keuze21 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerDer22K25 = False
            DerVerhaal = False
        else:
            print("Geen Antwoord ontvangen.\n")
    # Van 22 Naar 24 
    while VerDer22K24 == True:
        while VerDer22N24 == True:
            os.system("cls")
            VerDer22_24()
            VerDer22N24 = False
        MaakeenKeuze()
        Keuze22 = input()
        if Keuze22 == "A" or Keuze22 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerDer22K24 = False
            VerDer24K25 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    # Van 24 naar 25 (Eindestuk)
    while VerDer24K25 == True:
        while VerDer24N25 == True:
            os.system("cls")
            VerDer22_25()
            VerDer24N25 = False
        MaakeenKeuze()
        Keuze23 = input()
        if Keuze23 == "A" or Keuze23 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerDer24K25 = False
            DerVerhaal = False
        else:
            print("Geen Antwoord ontvangen.\n")

os.system('python "Stukje4.py"')