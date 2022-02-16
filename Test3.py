import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from MyMax7219 import MyMatrix
from random import randint
import time

matrix = MyMatrix()

intRichtung = 0

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

def Richtung(gpio):
    global intRichtung
    if GPIO.input(11) == GPIO.HIGH:
        print("Button 11 was pushed!")
        intRichtung += 1
    if GPIO.input(12) == GPIO.HIGH:
        print("Button 12 was pushed!")
        intRichtung += 3
    modulu = intRichtung % 4
    print(modulu)
    if modulu == 0:
        print("Modulo 0")
    if modulu == 1:
        print("Modulo 1")
    if modulu == 2:
        print("Modulo 2")
    if modulu == 3:
        print("Modulo 3")


GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(11, GPIO.FALLING, callback=Richtung)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(12, GPIO.FALLING, callback=Richtung)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(13, GPIO.FALLING, callback=Richtung)


	
print("Created device")
while 1 == 1: # Run forever
    if GPIO.input(11) == GPIO.HIGH:
        print("Button 11 was pushed!")
        time.sleep(0.5)
        for i in range(8):
            for j in range(8):
                matrix.pixel(i,j,randint(0,1))
                time.sleep(0.0002)