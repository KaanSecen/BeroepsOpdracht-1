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
end1 = style.YELLOW + "Test1"

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

x = input()

print(style.YELLOW + 'Hallo, ' + x)

for char in tijdstip:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

print(style.CYAN)
print(tijd)

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
