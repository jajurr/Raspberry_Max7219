#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import RPi.GPIO as gpio
import time
import max7219.led as led
from random import randint


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
while True: # Run forever
    if GPIO.input(15) == GPIO.HIGH:
        print("Button 10 was pushed!")
    if GPIO.input(11) == GPIO.HIGH:
        print("Button 11 was pushed!")
    if GPIO.input(12) == GPIO.HIGH:
        print("Button 12 was pushed!")
    if GPIO.input(13) == GPIO.HIGH:
        print("Button 13 was pushed!")