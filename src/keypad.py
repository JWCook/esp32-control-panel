# Modified from:
#   https://learn.adafruit.com/numpad-4000-mechanical-keyswitch-data-entry-device
# from keypad import KeyMatrix
from time import sleep

import board
from adafruit_matrixkeypad import Matrix_Keypad
from digitalio import DigitalInOut
from neopixel import NeoPixel
import adafruit_pcf8575

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

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector
expander = adafruit_pcf8575.PCF8575(i2c)

EXP_ROW_PINS = (15, 13, 11, 9, 1)
EXP_COL_PINS = (14, 12, 10, 8, 0)

EXP_KEYS = (
    (1, 2, 3, 4, 5),
    (6, 7, 8, 9, 0),
    ('A', 'B', 'C', 'D', 'E'),
    ('F', 'G', 'H', 'I', 'J'),
    ('K', 'L', 'M', 'N', 'O'),
)
# get a 'digitalio' like pin from the pcf
# led = expander.get_pin(8)
# button = expander.get_pin(0)

# # Setup pin7 as an output that's at a high logic level default
# led.switch_to_output(value=True)
# # Setup pin0 as an output that's got a pullup
# button.switch_to_input(pull=digitalio.Pull.UP)
# while True:
#     led.value = button.value
#     time.sleep(0.01)  # debounce


# key_pixels = NeoPixel(board.D5, 30, brightness=0.1)
# key_pixels.fill(WHITE)
# keys = KeyMatrix(
#     row_pins=ROW_PINS,
#     column_pins=COL_PINS,
#     columns_to_anodes=False,
# )

# Pins on the MCU board
# keypad = Matrix_Keypad(
#     [DigitalInOut(pin) for pin in ROW_PINS],
#     [DigitalInOut(pin) for pin in COL_PINS],
#     KEYS,
# )

# Pins on the expansion board
out_pins = [expander.get_pin(pin) for pin in COL_PINS]
for pin in out_pins:
    pin.switch_to_output(value=True)
keypad = Matrix_Keypad(
    [expander.get_pin(pin) for pin in ROW_PINS],
    out_pins,
    EXP_KEYS,
)

while True:
    board_pixels.fill((10, 10, 10))
    pressed_keys = keypad.pressed_keys
    if pressed_keys:
        print("Pressed: ", pressed_keys)
        board_pixels.fill((0, 10, 0))
    sleep(0.1)
