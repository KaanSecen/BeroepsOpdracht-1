# Imports
import os
import sys
import datetime
import time

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
    time.sleep(2)
    soundObj3.play()
    lijn4 = style.UNDERLINE + style.GREEN + "Maak een Keuze.\n\n"
    for char in lijn4:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()



#!--------------------------------------------------------------------------------------------------------------------------
#!--------------------------------------------------------------------------------------------------------------------------
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
    #Typing Effect
    for char in lijn1:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    #TypingEffect
    for char in lijn2:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


#het eerste stuk van het verhaal
def EersteKeuze():
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

#! Geluid bezig
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

#!--------------------------------------------------------------------------------------------------------------------------
#!--------------------------------------------------------------------------------------------------------------------------

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

#De Script voor 8 tot 12
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

#!--------------------------------------------------------------------------------------------------------------------------
#!--------------------------------------------------------------------------------------------------------------------------

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

#!--------------------------------------------------------------------------------------------------------------------------
#!--------------------------------------------------------------------------------------------------------------------------

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

#?--------------------------------------------------------------------------------------------------------------------------
#?--------------------------------------------------------------------------------------------------------------------------

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
            Credits()
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
    elif Keuze26 == "B" or Keuze26 == "b":
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