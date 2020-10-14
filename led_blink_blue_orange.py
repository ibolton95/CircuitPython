# Metro IO demo
# Welcome to CircuitPython 2.2.0 :)

import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)



while True:
    print("Make it dark blue!")
    dot.fill((34,11,214))
    time.sleep(.5)
    print("Make it orange!")
    dot.fill((214,89,11))
    time.sleep(.5)