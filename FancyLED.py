import time
import random
from digitalio import DigitalInOut, Direction


class FancyLED:
    def __init__(self, pin1, pin2, pin3):

        led1 = DigitalInOut(pin1)
        led1.direction = Direction.OUTPUT

        led2 = DigitalInOut(pin2)
        led2.direction = Direction.OUTPUT

        led3 = DigitalInOut(pin3)
        led3.direction = Direction.OUTPUT

    
        self.led_list = [led1, led2, led3]

       
        self.all_off()
     
    def alternate(self, number_of_alternates=4):
      
        print("Alternating")

        self.led_list[1].value = True
        # Turns on middle LED when alternating.

        for alternate_number in range(0, number_of_alternates):

            lit = False

            if alternate_number % 2 == 0:
                lit = True

            # Using "%2" divides the blink_number by 2 and then looks at the remainder - helpgul for distinguishing between even and odd numbers.


            self.led_list[0].value = lit
            self.led_list[2].value = not lit
         
            time.sleep(1)
            print(
                "Alternate Counter: "
                + str(alternate_number)
                + " out of "
                + str(number_of_alternates)
            )

    def blink(self, number_of_blinks=6):
        # LEDs in object blink on and off.

        print("Blinking")

        for blink_number in range(0, number_of_blinks):
            lit = False

            if blink_number % 2 == 0:
                lit = True

            self.led_list[0].value = lit
            self.led_list[1].value = lit
            self.led_list[2].value = lit
            time.sleep(1)

            print(
                "Blink Counter: "
                + str(blink_number)
                + " out of "
                + str(number_of_blinks)
            )

    def chase(self, number_of_chases=4):
        # LEDs in object will turn on individually.

        print("Chasing")
        counter = 0
        for chase_number in range(0, number_of_chases):
            lit = False

            if counter == 0:
                self.led_list[0].value = not lit
                self.led_list[1].value = lit
                self.led_list[2].value = lit
                counter += 1
                time.sleep(1)

            if counter == 1:
                self.led_list[0].value = not lit
                self.led_list[1].value = not lit
                self.led_list[2].value = lit
                counter += 1
                time.sleep(1)

            if counter == 2:
                self.led_list[0].value = not lit
                self.led_list[1].value = not lit
                self.led_list[2].value = not lit
                counter = 0
                time.sleep(1)

    def sparkle(self, number_of_sparkles=50):
        # LEDs will randomly blink on and off.

        print("Sparkling")
        lit = True
        for sparkle_number in range(0, number_of_sparkles):
            self.led_list[0].value = not lit
            self.led_list[1].value = not lit
            self.led_list[2].value = not lit

            self.led_list[random.randrange(0, 3, 1)].value = lit



            time.sleep(0.1)
 

    def all_off(self):

        for led in self.led_list:
            led.value = False
        time.sleep(1)
