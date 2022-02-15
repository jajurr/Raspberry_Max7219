import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from MyMax7219 import MyMatrix
from random import randint
import time

matrix = MyMatrix()

print("Created device")
while 1 == 1: # Run forever
    if GPIO.input(11) == GPIO.HIGH:
        print("Button 11 was pushed!")
        time.sleep(0.5)
        for i in range(8):
            for j in range(8):
                matrix.pixel(i,j,randint(0,1))
                time.sleep(0.0002)