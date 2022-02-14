#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import RPi.GPIO as gpio
import time
import max7219.led as led
from random import randint

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
taster = [11,12,13]
matrixe = 1
matrix = led.matrix(cascaded=matrixe)
height = 7
width = (8*matrixe)-1




for i in taster:
  gpio.setup(i,gpio.IN,pull_up_down=gpio.PUD_UP)
  gpio.add_event_detect(i, gpio.FALLING, callback=steuerung)
        
def steuerung(gpio):
  global richtung
  if GPIO.input(11) == GPIO.HIGH:   #rechts
    richtung = [1,0]
  elif GPIO.input(12) == GPIO.HIGH: #links
    richtung = [-1,0]
        
        