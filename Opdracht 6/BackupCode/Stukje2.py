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

#Vraag 12 Verhaal
def helftstukje():
    lijn28 = style.GREEN + "Een paar dagen later vertelt je oma dat ze je moeder en vader aan de telefoon heeft.\nJe oma zegt dat je ouders met jou willen praten.\nWat doe je?\n\n"
    keuze12A14 = style.UNDERLINE + style.CYAN + "A: Praten met je ouders aan de telefoon.\n\n"
    keuze12B13 = style.UNDERLINE + style.RED + "B: Niet praten met je ouders aan de telefoon.\n\n"
    for char in lijn28:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze12A14:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze12B13:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def helft12_14():
    lijn29 = style.GREEN + "Je hebt A gekozen.\n"
    lijn30 = style.GREEN + "Je oma geeft de telefoon aan jou om te praten met je ouders.\nJe bent aan de lijn met je ouders.\nWat ga je vragen?\n\n"
    keuze14A17 = style.UNDERLINE + style.CYAN + "A: Wanneer komen jullie terug naar Turkije?\n\n"
    keuze14B18 = style.UNDERLINE + style.RED + "B: Moeten we ook ooit naar Nederland komen?\n\n"
    for char in lijn29:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn30:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze14A17:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze14B18:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def helft12_13():
    lijn36 = style.GREEN + "Je hebt B gekozen.\n"
    lijn37 = style.GREEN + "Je oma vraagt waarom je niet met je ouders wilt gaan praten aan de telefoon.\nWat zeg je?\n\n"
    keuze12A13 = style.UNDERLINE + style.CYAN + "A: Liegen over iets dat je ouders niet hebben gedaan.\n\n"
    keuze12B13 = style.UNDERLINE + style.RED + "B: Zeggen dat je nu niet met ze wilt praten.\n\n"
    for char in lijn36:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn37:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze12A13:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze12B13:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def helft13_16():
    lijn38 = style.GREEN + "Je hebt B gekozen.\n"
    lijn39 = style.GREEN + "Je zegt tegen je oma dat je niet nu met ze wilt praten.\nZe begrijpt dat je nu niet wilt praten.\n\n"
    keuze13A16 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn38:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn39:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze13A16:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def helft14_17():
    lijn33 = style.GREEN + "Je hebt A gekozen.\n"
    lijn32 = style.GREEN + "Je vraagt de vraag aan je vader.\nHij zegt dat zegt dat hij denkt dat ze binnenkort wel terug naar Turkije gaan komen.\n\n"
    keuze14A17 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn33:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn32:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze14A17:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def helft14_18():
    lijn34 = style.GREEN + "Je hebt B gekozen.\n"
    lijn35 = style.GREEN + "Je vraagt de vraag aan je moeder.\nJe moeder zegt dat ze dat niet weet.\n\n"
    keuze14A18 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn34:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn35:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze14A18:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def helft13_15():
    lijn40 = style.GREEN + "Je hebt A gekozen.\n"
    lijn41 = style.GREEN + "Je liegt over iets dat je ouders niet hebben gedaan.\nJe oma weet dat je aan het liegen bent.\n\n"
    keuze13A15 = style.UNDERLINE + style.CYAN + "A: Toch maar zeggen dat je niet wilt ze wilt praten.\n\n"
    for char in lijn40:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn41:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze13A15:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def helft15_16():
    lijn42 = style.GREEN + "Je hebt A gekozen.\n"
    lijn43 = style.GREEN + "Je zegt tegen je oma dat je niet nu met ze wilt praten.\nZe zegt dat je niet meer moet gaan liegen.\n\n"
    keuze15A16 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn42:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn43:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze15A16:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#VerhaalHelft
VerhaalHelft = True
# Vraag 12 Tot 20
helftverhaal = True
# 12 Naar 14 Kant
helft12N14 = True
helft14N17 = True
helft14N18 = True
helft17N20 = True
helft18N20 = True
# 12 Naar 13 Kant
helft12N13 = True
helft13N15 = True
helft13N16 = True
helft15N16 = True
helft16N20 = True
#Keuzes 12 Naar 14 Kant
helft12K14 = False
helft14K17 = False
helft14K18 = False
helft17N20 = False
helft18N20 = False
# Keuze 12 Naar 13 Kant
helft12K13 = False
helft13K15 = False
helft15K16 = False
helft13K16 = False
helft16K20 = False


# Script voor 12 tot 20
while VerhaalHelft == True:
    while helftverhaal == True:
        os.system("cls")
        helftstukje()
        helftverhaal = False
    MaakeenKeuze()
    Keuze12 = input()
    if Keuze12 == "A" or Keuze12 == "a":
        print(style.RESET + "")
        os.system("cls")
        VerhaalHelft = False
        helft12K14 = True
    elif Keuze12 == "B" or Keuze12 == "b": # Deze maak ik Nu naar 13
        print(style.RESET + "")
        os.system("cls")
        VerhaalHelft = False
        helft12K13 = True
    else:
        print("Geen Antwoord ontvangen.\n")
    #12 Naar 14
    while helft12K14 == True:
        while helft12N14 == True:
            os.system("cls")
            helft12_14()
            helft12N14 = False
        MaakeenKeuze()
        Keuze13 = input()
        if Keuze13 == "A" or Keuze13 == "a":
            print(style.RESET + "")
            os.system("cls")
            helft12K14 = False
            helft14K17 = True
        elif Keuze13 == "B" or Keuze13 == "b":
            print(style.RESET + "")
            os.system("cls")
            helft12K14 = False
            helft14K18 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    #14 Naar 17 Eindpunt 1
    while helft14K17 == True:
        while helft14N17 == True:
            os.system("cls")
            helft14_17()
            helft14N17 = False
        MaakeenKeuze()
        Keuze14 = input()
        if Keuze14 == "A" or Keuze14 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerhaalHelft = False
            helft14K17 = False
        else:
            print("Geen Antwoord ontvangen.\n")
    # 14 Naar 18 Eindpunt 2
    while helft14K18 == True:
        while helft14N18 == True:
            os.system("cls")
            helft14_18()
            helft14N18 = False
        MaakeenKeuze()
        Keuze15 = input()
        if Keuze15 == "A" or Keuze15 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerhaalHelft = False
            helft14K18 = False
        else:
            print("Geen Antwoord ontvangen.\n")
    # Vraag 12 Naar 13
    while helft12K13 == True:
        while helft12N13 == True:
            os.system("cls")
            helft12_13()
            helft12N13 = False
        MaakeenKeuze()
        Keuze16 = input()
        if Keuze16 == "A" or Keuze16 == "a":
            print(style.RESET + "")
            os.system("cls")
            helft12K13 = False
            helft13K15 = True
        elif Keuze16 == "B" or Keuze16 == "b":
            print(style.RESET + "")
            os.system("cls")
            helft12K13 = False
            helft13K16 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    # Vraag 13 Naar 16 (Eindpunt 1)
    while helft13K16 == True:
        while helft13N16 == True:
            os.system("cls")
            helft13_16()
            helft13N16 = False
        MaakeenKeuze()
        Keuze17 = input()
        if Keuze17 == "A" or Keuze17 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerhaalHelft = False
            helft13K16 = False
        else:
            print("Geen Antwoord ontvangen.\n")
    # Vraag 13 Naar 15
    while helft13K15 == True:
        while helft13N15 == True:
            os.system("cls")
            helft13_15()
            helft13N15 = False
        MaakeenKeuze()
        Keuze18 = input()
        if Keuze18 == "A" or Keuze18 == "a":
            print(style.RESET + "")
            os.system("cls")
            helft13K15 = False
            helft15K16 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    # 15 Naar 16 (Eindpunt)
    while helft15K16 == True:
        while helft15N16 == True:
            os.system("cls")
            helft15_16()
            helft15N16 = False
        MaakeenKeuze()
        Keuze19 = input()
        if Keuze19 == "A" or Keuze19 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerhaalHelft = False
            helft15K16 = False
        else:
            print("Geen Antwoord ontvangen.\n")

os.system('python "Stukje3.py"')
