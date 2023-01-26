from library.neopixel import Neopixel
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

delay = 0.004
utime.sleep(delay)  

strip2.brightness(20)

while True:
    #Pseudonáhodné blikání 4 LED
    k = randrange(23)
    l = randrange(23)
    m = randrange(23)
    n = randrange(23)
    strip2.set_pixel(n, blank)
    strip2.show()
    strip2.set_pixel(k, yellow2)
    strip2.show()
    strip2.set_pixel(l, yellow2)
    strip2.show()
    utime.sleep(0.05)
    strip2.set_pixel(k, blank)
    strip2.show()
    strip2.set_pixel(m, yellow2)
    strip2.show()
    utime.sleep(0.05)
    strip2.set_pixel(l, blank)
    strip2.show()
    strip2.set_pixel(m, blank)
    strip2.show()
    strip2.set_pixel(n, yellow2)
    strip2.show()
    utime.sleep(0.05)