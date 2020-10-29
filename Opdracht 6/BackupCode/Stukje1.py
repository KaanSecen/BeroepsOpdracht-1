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

#Vraag 8 Verhaal
def middenstukje():
    lijn19 = style.YELLOW + "Jaar: 1991\n\n"
    lijn18 = style.GREEN + "Na 1 jaar zonder vader heb je echt een stuk van je jeugd gemist.\nJe bent die tijd altijd bij je moeder gebleven.\nHet is een moeilijke jaar voor jou geweest.\nJe ging op een dag naar huis.\nThuis waren al je spullen verdwenen.\nWat ga je doen?\n\n"
    keuze8A = style.UNDERLINE + style.CYAN + "A: Direct naar je oma gaan.\n\n"
    keuze8B = style.UNDERLINE + style.RED + "B: Het huis gaan doorzoeken.\n\n"
    for char in lijn19:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn18:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze8A:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze8B:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#Vraag 8 Naar 12 Stukjes
def verhaal8_9():
    lijn20 = style.GREEN + "Na 1 jaar zonder vader heb je echt een stuk van je jeugd gemist.\nJe bent die tijd altijd bij je moeder gebleven.\nHet is een moeilijke jaar voor jou geweest.\nJe gaat naar huis.\nThuis waren al je spullen verdwenen.\nWat ga je doen?\n\n"
    keuze9A = style.UNDERLINE + style.CYAN + "A: Direct naar je oma gaan.\n\n"
    keuze9B = style.UNDERLINE + style.RED + "B: Het huis gaan doorzoeken.\n\n"
    for char in lijn20:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze9A:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze9B:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def verhaal9_12():
    os.system("cls")
    lijn21 = style.GREEN + "Je hebt A gekozen.\n"
    lijn22 = style.GREEN + "Je gaat direct naar je oma.\nZe zegt dat ze slecht nieuws heeft voor jou.\nZe vertelt ook dat je moeder naar Nederland is vertrokken.\nJe oma zegt dat je daarom al je spullen van jullie huis naar haar is verplaatst.\nJe ziet je broertje binnen.\nHij zegt: “ik wil wel naar Nederland”.\nWat zeg jij?\n\n"
    keuze9A12 = style.UNDERLINE + style.CYAN + "A: Ik wil ook heel graag naar Nederland.\n\n"
    keuze9B12 = style.UNDERLINE + style.RED + "B: Ik wil liever bij mijn dorpje in Turkije blijven.\n\n"
    for char in lijn21:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn22:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze9A12:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze9B12:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    
def verhaal8_10():
    os.system("cls")
    lijn23 = style.GREEN + "Je hebt B gekozen.\n"
    lijn24 = style.GREEN + "Je zoekt het hele huis door.\nJe hebt een papiertje gevonden wat jouw moeder heeft geschreven.\nOp het papiertje staat er: “Sorry, ik ben ook naar Nederland gegaan.\nIk heb ervoor ook gezorgd dat al jouw spullen nu bij oma nu is”.\n\n"
    keuze8A10 = style.UNDERLINE + style.CYAN + "A: Naar je oma gaan.\n\n"
    for char in lijn23:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn24:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze8A10:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def verhaal10_12():
    os.system("cls")
    lijn25 = style.GREEN + "Je hebt A gekozen.\n"
    lijn26 = style.GREEN + "Je gaat naar je oma.\nJe hebt alles vertelt.\nZe vertelt dat je voorlopig hier blijft.\nJe ziet je broertje binnen.\nHij zegt: “ik wil wel naar Nederland”.\nWat zeg jij?\n\n"
    keuze10A12 = style.UNDERLINE + style.CYAN + "A: Nederland zal ik ook heel graag naartoe willen.\n\n"
    keuze10B12 = style.UNDERLINE + style.CYAN + "A: Ik blijf liever bij mijn dorpje.\n\n"
    for char in lijn25:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn26:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze10A12:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze10B12:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    
#VerhaallijnMidden
VerhaalMid = True
# Vraag 8 Tot 12 Stukken
middenstuk = True
midden8N9 = True
midden8N10 = True
midden10N12 = True
#Keuzes
verhaalmid8K9 = False
Verhaalmid8K10 = False
verhaalmid10K12 = False

#De Script voor 8 toy 12
while VerhaalMid == True:
    while middenstuk == True:
        os.system("cls")
        middenstukje()
        middenstuk = False
    MaakeenKeuze()
    Keuze8 = input()
    if Keuze8 == "A" or Keuze8 == "a":
        print(style.RESET + "")
        os.system("cls")
        VerhaalMid = False
        verhaalmid8K9 = True
    elif Keuze8 == "B" or Keuze8 == "b":
        print(style.RESET + "")
        os.system("cls")
        VerhaalMid = False
        Verhaalmid8K10 = True
    else:
        print("Geen Antwoord ontvangen.\n")
    # 8 Naar 9 Naar 12 (Eindpunt)
    while verhaalmid8K9 == True:
        print(style.RESET + "")
        while midden8N9 == True:
            verhaal9_12()
            midden8N9 = False
        MaakeenKeuze()
        Keuze9 = input()
        if Keuze9 == "A" or Keuze9 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerhaalMid = False
            verhaalmid8K9 = False
        elif Keuze9 == "B" or Keuze9 == "b":
            print(style.RESET + "")
            os.system("cls")
            verhaalMid = False
            verhaalmid8K9 = False
        else:
            print("Geen Antwoord ontvangen.\n")
    # 8 Naar 10
    while Verhaalmid8K10 == True:
        print(style.RESET + "")
        while midden8N10 == True:
            verhaal8_10()
            midden8N10 = False
        MaakeenKeuze()
        Keuze10 = input()
        if Keuze10 == "A" or Keuze10 == "a":
            print(style.RESET + "")
            os.system("cls")
            Verhaalmid8K10 = False
            verhaalmid10K12 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    # 10 Naar 12 (Eindpunt)
    while verhaalmid10K12 == True:
        print(style.RESET + "")
        while midden10N12 == True:
            verhaal9_12()
            midden10N12 = False
        MaakeenKeuze()
        Keuze11 = input()
        if Keuze11 == "A" or Keuze11 == "a":
            print(style.RESET + "")
            os.system("cls")
            VerhaalMid = False
            verhaalmid10K12 = False
        elif Keuze11 == "B" or Keuze11 == "b":
            print(style.RESET + "")
            os.system("cls")
            Verhaalmid = False
            verhaalmid10K12 = False
        else:
            print("Geen Antwoord ontvangen.\n")

os.system('python "Stukje2.py"')