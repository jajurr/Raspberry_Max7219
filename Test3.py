#!/usr/bin/env python

import time
from random import randrange
import max7219.led as led

# create matrix device
device = led.matrix(cascaded=1)
device.brightness(7)
try:
  while True:
    # zeilenweise von links nach rechts einschalten
    device.clear()
    for y in range(8):
      for x in range(8):
        device.pixel(x, y, 1, redraw=True)
        time.sleep(0.1)

    # und wieder ausknipsen
    for y in range(8):
      for x in range(8):
        device.pixel(x, y, 0, redraw=True)
        time.sleep(0.1)

except KeyboardInterrupt:
  device.clear()