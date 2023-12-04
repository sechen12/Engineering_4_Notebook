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
    * [Landing_Area_Functions](#Landing_Area_Functions)
    * [Landing_Area_Plotting](#Landing_Area_Plotting)
    * [Morse_Code_Translation](#Morse_Code_Translation)
    * [Morse_Code_Transmission](#Morse_Code_Transmission)
    * [Data_Storage](#Data_Storage)
* [Onshape](#Onshape)
   * [Beam_Design](#Beam_Design)
        * [FEA_Part_1](#FEA_Part_1)
        * [FEA_Part_3](#FEA_Part_3)
        * [FEA_Part_4](#FEA_Part_4)

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


## **Launchpad_1_Countdown**

### Assignment Description

Using VS Code, make a program that counts down from 10, and when it reaches zero, to say "lift off".

### Evidence

[images_Countdown Evidence (1).webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/8326942f-afb0-4b5f-b39a-256e088f2aff)

### Code

[Code](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad_I_countdown.py)

### Reflection

Using the loop made the coding much easier. I started the code using if-statements, but that caused my code to be overly long and complicated. To make the program countown from 10 to zero, you only need a total of 7 lines. I worked with the person next to me, [Elias Garcia](https://github.com/egarcia28/Engineering_4_Notebook/tree/main/raspberry-pi). I copied my entire coding assignment from Elias Garcia. Here is a link to their notebook.

## **Launchpad_2_Lights**

### Assignment Description

To accompany the countdown, the assignment was to have 2 LEDs, one red, and one green. WHile the countown was running, the red LED would blink for every number written in the Serial Monitor. When the program was finished running, and the final message presented was "Lift Off!", the green light would turn on indefinitely.

### Evidence

[Untitled_ Sep 12, 2023 10_27 AM.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/f450a972-42ab-49f4-add4-b162aa5fe4ad)

### Wiring

![WIN_20230912_10_36_38_Pro](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/1e97cb75-a83b-4a67-94e7-da0a4bc6e3bf)

### Code

[code](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Launch_Pad_II_Lights.py)

### Reflection

This assignment was relatively simple and logical. THe main problem I had was with the wiring. One of the LEDs was broken, but I didn't know that until I tried a few other LEDs. It's important to examine all possibilities as to why the program may not be running properly. # I copied my entire coding assignment from ELias Garcia. https://github.com/egarcia28/Engineering_4_Notebook/tree/main/raspberry-pi


## **Launchpad_3_Button**

### Assignment Description

Continuing off of Launchpad 1 and 2, now we have added a button to determine when the the code for the lights and countdown are going to run.

### Evidence

[Launchpad 3.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/d34e8ce3-f540-47b6-96dc-4e0046250c24)

### Wiring

![IMG-2678](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/c6ad99c5-e26f-42e0-bb6e-18e7b30494e7)

### Code

[code](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Lauchpad_III_Button.py)

### Reflection

This assignment was relatively staight foward. It was the fastest for me to complete because of the new knowledge I've collected about Circuit Python becuase of these "Launchpads". One thing I did have trouble on is figuring out the direction I wanted to pull the button. Unfortunately, I still don't understand how they work - I used trial and error to complete the code. Although the double/single equal sign difference is something that I should have been familiar with by now, I learned that the double equal sign (==) is used to check if what your statement is true:
```python
if button.value == True:
```
It was also recently clarified to me that the ```While True: ```statement is used to continuously run the code. This statement was important in the "Button" code becuase the program needed to constantly check if the button was true or false (off/on). I made the mistake of not using a "While True" statement in my intial code. I used large portions of Elias Garcia's work in this assignment. https://github.com/egarcia28/Engineering_4_Notebook

## **Launchpad_4_Servo**

### Assignment Description

When the code runs, when the button is pressed, the serial printer counts down from 10, presenting the according number every second. At the same time, a red LED blinks for every second, and a green LED turns on indefinitely, and a servo turns 180 degrees. We were building off the assignment above, but running a servo at the end of the code.

### Evidence

[Launchpad_4_Servo.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/c9ed09f7-a8c3-4a07-9740-14453d00eb11)

### Wiring

![Luanchpad_4_Servo_Capture](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/d004f71a-b694-4e0f-bc3c-6faea25e99a6)

### Code

[code](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad_IV_Servo.py)

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
I also learned in terms of wiring, that the pin VBUS has 5V, and that's where the power of the servo pin should go. I used large portions of Elias Garcia's work in this assignment. https://github.com/egarcia28/Engineering_4_Notebook.


## **Crash_Avoidance_Accelerometer**

### Assignment Description

We made a program that prints the MPU6050 acceleration data in the three axises: X, Y, and Z.

### Evidence

https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/e8f3c4e0-fcc9-4d31-8eea-d8e8141b4282

### Wiring

![Crash Avoidance Part 1 (Accelerometer)](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/eaa0a0c8-dd5c-4caf-a0c8-8d0d005a6e85)

### Code

[code](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Accelerometer.py)

### Reflection

This assignment was relatively simple. It required the downloading of certain libraries, the defining of variables, and the use of an f-string. Through past assignments, I learned how to use test codes to help the overall program run.At first, I had trouble with configuring the f-string, but when I used a test variable, and a test f-string, I learned the synatx, and how to code the accelerometer's values. Here is the test code I ran to help myself understand the f-string.
```python
f = 0 # test variable

f("This is an f-string {f} and {f}.")
```
I copied my entire coding assignment from Elias Garcia. Here is a link to their notebook. https://github.com/egarcia28/Engineering_4_Notebook/blob/main/raspberry-pi/crash_avoidance_1.py

## **Crash_Avoidance_Light_and_Power**

### Assignment Description
Using the values that we programed beofre in the accelerometer assignment, incorporate an LED that lights up when the acceleromter is tilted 90 degrees. The next step was adding a battery and a switch so that the Pico didn't have to be connected to the computer.

### Evidence

https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/76175425-ae79-4eae-a74b-491b1ea28142

### Wiring

![Crash Avoidance Light and Battery](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/3f39542b-988c-4ce4-a7c5-6cc62a276c7e)

### Code

[code](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Light%20%2B%20Power.py)

### Reflection
I learned how to charge the battery; you have connect the battery to a 'battery charger', then connect it to a computer to let it charge for a few minutes before using it on the Pico. The coding portion of the assignment was the easiest concept to grasp. Becuase of mindless mistakes, the battery wouldn't connect to the Pico. For my next assignments, I can't forget that the breadboard rows run horizontally, and to connect wires together they need to be in the same row. # I used large portions of Elias Garcia's work in this assignment. https://github.com/egarcia28/Engineering_4_Notebook

## **Crash_Avoidance_OLED_Screen**

### Assignment Description
Add an OLED screen to the previous task - display the acceleration values on an OLED screen. The LED must turn on if the accelerometer is tilted 90 degrees, and the we must use a battery and a switch to power the code uploaded to the Pico, so that the Pico is diconnected from the breadboard.
### Evidence

[Crash_Avoidance_OLED_Screen.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/7e3d2df3-e860-463c-9bb3-80cd80173135)

### Wiring

![IMG-6559](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/0dbc495a-85d5-4ee2-9cd8-65d363a81d0e)

### Code

[code](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_OLED_Screen.py)

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

Also, didn't realize that in order for the OLED and the acceleromter to communicate, they need to share the SDA and SCL pins. I used large portions of Elias Garcia's work in this assignment. https://github.com/egarcia28/Engineering_4_Notebook

## Landing_Area_Functions

### Assignment Description

We created a program that took values from somebody typing into the Serial Monitor in an (x,y) syntax. You do this 3 times (3 points of a triangle). The program then takes those values and either gives you an "error" message, or calculates the area of the triangle.

### Evidence

[Landing Area Functions.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/bf5fb5be-b978-4893-8e7c-174ea19c89d7)

### Code

```python
#type: ignore

import board

def TriArea(x1,y1,x2,y2,x3,y3): # Creates a function to find the area
    try: # Find the area if coordinates are valid
        area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) # Triangle area formula
        return area
    except: # If coordinates are invalid, run this code:
        print("Invalid Coordinates")
        area = 0
        return area

while True:
    print("Point 1 Coordinates (x,y):") # Print so the person running code knows which point they're entering the corridnates for
    p1 = input() # Point 1 is where somebody can put their deesired numbers
    x1, y1 = p1.split(",") # Turn p1 into two variables separated by a comma
    print(f"Point 1: ({p1})") # Confirm the coordinates (also puts parenthesis around the cooridnates if not already done so)

    print("Point 2 Coordinates (x,y):") # Repeat for coordinate 2
    p2 = input()
    x2, y2 = p2.split(",")
    print(f"Point 2: ({p2})")

    print("Point 3 Coordinates (x,y):") # Repeat for coordinate 3
    p3 = input()
    x3, y3 = p3.split(",")
    print(f"Point 3: ({p3})")

    x1 = float(x1) # taking the cooridnates and turning them from strings to floats - making the number recognizable to the comupter
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    
    area = TriArea(x1,y1,x2,y2,x3,y3) # Plug in floats to find area
    print(" ") # space
    print(f"AREA IS: {area}")
    print(" ") # space
```
### Reflection

I had a lot of trouble grasping the idea of a ```float```. I learned that floats were important for making a string into a value that the computer recognizes as a number, not just a digit.

I also tried to employ what I had learned from my previous assignments to this one. We learned how to break the code down into its small parts, and solve one problem at a time. The makes the task less daunting, and the code more comprehensible. For example, knowing that the end goal of the code was to calculate the area of the triangle, you can work on the section of the code that finds the area.

Grant's code was really helpful in making the code. I didn't understand the use for a float and how to code for what is supposed to be presented in the Serial Monitor.

## Landing_Area_Plotting

### Assignment Description

Building off of what we did last time, we had to graph/plot the traingle values we had put into the Serial monitor, onto an OLED screen. The OLED screen should also print the area.

### Evidence

[Landing Area Part 2.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/c6a6b117-8b35-430c-affb-03dedab7e524)

### Wiring

PicoW was wired to OLED Screen using the following
* 3V3 (OUT) from the Pico  to Vin on the screen
* SDA (Data) to GP14
* SCL (Clk) to GP15
* Ground to GND.

### Code

```python
#type: ignore
import board
import displayio
import time
import busio
import adafruit_displayio_ssd1306
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

displayio.release_displays()

sda_pin = board.GP14 # defining serial data pin
scl_pin = board.GP15 # defining serial clock pin
i2c = busio.I2C(scl_pin, sda_pin) # allowing the sda and scl pins to communicate using one channel

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP11) # getting the computer to recognize the OLED
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # defining the OLED
splash = displayio.Group() # Creating a display group


def TriArea(x1,y1,x2,y2,x3,y3): # Creates a function to find the area
    try: # Find the area if coordinates are valid
        area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) # Triangle area formula
        return area
    except: # If coordinates are invalid, run this code:
        print("Invalid Coordinates")
        area = 0
        return area

while True:
    print("Point 1 Coordinates (x,y):") # Print so the person running code knows which point they're entering the corridnates for
    p1 = input() # Point 1 is where somebody can put their deesired numbers
    x1, y1 = p1.split(",") # Turn p1 into two variables separated by a comma
    print(f"Point 1: ({p1})") # Confirm the coordinates (also puts parenthesis around the cooridnates if not already done so)

    print("Point 2 Coordinates (x,y):") # Repeat for coordinate 2
    p2 = input()
    x2, y2 = p2.split(",")
    print(f"Point 2: ({p2})")

    print("Point 3 Coordinates (x,y):") # Repeat for coordinate 3
    p3 = input()
    x3, y3 = p3.split(",")
    print(f"Point 3: ({p3})")

    x1 = float(x1) # taking the cooridnates and turning them from strings to floats
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    
    area = TriArea(x1,y1,x2,y2,x3,y3) # Plug in floats to find area
    print(" ") # space
    print(f"AREA IS: {area}")
    print(" ") # space

    text_area = label.Label(terminalio.FONT, text= f"Area = {area}", color=0xFFFF00, x=5, y=5)
    splash.append(text_area)

    hline = Line(0,32,128,32, color=0xFFFF00)
    splash.append(hline)
    vline = Line(64,0,64,64, color=0xFFFF00)
    splash.append(vline)

    circle = Circle(64, 32, 2, outline=0xFFFF00)
    splash.append(circle)

    X1 = int(x1 + 64)
    X2 = int(x2 + 64)
    X3 = int(x3 + 64)
    Y1 = int(-y1 + 32)
    Y2 = int(-y2 + 32)
    Y3 = int(-y3 + 32)

    triangle = Triangle(X1, Y1, X2, Y2, X3, Y3, outline=0xFFFF00)
    splash.append(triangle)
    display.show(splash)

```
### Reflection
The most difficult part of the code was becoming familiar to the OLED dimensions. In order to plot the 3 points of the triangle, the program had to translate the values that the computer could calculate, into values the OLED screen could understand, and plot. Also, it is important to set the OLED up appropriately; there are many libraries to import in order to connect the OLED to the Pico:
```python
import displayio
import time
import busio
import adafruit_displayio_ssd1306
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

displayio.release_displays()

sda_pin = board.GP14 # defining serial data pin
scl_pin = board.GP15 # defining serial clock pin
i2c = busio.I2C(scl_pin, sda_pin) # allowing the sda and scl pins to communicate using one channel

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP11) # getting the computer to recognize the OLED
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # defining the OLED
splash = displayio.Group() # Creating a display group
```

## Morse_Code_Translation

### Assignment Description
The assignment was to create a program that translated the alphabet into morse code. We were given the code for the translated morse code letters.
### Evidence 
https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/47506d09-9df5-4d51-8aa2-a1ddf6d83a4e
### Code

```python
#type: ignore

import board

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

while True:
    print("Enter morse code message or -q to quit:")
    text = input()
    if text == "q":
        print("quit")
        break
    else:
        upper_text = text.upper()
        for letter in upper_text:
            print(MORSE_CODE[f"{letter}"], end=" ") #Print each letter in morse
        print(" ")
```
### Reflection

The morse code assignment was relatively simple. The only are where I struggled was understandig why it was important to use the ```upper.method()```. The ```upper.method()``` is used to help the computer understand the values the someone might be putting into the computer. If you look at the chunk of code where the morse code is translated, you will see that all of the leters translated are uppercase. When you use the ```upper.method()```, the computer will take the letters input by the user, and automatically make them uppercase so that the program can read the words.

## Morse_Code_Transmission

### Assignment Description
Use the code that we wrote for the morse code translation to translate the morse code into a series of blinks and pauses according to the translation.
### Evidence 

![transmission](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/544929ed-43de-4c44-aaa9-120041994f54)

### Wiring

![WIN_20230912_10_36_38_Pro](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/1e97cb75-a83b-4a67-94e7-da0a4bc6e3bf)

### Code

```python
#type: ignore

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
save = " " # saves the input in the serial monitor so that the code can run all of its components

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

while True:
    print("Enter morse code message or -q to quit:") # print this message whenever the code is run
    text = input() # making a variable to put the input
    if text == "q": # run this if-statement if somebody types "q", then stop the code
        print("quit")
        break
    else: # if "q" isn't written, run this code
        upper_text = text.upper() # making variable to help translate english into something the computer can read
        for letter in upper_text:
            save = save + MORSE_CODE[letter] + " " # save equals what it saved previously and the new input
        print(f"translation"+ save)
        for character in save: #loop thru morse message
            if character == ".":
                led.value = True
                time.sleep(dot_time) # if character is a dot, do a short blink
            elif character == "-":
                led.value = True
                time.sleep(dash_time) # if character is a dash, do a long blink
            elif character == " ":
                led.value = False
                time.sleep(between_letters) # if character is between letters, do a “between letters” pause
            elif character == "/":
                led.value = False
                time.sleep(between_words) # if it's between words, do a “between words” pause
            led.value = False
            time.sleep(between_taps)
```

### Reflection
The python coding is getting easier, but I have a habit of forgetting to add small thins to the code to make it work. For example, I forgot to put colons after the "if-statement" for a few of them, so the computer couldn't read what I was trying to say. I also forgo to add the ".value" after "led" when I wanted to control when the led was on or off.

## Data_Storage

### Assignment Description
Write a program that can switch between data mode and code mode. While the Pico is switched into code mode, the code that you have written should save to the board, like normal. To actually run the code you have written, you have to switch into data mode. Through a series of steps, the data mode should store the data taken from the MPU sensor, into a CSV file. While the data is saving to the board, the LED should turn on whenever the MPU is tilted.
### Evidence

### Wiring
[Crash_Avoidance_OLED_Screen.webm](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/7e3d2df3-e860-463c-9bb3-80cd80173135)
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

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
tilt = 0
with open("/data.csv", "a") as datalog:
    while True:
        XAcceleration = mpu.acceleration[0] ## States which value of the Tuple corresponds to which accelerometer value 
        YAcceleration = mpu.acceleration[1] ## For Y
        ZAcceleration = mpu.acceleration[2] ## For Z
        
        time.sleep(.1) ## Adds a slight pause after each cycle 

        if ZAcceleration < 3:
            led.value = True ## Turns on the Red LED
            tilt = True
        else:
            led.value = True # LED cycle
            time.sleep(.5)
            led.value = False       
            tilt = False    
    
        datalog.write(f"{time.monotonic()},{XAcceleration},{YAcceleration},{ZAcceleration},{tilt}\n") #Put the data into a chart

        datalog.flush() # Save the data
        time.sleep(.1)
```

### Reflection
The code was taken almost directectly from the [Crash_Avoidance_Light_and_Power](#Crash_Avoidance_Light_and_Power). The only changes that were made were adding a line connecting the data file to the data stored on the Pico, and the writting that would be presented in the data file. My biggest problem was forgetting to add a variable that stored the condition of the MPU. Without this, the data couldn't be stored into the chart, because there wasn't any data.

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

## **Beam_Design**

## FEA_Part_1

### Assignment Description
Create a beam within the [parameters](https://github.com/sechen12/Engineering_4_Notebook/files/12783413/Assignment.Requirements_.pdf) to hold the heaviest bucket.

### Evidence 
<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/Beam%20Starter%20+%20Holder.png?raw=true" width="400">

### Part Link

[Onshape Document](https://cvilleschools.onshape.com/documents/5517eb4141dde3d11583bfcf/w/76219d7db810f33e12052ceb/e/62c262db223382f79a959590?renderMode=0&uiState=651ad1bd196827695acf9253)



<!-- ![Beam Starter + Holder](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/673c98ca-6363-4e1f-b6bc-40ca76358214)
![Assembly 1 (1)](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/270a59ce-fcc0-43af-bf25-90dcb28b34d0)
![Assembly v 1](https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/c7cba57b-1d80-4629-b370-820978ddee8c) -->


### Reflection
My partner and I went through multiple rendors of the beam. While we were researching, we found that beams that are taller vertically, and have horizontal support along the tops and bottoms of the beam are strong. We also found that structures that have a ramp will diffuse the tension that is placed on the point where the beam and the cast is connected.

Initially, our beam was wide and flat. We learned by researching strong beam structures, that the most structurally sound beams are taller vertically than horizontally wide. We then concentrated our beam's weight to being taller rather than wider. We played with the idea that if the beam is shaped like a ramp, thicker at the point where the beam meets the frame, and thinner at the end, the beam will be more likely to stay attached.

## FEA_Part_3

### Part Image

|Image of Model |Stress |Displacement |
|-|-|-|
|<img src="https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/673c98ca-6363-4e1f-b6bc-40ca76358214" width="400"> |<img src="https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/270a59ce-fcc0-43af-bf25-90dcb28b34d0" width="400"> |<img src="https://github.com/sechen12/Engineering_4_Notebook/assets/112981481/c7cba57b-1d80-4629-b370-820978ddee8c" width="400"> |

### Reflection

Looking at the first image, our beam went from being able to hold 6.774 lbs to around 8.2 lbs. We improved our beam by almost 2 pounds.

Our reinforcement plan will aim to have less bend closer to the holder, and more evenly distribute the stress across our beam. To do this I will add a horizontal bracket on each side of the beam, jointed with the attachement. This will decrease overall displacement of the beam, while not adding too much weight to our beam in order to stay below a weight of 13 grams. 

## FEA_Part_4

### Assignment Description

Using what we learned from the Onshape course we took during FEA Part 3, we were assigned to run the FEA simulations and ajust the beam accordingly. We had to stay within the parameters (had to be less than 13g in weight, and the beam was considered diqualified from the cometition if it bend past 35mm)


### Reflection

Looking at the first image, our beam went from being able to hold 6.774 lbs to around 8.2 lbs. We improved our beam by almost 2 pounds.

### Part Link

[Onshape Document](https://cvilleschools.onshape.com/documents/5517eb4141dde3d11583bfcf/w/76219d7db810f33e12052ceb/e/731981f9da0684932d2a38a5)

### Part Image

|Image of Model |Stress |Displacement |
|-|-|-|
|<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/Beam%20Starter%20+%20Holder%20(1).png?raw=true" width="400"> |<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/Assembly%201%20(2).png?raw=true" width="400"> |<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/Assembly%201%20(3).png?raw=true" width="400"> |

### Reflection

The FEA simulation was very helpful in predicting where the beam was the most weak. Using the simulation, we could repair the areas that were weaker. One thing we learned from the inital beam design, and testing it, was that the point where the beam and the frame connected was weak. Using what we learned from the first iteration, we made the second beam to be better fused to the frame. When we tested our beam for the second time, the beam broke right before the point of connection.

Our first beam did quite well on the first simulation, being able to hold around 7 pounds, while deforming 32mm. The stress for the beam was focused more in the middle-holder side of the beam, and we wanted it to be as close to the holder as possible. Our second beam was able to hold more towards 9 pounds, and was still able to keep a displacement towards 34mm.
