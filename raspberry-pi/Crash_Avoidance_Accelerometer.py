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