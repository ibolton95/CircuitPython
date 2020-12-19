import digitalio
import time


class RGB:

    def __init__(self, red_pin, green_pin, blue_pin):


        self.r = digitalio.DigitalInOut(red_pin)
        self.r.direction = digitalio.Direction.OUTPUT

  

        self.g = digitalio.DigitalInOut(green_pin)
        self.g.direction = digitalio.Direction.OUTPUT

        self.b = digitalio.DigitalInOut(blue_pin)
        self.b.direction = digitalio.Direction.OUTPUT

    def red(self):
       
        self.r.value = False
        self.g.value = True
        self.b.value = True

    def magenta(self):
     
        self.r.value = False
        self.g.value = True
        self.b.value = False

    def blue(self):
 
        self.r.value = True
        self.g.value = True
        self.b.value = False

    def cyan(self):
 
        self.r.value = True
        self.g.value = False
        self.b.value = False

    def green(self):
  
        self.r.value = True
        self.g.value = False
        self.b.value = True

    def yellow(self):
 
        self.r.value = False
        self.g.value = False
        self.b.value = True

    def dark(self):

        self.r.value = True
        self.g.value = True
        self.b.value = True