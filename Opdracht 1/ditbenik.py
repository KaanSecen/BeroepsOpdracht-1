import os
import sys
import datetime
from time import sleep


os.system("")


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


print(style.MAGENTA)
tijd = datetime.datetime.now()

line1 = style.GREEN + "Hello You!, Ik ben Kaan Secen.\n"
line2 = style.CYAN + "Wie ben jij?\n"
line3 = style.RED + "Type je naam:\n"
tijdstip = style.MAGENTA + "De Datum en tijd is:"
restart1 = style.GREEN + "Wil jij dit programma opnieuw doen?\n"
restart2 = style.GREEN + "Type Y/N:\n"
vraag1 = style.MAGENTA + "\n3 vragen over mij.\n\nVraag 1: Waar woon ik?\nKies 1 2 of 3.\n\n1. Amsterdam Noord\n2. Amsterdam West\n3. Amsterdam Zuid\n\n"
vraag2 = style.MAGENTA + "Vraag 2: Hoe oud ben ik?\nKies 1 2 of 3.\n\n1. 3 Jaar\n2. 17 Jaar\n3. 99 Jaar\n\n"
vraag3 = style.MAGENTA + "Vraag 3: Welke van deze hobby's doe ik?\nKies 1 2 of 3.\n\n1. Zwemmen\n2. Schaatsen\n3. Boksen\n\n"
end1 = style.YELLOW + "Test1"

#Introduction Kaan Secen
for char in line1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in line2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in line3:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

naam = input()

print(style.YELLOW + 'Hallo, ' + naam)

for char in tijdstip:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

print(style.CYAN)
print(tijd)

#Vragen stukje

# naam geel maker

naamgeel = style.YELLOW + naam

for char in vraag1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

vraag=input("Type een Cijfer >")
if vraag=='1':
     print(style.GREEN + "\nGoedzo",naamgeel)
     print(style.GREEN + "ik woon op dit moment in Amsterdam Noord.\n")
if vraag=='2':
     print(style.RED + "\nDat is fout",naamgeel)
     print(style.RED + "ik woon nu in Amsterdam Noord.\n")
if vraag=='3':
     print(style.RED + "\nDat is fout",naamgeel)
     print(style.RED + "ik woon nu in Amsterdam Noord.\n")

for char in vraag2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

vraag=input("Type een Cijfer >")
if vraag=='1':
     print(style.RED + "\nDat is fout",naamgeel)
     print(style.RED + "Ik ben echt niet 3 jaar oud.\n")
if vraag=='2':
     print(style.GREEN + "\nGoedzo",naamgeel)
     print(style.GREEN + "Ik ben nu 17 jaar oud.\n")
if vraag=='3':
     print(style.RED + "\nDat is fout",naamgeel)
     print(style.RED + "Zie ik er uit als een opa ofzo?\n")

for char in vraag3:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

# Vraag 3 met extra
vraag=input("Type een Cijfer >")
if vraag=='1':
     print(style.GREEN + "\nGoedzo",naamgeel)
     print(style.GREEN + "Klopt Zwemmen is mijn hobby.\n")
     if vraag == '1':
               sleep(0.1)  
               sys.stdout.write(style.YELLOW + "Nu een extra vraag:\n\n")
               sys.stdout.flush()
               sleep(0.1)  
               sys.stdout.write(style.MAGENTA + "Welke zwemdiploma's heb ik allemaal?\nKies 1 2 of 3.\n\n1. Zwemdiploma A\n2. Zwemdiploma A en B\n3. Alle Zwemdiploma's\n\n")
               sys.stdout.flush()
               vraagzwem=input("Type een Cijfer >")
               if vraagzwem == '1':
                    print(style.RED + "\nDat is fout",naamgeel)
                    print(style.RED + "Inmiddels heb ik al mijn A en B\n")
               if vraagzwem == '2':
                    print(style.GREEN + "\nGoedzo",naamgeel)
                    print(style.GREEN + "Ik heb op dit moment mijn A en B ik ga nu voor mijn C.\n")
               if vraagzwem == '3':
                    print(style.RED + "\nDat is fout",naamgeel)
                    print(style.RED + "Ik heb op dit moment A en B maar ik wil heel graag ook mijn C halen.\n")
if vraag=='2':
     print(style.RED + "\nDat is fout",naamgeel)
     print(style.RED + "Ik kan echt niet schaatsen\n")
if vraag=='3':
     print(style.RED + "\nDat is fout",naamgeel)
     print(style.RED + "Boksen nee man ik ben niet zo sterk.\n")
if vraag=='2' or '3':
     sleep(0.1)  
     sys.stdout.write(style.YELLOW + "Nu een extra vraag:\n\n")
     sys.stdout.flush()
     sleep(0.1)  
     sys.stdout.write(style.MAGENTA + "Waarom denk je dat ik niet gekozen heb voor Boksen of Schaatsen?\nKies 1 2 of 3.\n\n1. Ik vond het te saai.\n2. Ik wist meteen dat ik wou zwemmen\n3. het was te lastig met mijn linker been\n\n")
     sys.stdout.flush()
     vraaghobby=input("Type een Cijfer >")
     if vraaghobby == '1':
          print(style.RED + "\nDat is fout",naamgeel)
          print(style.RED + "Ik vond het best moeilijk maar het was een beetje lastig met mijn linker been.\n")
     if vraaghobby == '3':
          print(style.GREEN + "\nGoedzo",naamgeel)
          print(style.GREEN + "Klopt ik vond het best lastig met mijn linker been om te gaan schaatsen/boksen\n")
     if vraaghobby == '2':
          print(style.RED + "\nDat is fout",naamgeel)
          print(style.RED + "Ik vond zwemmen ook eerst moeilijk maar ik heb mezelf later aangepast om het wel te doen.\n")
# Restart stukje

for char in restart1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in restart2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

result=input()
if result=='y':
     os.system('python "Hello You.py"')
else:
     sleep(1)
     print(style.RESET + "\nGemaakt Door Kaan Secen.")