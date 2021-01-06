import board
import adafruit_hcsr04


import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

Sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:

    distance = Sonar.distance

    try:
        print("Distance is " + str(round(distance)))

        step_size = 7.5

        red = 0
        green = 0
        blue = 0

        # Sets red, green, and blue to 0 so that the LED is dark

        if distance < 12.5:
            # Red to pink.

            red = 255
            green = 0
            blue = max(0,
                       int(((distance - 5) / step_size) * 255)
                       )

        if 12.5 < distance < 20:
            # Pink to blue.

            red = 255 - int(((distance - 12.5) / step_size) * 255)
            green = 0
            blue = 255

        if 20 < distance < 27.5:
            # Blue to cyan.

            red = 0
            green = int(((distance - 20) / step_size) * 255)
            blue = 255

        if distance > 27.5:
            # Cyan to green.

            red = 0
            green = 255
            blue = max(0,
                       255 - int(((distance - 27.5) / step_size) * 255)
                       )


        dot.fill((red, green, blue))


    except RuntimeError:
        print("Trying again")

    time.sleep(0.2)