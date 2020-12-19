# CircuitPython

## Connecting to Github LED Blink
I am figuring out coding for the metroexpress, but making an LED Blink was relatively simple. The bigger challenge is just remembering the process of commiting and pushing the code into git, as I accidently made a duplicate CircuitPython clone in the process. The code for this assignment (and all future assignments) is not in the README, it's a file in the repository.

<img src="./images2/led_blink_green.jpg" width="200"> 

## CircuitPython Servo
In this assignment, I wired up a servo using capacitive touch, which involved a touchio function. While I was researching to create my "while True" loop, I learned about the statement "elif", which is similar to else in that it allows for multiple possible conditions whithin the "while True" section. This allowed me to write "if one thing" and then "elif another thing". I also had some issues with committing my code to GitHub because when I pulled my changes locally, they split. With help, I learned that I had to commit to merge the changes and then push them both to GitHub.


<img src="./images2/ServoCapTouch.jpg" width="400"> 

## CircuitPython LCD
In this assignment, I wired an LCD using capacitive touch: when one wire was touched, the counting direction was set to positive or negative, and when the other wire was touched, the count was increased or decreased (accroding to wire 1) by a magnitude of 1. While writing the code, I had a lot of trouble with the i2c file, as it did not process correctly within my code. I eventually wiped my Metro Express and started over, which helped, and then I had to remember to change the i2cInterface() to contain 0x3f rather than 0x27. I also had instances of my computer not registering my Metro Express when I plugged it in, which made it hard to restart, but switching the port that I plug it into has helped so far, so hopefully I don't run into this problem much more, as it is very hard to solve any other way. When I finally had my code working and my LCD running the code, I had trouble pushing my code to my GitHub repository, as I received the message that the remote contains work that I do not have locally. To fix this issue, I had to pull my changes from my git repository, commit changes, and the push all of my committed changes up to my git repository (along with the code).


<img src="./images2/LcdCapTouch.jpg" width="400"> 

## CircuitPython Photointerrupter
In this assignment, I wired a photointerrupter and had it keep track of the number of times I interrupted it. My LCD screen displayed the number of interrupts along with my serial monitor, which outputted the number of interrupts every 4 seconds. There was a delay on the counter so that it could register individual interrupts. I learned more about the str(counter) function, which is a string required for displaying a variable along with words. My only struggles were running into the "remote contains work that I do not have locally" issue again (which I solved in the last assignment) and a deprecation notice when I typed in my GitHub info into Termux. I received a notice from GitHub that "basic authentication using a password to Git is deprecated and will soon no longer work." However, it worked after I had to pull my changes locally to solve the previous issue, so maybe it was just an error related to that issue. Either way, I'm interested to see what will come out of this issue, as I am always required to sign into my GitHub account when I push changes to GitHub from Termux.


<img src="./images2/Photointerrupter.jpg" width="400"> 

## Classes, Objects, and Modules
In this assignment, I learned how to create classes with objects, modules, and specific properties. I had to make a class of RGB LEDs that supported a code that caused the LEDs to cycle through different colors, which required the self argument, which refers an object to itself when writing specific methods/modules. I had to learn to write self.r, self.g, and self.b and that the led pins are going to ground- so False is on and True is off. The wiring was a little chaotic so I am including a picture of the wiring instead of a written diagram.
