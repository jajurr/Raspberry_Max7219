import time
from random import randrange
import max7219.led as led

# create matrix device
device = led.matrix(cascaded=2)
device.brightness(7)

try:
  while True:
    device.clear()

    # eine LED durch alle Zeilen laufen lassen
    for y in range(8):
      for x in range(8):
        device.pixel(x, y, 1, redraw=True)
        time.sleep(0.01)
        device.pixel(x, y, 0, redraw=True)
        time.sleep(0.01)

except KeyboardInterrupt:
  device.clear()