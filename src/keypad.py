# Modified from:
#   https://learn.adafruit.com/numpad-4000-mechanical-keyswitch-data-entry-device
# from keypad import KeyMatrix
from time import sleep

import adafruit_pcf8575
import board
from adafruit_matrixkeypad import Matrix_Keypad
from digitalio import DigitalInOut
from neopixel import NeoPixel

# BLUE = 0x000510
# WHITE = 0x303030
# RED = 0xFF0000
ROW_PINS = (board.IO37, board.IO36, board.IO6, board.IO14, board.IO17)
COL_PINS = (board.IO44, board.IO35, board.IO5, board.IO12, board.IO18)

EXP_ROW_PINS = (15, 13, 11, 9, 1)
EXP_COL_PINS = (14, 12, 10, 8, 0)

KEYS = (
    (1, 2, 3, 4, 5),
    (6, 7, 8, 9, 0),
    ('A', 'B', 'C', 'D', 'E'),
    ('F', 'G', 'H', 'I', 'J'),
    ('K', 'L', 'M', 'N', 'O'),
)

board_pixels = NeoPixel(board.NEOPIXEL, 1)
board_pixels.fill((10, 10, 10))

# i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector
# expander = adafruit_pcf8575.PCF8575(i2c)


# With the keypad library
# from keypad import KeyMatrix
# km = KeyMatrix(
#     row_pins=ROW_PINS,
#     column_pins=COL_PINS,
# )
# while True:
#     event = km.events.get()
#     if event:
#         print(event)

# Pins on the MCU board
keypad = Matrix_Keypad(
    [DigitalInOut(pin) for pin in ROW_PINS],
    [DigitalInOut(pin) for pin in COL_PINS],
    KEYS,
)

# Pins on the expansion board
# out_pins = [expander.get_pin(pin) for pin in COL_PINS]
# for pin in out_pins:
#     pin.switch_to_output(value=True)
# keypad = Matrix_Keypad(
#     [expander.get_pin(pin) for pin in ROW_PINS],
#     out_pins,
#     KEYS,
# )


while True:
    board_pixels.fill((10, 10, 10))
    pressed_keys = keypad.pressed_keys
    if pressed_keys:
        print("Pressed: ", pressed_keys)
        board_pixels.fill((0, 10, 0))
    sleep(0.1)
