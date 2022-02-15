import max7219
from machine import Pin, SPI
spi = SPI(1)
display = max7219.Matrix8x8(spi, Pin('X5'), 1)
display.pixel(0,0,1)
display.show()