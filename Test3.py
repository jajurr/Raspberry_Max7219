from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.legacy.font import proportional, LCD_FONT
serial = spi(port=0, device=0, gpio=noop(), block_orientation=-90)
device = max7219(serial, width=32, height=24)
with canvas(device) as draw:
draw.rectangle(device.bounding_box, outline="white")
text(draw, (2, 2), ".", fill="white", font=proportional(LCD_FONT))
