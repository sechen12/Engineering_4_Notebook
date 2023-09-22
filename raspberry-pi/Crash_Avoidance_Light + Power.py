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
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP11) # getting the computer to recognize the OLED
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # defining the OLED

sda_pin = board.GP14 # defining serial data pin
scl_pin = board.GP15 # defining serial clock pin
i2c = busio.I2C(scl_pin, sda_pin) # allowing the sda and scl pins to communicate using one channel
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # initializes the sensor


while True:
    print(f"x accelteration: {mpu.acceleration[0]}.") # this is an 'f-string'; it's a certain syntax that helps print the variables clearer
    print(f"y accelteration: {mpu.acceleration[1]}.")
    print(f"z accelteration: {mpu.acceleration[2]}.")
    print("")
    time.sleep(.5)

    
    # create the display group
    splash = displayio.Group()

    # add title block to display group
    title = "ANGULAR VELOCITY"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)

    text_area.text = (f“your_fstring_with_gyro_values_here”)
    # Don't forget to round the angular velocity values to three decimal places

    # send display group to screen
    display.show(splash)


    if mpu.acceleration[0] > 9 or mpu.acceleration[2] < 0: # if the x value is greater than 9, or the z value is less than 2, turn the LED on
        led.value = True
    else:
        led.value = False # if the statement isn't true, don't turn the LED on

## MPU adress = 0x68
## OLED adress = 0x3d