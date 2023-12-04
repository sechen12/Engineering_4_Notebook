#type: ignore
# I used large portions of Elias Garcia's work in this assignment. https://github.com/egarcia28/Engineering_4_Notebook
import board
import time
import digitalio

GLed = digitalio.DigitalInOut(board.GP0)
GLed.direction = digitalio.Direction.OUTPUT
RLed = digitalio.DigitalInOut(board.GP1)
RLed.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while True: # contiuously runs this loop
    if button.value == True: # if the button is pressed, run this code
        
        for x in range(10):
            print(10-x) #prints 10 --> 1 in descending order
            RLed.value = True
            time.sleep(.5) #delays the count by one second in between numbers
            RLed.value = False
            time.sleep(.5)

        print("liftoff!") #print liftoff when the rest of the code is finished running
        while True:
            GLed.value = True