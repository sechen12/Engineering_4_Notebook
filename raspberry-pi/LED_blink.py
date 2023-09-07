import board
import time
import digitalio

led = digitalio.DigitalInOut(board.LED) #defines LED
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True #turns LED on
    time.sleep(0.5) #pause
    led.value = False #turns LED off
    time.sleep(0.5) #pause