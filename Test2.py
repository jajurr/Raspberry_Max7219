#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import max7219.led as led
import time
from luma.led_matrix.device import max7219

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

matrixe = 1
matrix = led.matrix(cascaded=matrixe)

print("Created device")
while 1 == 1: # Run forever
    matrix.pixel(1,1,1)
    if GPIO.input(11) == GPIO.HIGH:
        print("Button 11 was pushed!")
        time.sleep(0.5)
    if GPIO.input(12) == GPIO.HIGH:
        print("Button 12 was pushed!")
        time.sleep(0.5)
    if GPIO.input(13) == GPIO.HIGH:
        print("Button 13 was pushed!")
        time.sleep(0.5)
