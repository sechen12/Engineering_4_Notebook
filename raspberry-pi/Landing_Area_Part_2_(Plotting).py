#type: ignore
# I copied my entire coding assignment from Grant Gastinger. https://github.com/ggastin30/Engineering_4_Notebook

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
