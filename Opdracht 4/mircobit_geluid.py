# Imports for project
from microbit import *
import speech
import random

LengteWoordArray = 3

onderwerp = ["He", "She", "Arnold"]
werkwoord = ["Walks", "flies", "runs"]
rest = ["to school", "to home", "to the playground"]

pitchsnel = 100

def SayTheWords1(word):
    print(word)
    speech.say(word, speed=120, pitch=pitchsnel, throat=100, mouth=200)
    sleep(500)
    
def SayTheWords2(word1):
    willekeurigGetal = random.randint(0, LengteWoordArray - 1)
    display.show(willekeurigGetal)
    SayTheWords1(onderwerp[willekeurigGetal])
    willekeurigGetal = random.randint(0, LengteWoordArray - 1)
    display.show(willekeurigGetal)
    SayTheWords1(werkwoord[willekeurigGetal])
    willekeurigGetal = random.randint(0, LengteWoordArray - 1)
    display.show(willekeurigGetal)
    SayTheWords1(rest[willekeurigGetal])
    
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        sleep(2500)
        pitchsnel += 10
        display.scroll(pitchsnel)
    elif button_b.is_pressed():
        display.show(Image.SAD)
        sleep(2500)
        pitchsnel -= 10
        display.scroll(pitchsnel)
    elif display.read_light_level() < 40:
        SayTheWords2("")
    else:
        display.show(Image.SQUARE)
        