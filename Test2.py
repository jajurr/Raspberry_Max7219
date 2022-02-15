#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import max7219.led as led
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

matrixe = 1
matrix = led.matrix(cascaded=matrixe)

print("Created device")
matrix.show_message("READY")
while 1 == 1: # Run forever
    with canvas(self.device) as draw:
        draw.point((1, 1))
    if GPIO.input(11) == GPIO.HIGH:
        print("Button 11 was pushed!")
        time.sleep(0.5)
    if GPIO.input(12) == GPIO.HIGH:
        print("Button 12 was pushed!")
        time.sleep(0.5)
    if GPIO.input(13) == GPIO.HIGH:
        print("Button 13 was pushed!")
        time.sleep(0.5)
