#type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print(f"x Angular Velocity: {}.")
    print(f"y Angular Velocity: {}.")
    print(f"z Angular Velocity: {}.")
    time.sleep(.5)