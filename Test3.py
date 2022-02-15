import time
from random import randrange
import max7219.led as led

# create matrix device
device = led.matrix(cascaded=2)
device.brightness(7)

try:
  while True:
    device.clear()
    print("Created device")
    
    device.pixel(1, 1, 1, redraw=True)
    time.sleep(1)

except KeyboardInterrupt:
  device.clear()