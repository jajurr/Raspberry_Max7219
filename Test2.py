#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import RPi.GPIO as gpio # Import Raspberry Pi GPIO library

gpio.setmode(gpio.BCM)
taster = [14,15,18,23]

print("Created device")

while (True) : # Run forever
    if (gpio == 11):
        print("Button was pushed!")
    if (gpio == 12):
        print("Button was pushed!")
    if (gpio == 13):
        print("Button was pushed!")
    if (gpio == 14):
        print("Button was pushed!")
    if (gpio == 15):
        print("Button was pushed!")
    if (gpio == 16):
        print("Button was pushed!")
    if (gpio == 17):
        print("Button was pushed!")
    if (gpio == 18):
        print("Button was pushed!")