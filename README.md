# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [Code](#Code)
    * [Launchpad_1_Countdown](#Launchpad_1_Countdown)
    * [Launchpad_2_Lights](#Launchpad_2_Lights)
    * [Launchpad_3_Button](#Launchpad_3_Button)
    * [Launchpad_4_Servo](#Launchpad_4_Servo)
    * [Crash_Avoidance_Accelerometer](#Crash_Avoidance_Accelerometer)
    * [Crash_Avoidance_Light_and_Power](#Crash_Avoidance_Light_and_Power)
    * [Crash_Avoidance_OLED_Screen](#Crash_Avoidance_OLED_Screen)
* [Onshape](#Onshape)
   * [Beam_Design](#Beam_Design)

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!
![Picture Name Here](images/your-image-name.png)

### Test Link

[Hyperlink text](raspberry-pi/test.py)

### Test Image

![Picture Name Here](https://raw.githubusercontent.com/sechen12/Engineering_4_Notebook/main/images/Yoda_SWSB.webp)https://raw.githubusercontent.com/sechen12/Engineering_4_Notebook/main/images/Yoda_SWSB.webp

### Test GIF

![Picture Name Here](https://github.com/sechen12/Engineering_4_Notebook/blob/main/images/yoda_gif.gif?raw=true)https://github.com/sechen12/Engineering_4_Notebook/blob/main/images/yoda_gif.gif?raw=true


## Launchpad_1_Countdown

### Assignment Description

Using VS Code, make a program that counts down from 10, and when it reaches zero, to say "lift off".

### Evidence

[images_Countdown Evidence (1).webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/8326942f-afb0-4b5f-b39a-256e088f2aff)

### Code

```python
import time
import board
import digitalio

for x in range(10):
    print(10-x) #prints 10 --> 1 in descending order
    time.sleep(1) #delays the count by one second in between numbers
print("liftoff!") #print liftoff when the rest of the code is finished running
```
### Reflection

Using the loop made the coding much easier. I started the code using if-statements, but that caused my code to be overly long and complicated. To make the program countown from 10 to zero, you only need a total of 7 lines.


## Launchpad_2_Lights

### Assignment Description

To accompany the countdown, the assignment was to have 2 LEDs, one red, and one green. WHile the countown was running, the red LED would blink for every number written in the Serial Monitor. When the program was finished running, and the final message presented was "Lift Off!", the green light would turn on indefinitely.

### Evidence

[Untitled_ Sep 12, 2023 10_27 AM.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/f450a972-42ab-49f4-add4-b162aa5fe4ad)

### Wiring

![WIN_20230912_10_36_38_Pro](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/1e97cb75-a83b-4a67-94e7-da0a4bc6e3bf)

### Code

```python
#type: ignore
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
```

### Reflection

This assignment was relatively simple and logical. THe main problem I had was with the wiring. One of the LEDs was broken, but I didn't know that until I tried a few other LEDs. It's important to examine all possibilities as to why the program may not be running properly.


## Launchpad_3_Button

### Assignment Description

Continuing off of Launchpad 1 and 2, now we have added a button to determine when the the code for the lights and countdown are going to run.

### Evidence

[Launchpad 3.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/d34e8ce3-f540-47b6-96dc-4e0046250c24)

### Wiring

![IMG-2678](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/c6ad99c5-e26f-42e0-bb6e-18e7b30494e7)

### Code

```python
#type: ignore
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
```

### Reflection

This assignment was relatively staight foward. It was the fastest for me to complete because of the new knowledge I've collected about Circuit Python becuase of these "Launchpads". One thing I did have trouble on is figuring out the direction I wanted to pull the button. Unfortunately, I still don't understand how they work - I used trial and error to complete the code. Although the double/single equal sign difference is something that I should have been familiar with by now, I learned that the double equal sign (==) is used to check if what your statement is true:
```python
if button.value == True:
```
It was also recently clarified to me that the ```While True: ```statement is used to continuously run the code. This statement was important in the "Button" code becuase the program needed to constantly check if the button was true or false (off/on). I made the mistake of not using a "While True" statement in my intial code.

## Launchpad_4_Servo

### Assignment Description

When the code runs, when the button is pressed, the serial printer counts down from 10, presenting the according number every second. At the same time, a red LED blinks for every second, and a green LED turns on indefinitely, and a servo turns 180 degrees. We were building off the assignment above, but running a servo at the end of the code.

### Evidence

[Launchpad_4_Servo.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/c9ed09f7-a8c3-4a07-9740-14453d00eb11)

### Wiring

![Luanchpad_4_Servo_Capture](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/d004f71a-b694-4e0f-bc3c-6faea25e99a6)

### Code

```python
#type: ignore
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
```

### Reflection

This task was relatively simple - the most difficult part was the set up. In order to initialize the servo, you need to download a Circuit Python Library bundle, then move the Adafruit Servo folder into you lib folder on your board. Finally there are some lines of code you need to use to define the servo:
```python
pwm_servo = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0
```
Finally, you need to write the code for the servo, and by placing the line in the same loop as where you coded the green LED to turn on, the servo should turn your desired angle with the correct code:
```python
servo1.angle = 180
```
I also learned in terms of wiring, that the pin VBUS has 5V, and that's where the power of the servo pin should go.

## Crash_Avoidance_Accelerometer

### Assignment Description

We made a program that prints the MPU6050 acceleration data in the three axises: X, Y, and Z.

### Evidence

https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/e8f3c4e0-fcc9-4d31-8eea-d8e8141b4282

### Wiring

![Crash Avoidance Part 1 (Accelerometer)](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/eaa0a0c8-dd5c-4caf-a0c8-8d0d005a6e85)

### Code

```python
#type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio

sda_pin = board.GP14 # defining serial data pin
scl_pin = board.GP15 # defining serial clock pin
i2c = busio.I2C(scl_pin, sda_pin) # allowing the sda and scl pins to communicate using one channel
mpu = adafruit_mpu6050.MPU6050(i2c) # initializes the sensor


while True:
    print(f"x accelteration: {mpu.acceleration[0]}.") # this is an 'f-string'; it's a certain syntax that helps print the variables clearer
    print(f"y accelteration: {mpu.acceleration[1]}.")
    print(f"z accelteration: {mpu.acceleration[2]}.")
    print("")
    time.sleep(.5)
```

### Reflection

This assignment was relatively simple. It required the downloading of certain libraries, the defining of variables, and the use of an f-string. Through past assignments, I learned how to use test codes to help the overall program run.At first, I had trouble with configuring the f-string, but when I used a test variable, and a test f-string, I learned the synatx, and how to code the accelerometer's values. Here is the test code I ran to help myself understand the f-string.
```python
f = 0 # test variable

f("This is an f-string {f} and {f}.")
```

## Crash_Avoidance_Light_and_Power

### Assignment Description
Using the values that we programed beofre in the accelerometer assignment, incorporate an LED that lights up when the acceleromter is tilted 90 degrees. The next step was adding a battery and a switch so that the Pico didn't have to be connected to the computer.
### Evidence

https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/76175425-ae79-4eae-a74b-491b1ea28142

### Wiring

![Crash Avoidance Light and Battery](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/3f39542b-988c-4ce4-a7c5-6cc62a276c7e)

### Code

```python
#type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio

sda_pin = board.GP14 # defining serial data pin
scl_pin = board.GP15 # defining serial clock pin
i2c = busio.I2C(scl_pin, sda_pin) # allowing the sda and scl pins to communicate using one channel
mpu = adafruit_mpu6050.MPU6050(i2c) # initializes the sensor


while True:
    print(f"x accelteration: {mpu.acceleration[0]}.") # this is an 'f-string'; it's a certain syntax that helps print the variables clearer
    print(f"y accelteration: {mpu.acceleration[1]}.")
    print(f"z accelteration: {mpu.acceleration[2]}.")
    print("")
    time.sleep(.5)

    if mpu.acceleration[0] > 9 or mpu.acceleration[2] < 0: # if the x value is greater than 9, or the z value is less than 2, turn the LED on
        led.value = True
    else:
        led.value = False # if the statement isn't true, don't turn the LED on
```

### Reflection
I learned how to charge the battery; you have connect the battery to a 'battery charger', then connect it to a computer to let it charge for a few minutes before using it on the Pico. The coding portion of the assignment was the easiest concept to grasp. Becuase of mindless mistakes, the battery wouldn't connect to the Pico. For my next assignments, I can't forget that the breadboard rows run horizontally, and to connect wires together they need to be in the same row.

## Crash_Avoidance_OLED_Screen

### Assignment Description
Add an OLED screen to the previous task - display the acceleration values on an OLED screen. The LED must turn on if the accelerometer is tilted 90 degrees, and the we must use a battery and a switch to power the code uploaded to the Pico, so that the Pico is diconnected from the breadboard.
### Evidence

[Crash_Avoidance_OLED_Screen.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/7e3d2df3-e860-463c-9bb3-80cd80173135)

### Wiring

![IMG-6559](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/0dbc495a-85d5-4ee2-9cd8-65d363a81d0e)

### Code

```python
#type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
displayio.release_displays() #put this line just below your imports


sda_pin = board.GP14 # defining serial data pin
scl_pin = board.GP15 # defining serial clock pin
i2c = busio.I2C(scl_pin, sda_pin) # allowing the sda and scl pins to communicate using one channel
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # initializes the sensor
led = digitalio.DigitalInOut(board.GP18)
led.direction = digitalio.Direction.OUTPUT

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP11) # getting the computer to recognize the OLED
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # defining the OLED

while True:
    if mpu.acceleration[0] > 9 or mpu.acceleration[2] < 0: # if the x value is greater than 9, or the z value is less than 2, turn the LED on
        led.value = True
    else:
        led.value = False # if the statement isn't true, don't turn the LED on


    splash = displayio.Group()
    title = "ANGULAR VELOCITY" # gives a title to the OLED
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) # defines the perameters of the OLED
    splash.append(text_area)
    text_area.text = f"{title}\n x values:{round(mpu.gyro[0], 3)}\n y values:{round(mpu.gyro[1], 3)}\n z values:{round(mpu.gyro[2], 3)}" # f-string that prints the x, y, and z values on different lines on the OLED
    display.show(splash) # display what is shown above

## MPU adress = 0x68
## OLED adress = 0x3d
```

### Reflection

Out of all the tasks that were assigned, the final Crash Avoidence took me the longest. In order to connect the OLED screen to the Pico/computer, there were a series of steps that consisted of downlaoding mulitple libraries, and using test code to locate the address of the accelerometer, and the OLED. Here is the test code I ran:

```python
#type: ignore

import board
import time
import busio


sda_pin = board.GP14 # defining serial data pin
scl_pin = board.GP15 # defining serial clock pin
i2c = busio.I2C(scl_pin, sda_pin)

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()
```
If you run this code with the according pins, you can find the addresses in the Serial Monitor. To find the addresses of the OLED and the accelerometer specifically, you can unplug the power from one or the other and one address should cease from printing. The address that is still presented in the Serical Monitor, is the address of the OLED/accelerometer still getting power.

Also, didn't realize that in order for the OLED and the acceleromter to communicate, they need to share the SDA and SCL pins.

## Beam_Design

### Assignment Description
Create a beam within the [parameters](https://github.com/sechen12/Engineering_4_Notebook/files/12783413/Assignment.Requirements_.pdf) to hold the heaviest bucket.
### Part Link

[Onshape Document](https://cvilleschools.onshape.com/documents/5517eb4141dde3d11583bfcf/w/76219d7db810f33e12052ceb/e/62c262db223382f79a959590?renderMode=0&uiState=651ad1bd196827695acf9253)

### Part Image

### Reflection

