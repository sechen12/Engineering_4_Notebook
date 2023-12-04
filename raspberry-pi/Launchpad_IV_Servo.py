#type: ignore
#I used large portions of Elias Garcia's work in this assignment. https://github.com/egarcia28/Engineering_4_Notebook
import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

# defining LEDs/assigningvariables
GLed = digitalio.DigitalInOut(board.GP0)
GLed.direction = digitalio.Direction.OUTPUT
RLed = digitalio.DigitalInOut(board.GP1)
RLed.direction = digitalio.Direction.OUTPUT

# defining button/assigningvariables
button = digitalio.DigitalInOut(board.GP2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# defining servo/assigningvariables
pwm_servo = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0


while True:
    if button.value == True:
        
        for x in range(10):
            print(10-x) #prints 10 --> 1 in descending order
            RLed.value = True
            time.sleep(.5) #delays the count by one second in between numbers
            RLed.value = False
            time.sleep(.5)

        print("liftoff!") #print liftoff when the rest of the code is finished running
        while True:
            GLed.value = True
            servo1.angle = 180 # turns servo 180 degrees
            print(servo1.angle) # double checking if code above was running