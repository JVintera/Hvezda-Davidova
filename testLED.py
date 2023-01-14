from neopixel import Neopixel
import utime
from random import randrange

numpix = 23
strip2 = Neopixel(numpix, 0, 14, "RGB")

#Barvy jsou nejspíš v pořadí GRB
yellow2 = (150, 255, 0)
blank = (0,0,0)
red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

strip2.brightness(10)

while True:
    #Rozsvítí a následně zhasne všechny LED
    for x in range(23):
        strip2.set_pixel(x, red)
        strip2.show()
    utime.sleep(1)
    for x in range(23):
        strip2.set_pixel(x, blank)
        strip2.show()
    utime.sleep(1)