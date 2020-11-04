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


#? --------------------------------------------------------------------------------------------------------------------------
#? --------------------------------------------------------------------------------------------------------------------------


# ! 27 TM 30
def VerVier_27():
    lijn58 = style.GREEN + "Na een paar uur ben je aangekomen in Ankara.\nDaar is jouw vader ook op jou aan het wachten.\nJe oom ging wel terug naar het dorp omdat hij niet mee kon.\nJullie nemen de bus naar Duitsland.\nJe kunt wel naar Duitsland omdat je vader een kort visum heeft geregeld.\nHalverwege de reis vraagt een politieagent waar je naar toe gaat.\nWat zeg je?\n\n"
    keuze27A28 = style.UNDERLINE + style.CYAN + "A: Je vertelt dat je naar Nederland gaat.\n\n"
    keuze27B29 = style.UNDERLINE + style.RED + "B: Je vertelt dat je naar Duitsland gaat.\n\n"
    for char in lijn58:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze27A28:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze27B29:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def VerVier27_28():
    lijn59 = style.GREEN + "Je hebt A gekozen.\n"
    lijn60 = style.GREEN + "Je vertelt aan de agent dat je naar Nederland gaat.\nVoor de zekerheid checkt hij jouw visum maar daar staat dat je een kort visum hebt naar Duitsland.\nJe wordt daarom teruggestuurd naar Turkije.\n\n"
    lijn61 = style.YELLOW = "Dit is een van de eindes.\nWil je het programma opnieuw gebruiken?\n\n"
    keuze28A = style.UNDERLINE + style.CYAN + "A: Ja.\n\n"
    keuze28B = style.UNDERLINE + style.RED + "B: Nee.\n\n"
    for char in lijn59:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn60:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn61:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze28A:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze28B:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def VerVier27_29():
    lijn62 = style.GREEN + "Je hebt B gekozen.\n"
    lijn63 = style.GREEN + "Je verteld aan de agent dat je naar Duitsland gaat.\nVoor de zekerheid checkt hij jouw visum.\nHij zegt: “het klopt”.\nJe gaat verder met de reis\n\n"
    keuze27A29 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn62:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn63:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze27A29:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()



#! 30 TM 32
def VerLas30():
    lijn64 = style.GREEN + "Je bent eindelijk aangekomen in Duitsland.\nJe vader heeft een auto geregeld om illegaal in Nederland te komen.\nDe reis duurt 2 uur om in Nederland te komen.\nWat doe je?\n\n"
    keuze30A31 = style.UNDERLINE + style.CYAN + "A: Je vader een idee geven om beter in Duitsland te leven.\n\n"
    keuze30B32 = style.UNDERLINE + style.RED + "B: Meegaan naar Nederland in de Auto.\n\n"
    for char in lijn64:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze30A31:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze30B32:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def VerLas30_31():
    lijn65 = style.GREEN + "Je hebt A gekozen.\n"
    lijn66 = style.GREEN + "Je geeft je vader een beter idee om in Duitsland te leven.\nHij vindt het een goed.\nJullie gingen verder leven in Duitsland.\n\n"
    lijn67 = style.YELLOW = "Dit is een van de eindes.\nWil je het programma opnieuw gebruiken?\n\n"
    keuze31A = style.UNDERLINE + style.CYAN + "A: Ja.\n\n"
    keuze31B = style.UNDERLINE + style.RED + "B: Nee.\n\n"
    for char in lijn65:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn66:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn67:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze31A:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze31B:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def VerLas30_32():
    lijn68 = style.GREEN + "Je hebt B gekozen.\n"
    lijn69 = style.GREEN + "Je neemt de auto naar Nederland.\nGelukkige was je niet gepakt tijdens de reis.\nNa een paar uur was je aangekomen in Amsterdam.\nDaar neem je de tram 13 naar Spilbergenstraat.\nEindelijk ben je bij de moeder.\nVan mei tot september mocht je niet uit het huis.\nIn september begint je school.\nJe probeerde veel Nederlands te leren maar je kan de eerste 3 jaar niet echt goed Nederlands praten.\nVoor jou duurde het in totaal 20 jaar voordat je aan Nederland kon wennen.\nJe hebt binnen de 20 jaar de Nederlandse cultuur begrepen/geaccepteerd/gerespecteerd.\nJe was illegaal in Nederland tot je 20ste.\nVerder had je een gelukkig leven in Nederland.\n\n"
    lijn70 = style.YELLOW = "Dit is een van de eindes.\nWil je het programma opnieuw gebruiken?\n\n"
    keuze32A = style.UNDERLINE + style.CYAN + "A: Ja.\n\n"
    keuze32B = style.UNDERLINE + style.RED + "B: Nee.\n\n"
    for char in lijn68:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn69:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn70:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze32A:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze32B:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")


#? Begin verhaal
VierVerhaal = True
#? Stukjes verhaal
VerVier27 = True
#? Stukjes Keuzes
VerVier27K28 = False
VerVier27K29 = False
#? Stukjes
VerVier27N28 = True
VerVier27N29 = True
# ? Credits
Credits1_28 = False
Credits2_28 = True

#? Begin verhaal
LasVerhaal = False
#? Stukjes verhaal
LasVerhaal30 = True
#? Stukjes Keuzes
VerLas30K31 = False
VerLas30K32 = False
#? Stukjes
VerLas30N31 = True
VerLas30N32 = True
# ? Credits Van 31
Credits1_31 = False
Credits2_31 = True
# ? Credits Van 31
Credits1_32 = False
Credits2_32 = True




while VierVerhaal == True:
    # ? Beginstukje van 27
    while VerVier27 == True:
        os.system("cls")
        VerVier_27()
        VerVier27 = False
    MaakeenKeuze()
    Keuze23 = input()
    if Keuze23 == "A" or Keuze23 == "a":
        print(style.RESET + "")
        os.system("cls")
        VierVerhaal = False
        VerVier27K28 = True
    elif Keuze23 == "B" or Keuze23 == "b":
        print(style.RESET + "")
        os.system("cls")
        VierVerhaal = False
        VerVier27K29 = True
    else:
        print("Geen Antwoord ontvangen.\n")
    # ! Van 27 Naar 28 (HELEMAAL EINDE)
    while VerVier27K28 == True:
        while VerVier27N28 == True:
            os.system("cls")
            VerVier27_28()
            VerVier27N28 = False
        MaakeenKeuze()
        Keuze24 = input()
        if Keuze24 == "A" or Keuze24 == "a":
            print(style.RESET + "")
            os.system("cls")
            os.system('python "Main.py"')
        elif Keuze24 == "B" or Keuze24 == "b":
            print(style.RESET + "")
            os.system("cls")
            VerVier27K28 = False
            Credits1_28 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    while Credits1_28 == True:
        while Credits2_28 == True:
            #TODO Credits()
            Credits2_28 = False
            quit()
    # ! Van 27 Naar 29 (einde 1)
    while VerVier27K29 == True:
        while VerVier27N29 == True:
            os.system("cls")
            VerVier27_29()
            VerVier27N29 = False
        MaakeenKeuze()
        Keuze25 = input()
        if Keuze25 == "A" or Keuze25 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerVier27K29 = False
            VierVerhaal = False
            LasVerhaal = True
        else:
            print("Geen Antwoord ontvangen.\n")
    #! BEGIN VAN 30 TM 30
while LasVerhaal == True:
    while LasVerhaal30 == True:
        os.system("cls")
        VerLas30()
        LasVerhaal30 = False
    MaakeenKeuze()
    Keuze26 = input()
    if Keuze26 == "A" or Keuze26 == "a":
        print(style.RESET + "")
        os.system("cls")
        LasVerhaal = False
        VerLas30K31 = True
    elif Keuze26 == "B" or Keuze26 == "b": #TODO DE LAATSTE OMG BIJNA KLAAR
        print(style.RESET + "")
        os.system("cls")
        LasVerhaal = False
        VerLas30K32 = True
    else:
        print("Geen Antwoord ontvangen.\n")
    #? VAN 30 NAAR 31 HELEMAAL EINDE
    while VerLas30K31 == True:
        while VerLas30N31 == True:
            os.system("cls")
            VerLas30_31()
            VerLas30N31 = False
        MaakeenKeuze()
        Keuze27 = input()
        if Keuze27 == "A" or Keuze27 == "a":
            print(style.RESET + "")
            os.system("cls")
            os.system('python "Main.py"')
        elif Keuze27 == "B" or Keuze27 == "b":
            print(style.RESET + "")
            os.system("cls")
            VerLas30K31 = False
            Credits1_31 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    #? 31 CREDITS EINDE
    while Credits1_31 == True:
        while Credits2_31 == True:
            Credits()
            Credits2_31 = False
            quit()
    #TODO VAN 30 NAAR 32 HELEMAAL EINDE
    while VerLas30K32 == True:
        while VerLas30N32 == True:
            os.system("cls")
            VerLas30_32()
            VerLas30N32 = False
        MaakeenKeuze()
        Keuze28 = input()
        if Keuze28 == "A" or Keuze28 == "a":
            print(style.RESET + "")
            os.system("cls")
            os.system('python "Main.py"')
        elif Keuze28 == "B" or Keuze28 == "b":
            print(style.RESET + "")
            os.system("cls")
            Credits1_32 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    while Credits1_32 == True:
        while Credits2_32 == True:
            Credits()
            Credits2_32 = False
            quit()
#? --------------------------------------------------------------------------------------------------------------------------
#? --------------------------------------------------------------------------------------------------------------------------