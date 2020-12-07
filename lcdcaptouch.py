import board
import busio
import touchio
import digitalio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27, import all libraries for lcd
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
touchstate = True
touch_pad1 = board.A1 #cap touch wires
touch1 = touchio.TouchIn(touch_pad1)
touch_pad2 = board.A5
touch2 = touchio.TouchIn(touch_pad2)
lcd.set_cursor_pos(0,0)
lcd.print("Hello CircuitPython!")
time.sleep(2)
pushcount = 0


while True:
    
    if touch1.value:
        lcdmessage = "Direction: UP   "
        touchstate = False#counting goes up when one wire is touched
        
    else:
        lcdmessage = "Direction: DOWN "
        touchstate = True#otherwise, the counting goes down
    
    lcd.set_cursor_pos(0,0)
    lcd.print(lcdmessage)#prints if it's moving up or down
    if touchstate == False:
        touchdirection = 1
    else:
        touchdirection = -1#makes it possible to move up or down with variables
    
    if touch2.value:
        pushcount = pushcount + touchdirection#number of pushes goes down or up
        lcd.set_cursor_pos(1,0)
        lcdmessage = "Presses: "#message of presses on bottom row
        lcdmessage += str(pushcount)#have to write str because it's a variable and not just words
        print(pushcount)
        lcd.print(lcdmessage)
    else:
        pushcount = pushcount#otherwise, pushcount is the same
        