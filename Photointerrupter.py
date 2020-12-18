from digitalio import DigitalInOut, Direction, Pull
import time
import board

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27, import all libraries for lcd
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

interrupter = DigitalInOut(board.D3)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP#sets up the photointerrupter as an input

lcd.set_cursor_pos(0,0)
time.sleep(2)
counter = 0


max = 4#delay time
start = time.time()
while True:
    lcd.set_cursor_pos(0,0)
    if interrupter.value:#if something interrupts, the counter increases by one.
     counter += 1
     time.sleep(.20)#included to be able to count induvidual interruptions
    else:
        counter = counter

    remaining = max - time.time()
    if remaining <= 0:
        lcdmessage = "Interruptions: "#message at bottom row
        lcdmessage += str(counter)#have to use string to combine a variable and words
        lcd.print(lcdmessage)
        print(lcdmessage)#prints to lcd and serial monitor
        
        max = time.time() + 4
        counter = counter#sets the counter to itself, not 0