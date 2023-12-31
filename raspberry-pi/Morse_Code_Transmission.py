#type: ignore
# I copied my entire coding assignment from Grant Gastinger. https://github.com/ggastin30/Engineering_4_Notebook

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
