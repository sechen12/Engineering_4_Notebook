#type: ignore
# I copied my entire coding assignment from ELias Garcia. https://github.com/egarcia28/Engineering_4_Notebook/tree/main/raspberry-pi

import time
import board
import digitalio

for x in range(10):
    print(10-x) #prints 10 --> 1 in descending order
    time.sleep(1) #delays the count by one second in between numbers
print("liftoff!") #print liftoff when the rest of the code is finished running