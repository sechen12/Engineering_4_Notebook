# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [Launchpad_1_Countdown](#Launchpad_1_Countdown)
* [Launchpad_2_Lights](#Launchpad_2_Lights)
* [Launchpad_3_Button](#Launchpad_3_Button)

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
```

### Reflection

This assignment was relatively staight foward. It was the fastest for me to complete because of the new knowledge I've collected about Circuit Python becuase of these "Launchpads". One thing I did have trouble on is figuring out the direction I wanted to pull the button. Unfortunately, I still don't understand how they work - I used trial and error to complete the code. Although the double/single equal sign difference is something that I should have been familiar with by now, I learned that the double equal sign (==) is used to check if what your statement is true:
```python
if button.value == True:
```
It was also recently clarified to me that the ```While True: ```statement is used to continuously run the code. This statement was important in the "Button" code becuase the program needed to constantly check if the button was true or false (off/on). I made the mistake of not using a "While True" statement in my intial code.
