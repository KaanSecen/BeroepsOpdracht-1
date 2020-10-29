# Add your Python code here. E.g.
from microbit import *
import music
import speech
import random
import math
import os

theeteller =0

menu = True
program = False
drinkmeter = False
theemax =10

beker = Image("00000:"
             "909000:"
             "90990:"
             "90909:"
             "99990")

beker1 = Image("00000:"
             "00000:"
             "99990:"
             "99909:"
             "99990")

beker2 = Image("00000:"
             "00000:"
             "99990:"
             "99909:"
             "99990")

beker3 = Image("00000:"
             "09990:"
             "09999:"
             "09999:"
             "09990")

# LOADING IMAGES
load26 = Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999")


while menu == True:
    sleep(1500)
    display.scroll("Start")
    if button_a.is_pressed():
        display.clear()
        sleep(500)
        display.show(Image("00000:"
             "00000:"
             "00900:"
             "00000:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "00000:"
             "09900:"
             "00000:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09000:"
             "09900:"
             "00000:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09900:"
             "09900:"
             "00000:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09990:"
             "09900:"
             "00000:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09990:"
             "09990:"
             "00000:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09990:"
             "09990:"
             "00090:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09990:"
             "09990:"
             "00990:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09990:"
             "09990:"
             "09990:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09990:"
             "09990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "09990:"
             "99990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("00000:"
             "99990:"
             "99990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("90000:"
             "99990:"
             "99990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("99000:"
             "99990:"
             "99990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("99900:"
             "99990:"
             "99990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("99990:"
             "99990:"
             "99990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("99999:"
             "99990:"
             "99990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99990:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99999:"
             "99990:"
             "00000"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "00000"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "00009"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "00099"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "00999"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "09999"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999"))
        sleep(500)
        display.show(Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "00000"))
        sleep(500)
        display.show(Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999"))
        sleep(500)
        menu = False
        program = True
        drinkmeter = True
        display.clear()

while  program == True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        theeteller += 1
        display.show(theeteller)
        sleep(2000)
        display.clear()
        drinkmeter = True
    if drinkmeter == True:
        sleep(500)
        display.show(beker3)
        drinkmeter = False
    if button_a.is_pressed():
        sleep(500)
        display.scroll("Je hebt")
        display.scroll(theeteller)
        display.scroll("keer thee gedronken!")
        sleep(500)
        display.scroll("Je moet nog")
        display.scroll(theemax - theeteller)
        display.scroll("keer thee drinken")
    if button_b.is_pressed():
        sleep(500)
        display.scroll("Kaan")
    if theeteller == 10:
        display.show(Image.HAPPY)