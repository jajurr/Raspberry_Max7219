#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import RPi.GPIO as gpio # Import Raspberry Pi GPIO library

gpio.setmode(gpio.BCM)

print("Created device")

while (True) : # Run forever
    if (gpio == 18):
        print("Button was pushed!")
    if (gpio == 17):
        print("Button was pushed!")
    if (gpio == 27):
        print("Button was pushed!")
    if (gpio == 23):
        print("Button was pushed!")
    if (gpio == 22):
        print("Button was pushed!")
    if (gpio == 24):
        print("Button was pushed!")
    if (gpio == 25):
        print("Button was pushed!")
    if (gpio == 9):
        print("Button was pushed!")