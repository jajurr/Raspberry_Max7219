import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from MyMax7219 import MyMatrix
from random import randint
import time

matrix = MyMatrix()

intRichtung = 0
modulu = 0

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

def Richtung(gpio):
    global intRichtung, modulu
    print(gpio)
    if GPIO.input(11) == GPIO.HIGH:
        print("Button 11 was pushed!")
        intRichtung = intRichtung + 1
        print("intRichtung:")
        print(intRichtung)
    if GPIO.input(12) == GPIO.HIGH:
        print("Button 12 was pushed!")
        intRichtung = intRichtung + 3
        print("intRichtung:")
        print(intRichtung)
    modulu = intRichtung % 4
    print("modulu:")
    print(modulu)
    if modulu == 0:
        print("modulu:")
        print(modulu)
    if modulu == 1:
        print("modulu:")
        print(modulu)
    if modulu == 2:
        print("modulu:")
        print(modulu)
    if modulu == 3:
        print("modulu:")
        print(modulu)


GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(11, GPIO.FALLING, callback=Richtung)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(12, GPIO.FALLING, callback=Richtung)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

	
print("Created device")
while 1 == 1: # Run forever
    if GPIO.input(13) == GPIO.HIGH:
        print("Button 13 was pushed!")
        time.sleep(0.5)