import time
import board
import pulseio
import servo
import digitalio
import touchio

touch_pad1 = board.A1
touch1 = touchio.TouchIn(touch_pad1)

touch_pad2 = board.A4
touch2 = touchio.TouchIn(touch_pad2)

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
                                         # Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
while True:
    if touch1.value:
     for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        
    elif touch2.value:
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        
            my_servo.angle = angle
        
    else:
        my_servo.angle = 0
