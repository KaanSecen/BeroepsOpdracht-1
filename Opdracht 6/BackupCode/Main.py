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

soundObj = pygame.mixer.Sound('typing.wav')
soundObj2 = pygame.mixer.Sound('geluid.wav')

# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------
# Verhaal 
Verhaalbegin = True
# 1 TOT 3
VerhaalbeginK1 = False
VerhaalbeginK2 = False
#Verhaalstukjes
eerststuk = True
verhaalstuk2N1 = True
verhaalstuk1N3 = True
verhaalstuk3N5 = True
verhaalstuk3N4 = True
verhaalstuk4N6 = True
verhaalstuk6N7 = True
# 3 TOT 8
Verhaalbegin3K5 = False
Verhaalbegin3K4 = False
verhaalbegin4K6 = False
verhaalbegin6K7 = False

#Def voor beginstuk(Leeftijd enz)
def verhaalijnbegininfo():
    #Woorden voor het stuk.
    lijn1 = style.YELLOW + "Jaar: 1990\nLocatie: Ürgüp, Turkije\nNaam: Asya\nLeeftijd: 11 Jaar\n\n"
    lijn2 = style.UNDERLINE + style.YELLOW + "Je speelt in dit verhaal als Asya.\nMaak de keuzes voor haar goed.\n"
    #Geluiden
    soundObj.play()
    #Typing Effect
    for char in lijn1:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    soundObj.stop()
    time.sleep(2)
    soundObj.play()
    #TypingEffect
    for char in lijn2:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    soundObj.stop()


#het eerste stuk van het verhaal
def EersteKeuze():
    soundObj2.play()
    lijn3 = style.GREEN + "Je woont in een klein dorpje in Turkije.\nJe hebt een moeilijke dag achter de rug gehad.\nJe komt van school naar huis.\nWanneer je thuiskomt is je vader opeens vertrokken.\nWat doe je?\n\n"
    keuze1A = style.UNDERLINE + style.CYAN + "A: Vragen aan je moeder waar je vader is?\n\n"
    keuze1B = style.UNDERLINE + style.RED + "B: Vragen aan je broertje waar je vader is?\n\n"
    for char in lijn3:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze1A:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze1B:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#Van 1 Naar 3   
def VerhaalK1():
    os.system("cls")
    lijn5 = style.GREEN + "Je hebt A gekozen.\n"
    lijn6 = style.GREEN + "Je vraagt aan je moeder waar je vader is.\nJe moeder zegt dat je vader naar Nederland is vertrokken.\nWat doe je?\n\n"
    keuze2A = style.UNDERLINE + style.CYAN + "A: Weglopen van thuis naar je oma.\n\n"
    keuze2B = style.UNDERLINE + style.RED + "B: Vragen voor welke reden is mijn vader vertrokken?\n\n"
    for char in lijn5:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn6:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze2A:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze2B:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#Van 1 Naar 2 -> Naar 1 Terug
def VerhaalK2():
    os.system("cls")
    lijn7 = style.GREEN + "Je hebt B gekozen.\n"
    lijn8 = style.GREEN + "Je vraagt aan je broertje waar je vader is.\nHij zegt dat hij het niet weet.\n\n"
    lijn9 = style.UNDERLINE + style.CYAN + "A. Toch maar aan je moeder vragen?\n\n"
    for char in lijn7:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn8:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn9:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#Van 3 Naar 5 (Eindpunt 8)
def Verhaal3_5():
    os.system("cls")
    lijn10 = style.GREEN + "Je hebt B gekozen.\n"
    lijn11 = style.GREEN + "Je moeder legt je uit dat je vader naar Nederland is gegaan om economische reden.\nJe moeder zegt ook dat je vader binnenkort weer terugkomt.\nJe hebt veel vertrouwen in je ouders verloren door deze gebeurtenis\n\n"
    keuze3A5 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn10:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn11:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze3A5:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#Van 3 Naar 4
def Verhaal3_4():
    os.system("cls")
    lijn12 = style.GREEN + "Je hebt A gekozen.\n"
    lijn13 = style.GREEN + "Je loopt weg van huis naar je huis van je oma.\nWanneer je aan de deur belt vraagt je oma wat je hier doet.\nWat zeg je?\n\n"
    keuze3A4 = style.UNDERLINE + style.CYAN + "A: Vertellen wat er echt is gebeurd.\n\n"
    keuze3B4 = style.UNDERLINE + style.RED + "B: Liegen over wat er echt is gebeurd.\n\n"
    for char in lijn12:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn13:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze3A4:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze3B4:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#Van 4 Naar 6
def Verhaal4_6():
    os.system("cls")
    lijn14 = style.GREEN + "Je hebt B gekozen.\n"
    lijn15 = style.GREEN + "Je liegt over wat er was gebeurd.\nJe vertelt dat je hier mocht slapen van je ouders.\nJe oma is je moeder bellen om te vragen of dat waar is.\nZe hoort dat het niet waar was.\nJe oma zegt: “Waarom lieg je tegen mij?”\n\n"
    keuze3A4 = style.UNDERLINE + style.CYAN + "A: Toch vertellen wat er echt is gebeurd.\n\n"
    for char in lijn14:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn15:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze3A4:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
#Van 6 Naar 7 (Eindpunt 8)
def Verhaal6_7():
    os.system("cls")
    lijn16 = style.GREEN + "Je hebt A gekozen.\n"
    lijn17 = style.GREEN + "Je vertelt aan je oma dat je vader opeens was vertrokken is.\nJe oma belt je moeder om te vragen wat er is gebeurd.\nJe moeder vertelt aan de telefoon dat je vader voor economische reden naar Nederland is gegaan.\nJe hebt veel vertrouwen in je ouders verloren door deze gebeurtenis.\nJe slaapt de nacht verder bij je oma.\nDe volgende dag ga je weer naar je moeder.\n\n"
    keuze6A7 = style.UNDERLINE + style.CYAN + "A: ...\n\n"
    for char in lijn16:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in lijn17:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in keuze6A7:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


#Speelt het beginstuk af
verhaalijnbegininfo()
print(style.RESET + "")


#je eerste keuzes
while Verhaalbegin == True:
    while eerststuk == True:
            EersteKeuze()
            eerststuk = False
    MaakeenKeuze()
    Keuze1 = input()
    #Keuze van A of B
    if Keuze1 == "A" or Keuze1 == "a":
        VerhaalbeginK1 = True
        Verhaalbegin = False
        os.system("cls")
    elif Keuze1 == "B" or Keuze1 == "b":
        VerhaalbeginK2 = True
        Verhaalbegin = False
        os.system("cls")
    else:
        print("Geen Antwoord ontvangen.\n")
    # Vraag 2 Naar 1
    while VerhaalbeginK2 == True:
        print(style.RESET + "")
        while verhaalstuk2N1 == True:
            VerhaalK2()
            verhaalstuk2N1 = False
        MaakeenKeuze()
        Keuze2 = input()
        if Keuze2 == "A" or Keuze2 == "a":
            print(style.RESET + "")
            os.system("cls")
            Verhaalbegin = True
            eerststuk = True
            VerhaalbeginK2 = False
        else:
            print("Geen Antwoord ontvangen.\n")
    #Vraag 1 Naar 3
    while VerhaalbeginK1 == True:
        print(style.RESET + "")
        while verhaalstuk1N3 == True:
            VerhaalK1()
            verhaalstuk1N3 = False
        MaakeenKeuze()
        Keuze3 = input()
        if Keuze3 == "A" or Keuze3 == "a":
            print(style.RESET + "")
            Verhaalbegin3K4 = True
            VerhaalbeginK1 = False
        elif Keuze3 == "B" or Keuze3 == "b":
            print(style.RESET + "")
            Verhaalbegin3K5 = True
            VerhaalbeginK1 = False
            os.system("cls")
        else:
            print("Geen Antwoord ontvangen.\n")
    #Vraag 3 Naar 5 (Naar 8 Eindepunt)
    while Verhaalbegin3K5 == True:
        print(style.RESET + "")
        while verhaalstuk3N5 == True:
            Verhaal3_5()
            verhaalstuk3N5 = False
        MaakeenKeuze()
        Keuze4 = input()
        if Keuze4 == "A" or Keuze4 == "a":
            print(style.RESET + "")
            os.system("cls")
            Verhaalbegin = False
            Verhaalbegin3K5 = False
        else:
            print("Geen Antwoord ontvangen.\n")
    #Vraag 3 Naar 4
    while Verhaalbegin3K4 == True:
        print(style.RESET + "")
        while verhaalstuk3N4 == True:
            Verhaal3_4()
            verhaalstuk3N4 = False
        MaakeenKeuze()
        Keuze5 = input()
        if Keuze5 == "A" or Keuze5 == "a":
            print(style.RESET + "")
            os.system("cls")
            verhaalbegin6K7 = True
            Verhaalbegin3K4 = False
        elif Keuze5 == "B" or Keuze5 == "b":
            print(style.RESET + "")
            os.system("cls")
            verhaalbegin4K6 = True
            Verhaalbegin3K4 = False
        else:
            print("Geen Antwoord ontvangen.\n")
    #Vraag 4 Naar 6
    while verhaalbegin4K6 == True:
        print(style.RESET + "")
        while verhaalstuk4N6 == True:
            Verhaal4_6()
            verhaalstuk4N6 = False
        MaakeenKeuze()
        Keuze6 = input()
        if Keuze6 == "A" or Keuze6 == "a":
            print(style.RESET + "")
            os.system("cls")
            verhaalbegin4K6 = False
            verhaalbegin6K7 = True
        else:
            print("Geen Antwoord ontvangen.\n")
    #Vraag 6 Naar 7 (Eind stuk)
    while verhaalbegin6K7 == True:
        print(style.RESET + "")
        while verhaalstuk6N7 == True:
            Verhaal6_7()
            verhaalstuk6N7 = False
        MaakeenKeuze()
        Keuze7 = input()
        if Keuze7 == "A" or Keuze7 == "a":
            print(style.RESET + "")
            os.system("cls")
            Verhaalbegin = False
            verhaalbegin6K7 = False
        else:
            print("Geen Antwoord ontvangen.\n")

os.system('python "Stukje1.py"')