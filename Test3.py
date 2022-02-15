#!/usr/bin/env python

import max7219.led as led

matrix = led.matrix(cascaded=1)
matrix.clear()

matrix.letter(deviceId = 0, ord("A"))