import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

CLRRED = (255, 0, 0)
CLRGREEN = (0, 255, 0)
CLRBLUE = (0, 0, 255)

pixels.brightness = .02

led = DigitalInOut(board.D13)

led.switch_to_output()

d4 = DigitalInOut(board.D4)
d5 = DigitalInOut(board.D5)
d4.switch_to_input(pull = Pull.DOWN)
d5.switch_to_input(pull = Pull.DOWN)

while True:
    d4_read = d4.value
    d5_read = d5.value

    if d4_read and d5_read:
        pixels.fill(CLRBLUE)
    elif d4_read:
        pixels.fill(CLRRED)
    elif d5_read:
        pixels.fill(CLRGREEN)
    else:
        pixels.fill(0)

    time.sleep(0.1)
