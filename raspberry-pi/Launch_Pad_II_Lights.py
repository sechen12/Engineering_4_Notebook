#type: ignore
# I copied my entire coding assignment from ELias Garcia. https://github.com/egarcia28/Engineering_4_Notebook/tree/main/raspberry-pi
import board
import time
import digitalio

GLed = digitalio.DigitalInOut(board.GP0)
GLed.direction = digitalio.Direction.OUTPUT
RLed = digitalio.DigitalInOut(board.GP1)
RLed.direction = digitalio.Direction.OUTPUT

for x in range(10):
    print(10-x) #prints 10 --> 1 in descending order
    RLed.value = True
    time.sleep(.5) #delays the count by one second in between numbers
    RLed.value = False
    time.sleep(.5)

print("liftoff!") #print liftoff when the rest of the code is finished running
while True:
    GLed.value = True