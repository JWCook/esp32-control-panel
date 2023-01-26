# Modified from:
#   https://learn.adafruit.com/numpad-4000-mechanical-keyswitch-data-entry-device
# from keypad import KeyMatrix
from time import sleep

import board
from adafruit_matrixkeypad import Matrix_Keypad
from digitalio import DigitalInOut
from neopixel import NeoPixel

# COLUMNS = 5
# ROWS = 5

# BLUE = 0x000510
# WHITE = 0x303030
# RED = 0xFF0000

# ROW_PINS = (board.D12, board.D33, board.D32)
# COL_PINS = (board.D13, board.D27, board.D15, board.D14)
# Switched a pair of pins, whoops
# ROW_PINS = (board.D27, board.D33, board.D32)
# COL_PINS = (board.D12, board.D13, board.D15, board.D14)
# KEYS = ((1, 2, 3, "A"), (4, 5, 6, "B"), (7, 8, 9, "C"))


ROW_PINS = (board.IO38, board.IO33)
COL_PINS = (board.IO1, board.IO3)
KEYS = ((1, 2), (4, 5))

board_pixels = NeoPixel(board.NEOPIXEL, 1)
board_pixels.fill((10, 10, 10))

# key_pixels = NeoPixel(board.D5, 30, brightness=0.1)
# key_pixels.fill(WHITE)

# keys = KeyMatrix(
#     row_pins=ROW_PINS,
#     column_pins=COL_PINS,
#     columns_to_anodes=False,
# )

keypad = Matrix_Keypad(
    [DigitalInOut(pin) for pin in ROW_PINS],
    [DigitalInOut(pin) for pin in COL_PINS],
    KEYS,
)

while True:
    board_pixels.fill((10, 10, 10))
    pressed_keys = keypad.pressed_keys
    if pressed_keys:
        print("Pressed: ", pressed_keys)
        board_pixels.fill((0, 10, 0))
    sleep(0.1)
