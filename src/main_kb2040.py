import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Hello World!")
while True:
    # pixels.fill((255, 0, 0))
    # time.sleep(0.5)
    # pixels.fill((128, 0, 128))
    # time.sleep(0.5)
    # pixels.fill((0, 128, 128))
    # time.sleep(0.5)
    # pixels.fill((0, 255, 0))
    # time.sleep(0.5)
    # pixels.fill((0, 0, 0))
    # time.sleep(0.1)

    pixels.fill((128, 0, 128))
    time.sleep(5)
    pixels.fill((0, 128, 128))
    time.sleep(5)