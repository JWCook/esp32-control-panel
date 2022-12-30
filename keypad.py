# Modified from:
#   https://learn.adafruit.com/numpad-4000-mechanical-keyswitch-data-entry-device
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from neopixel import NeoPixel

from keypad import KeyMatrix

COLUMNS = 5
ROWS = 5

BLUE = 0x000510
WHITE = 0x303030
RED = 0xFF0000


board_pix = NeoPixel(board.NEOPIXEL, 1, brightness=0.1)
board_pix[0] = BLUE

key_pixels = NeoPixel(board.D5, 30, brightness=0.1)
key_pixels.fill(WHITE)

keys = KeyMatrix(
    row_pins=(board.D4, board.A3, board.A2, board.A1, board.A0),
    column_pins=(board.D13, board.D12, board.D11, board.D10, board.D9),
    columns_to_anodes=False,
)

kbd = Keyboard(usb_hid.devices)

# fmt: off
keycode_LUT = [
    0, 1, 2, 3, 4,
    5, 6, 7, 8,
    10, 11, 12, 13, 14,
    15, 16, 17, 18,
    20, 21, 23, 24
]
pixel_LUT = [
    0, 1, 2, 3, 4,
    8, 7, 6, 5,
    10, 11, 12, 13, 14,
    18, 17, 16, 15,
    20, 21, 23, 24
]
# fmt: on

# keycode dictionary including modifier state and keycodes
keymap = {
    0: Keycode.KEYPAD_NUMLOCK,
    1: Keycode.BACKSPACE,
    2: Keycode.FORWARD_SLASH,
    3: Keycode.KEYPAD_ASTERISK,
    4: Keycode.KEYPAD_MINUS,
    5: Keycode.PAGE_UP,
    6: Keycode.KEYPAD_SEVEN,
    7: Keycode.KEYPAD_EIGHT,
    8: Keycode.KEYPAD_NINE,
    9: Keycode.PAGE_DOWN,
    10: Keycode.KEYPAD_FOUR,
    11: Keycode.KEYPAD_FIVE,
    12: Keycode.KEYPAD_SIX,
    13: Keycode.KEYPAD_PLUS,
    14: Keycode.SHIFT,
    15: Keycode.KEYPAD_ONE,
    16: Keycode.KEYPAD_TWO,
    17: Keycode.KEYPAD_THREE,
    18: Keycode.CONTROL,
    19: Keycode.KEYPAD_ZERO,
    20: Keycode.KEYPAD_PERIOD,
    21: Keycode.KEYPAD_EQUALS,
}

shift_mod = False
ctrl_mod = False


while True:
    key_event = keys.events.get()
    if not key_event:
        continue

    keycode = keymap[keycode_LUT.index(key_event.key_number)]
    pixel_idx = pixel_LUT.index(key_event.key_number)
    keypresses = [keycode]

    if key_event.pressed:
        if keycode == Keycode.SHIFT:
            shift_mod = True
        elif keycode == Keycode.CONTROL:
            ctrl_mod = True

        if ctrl_mod:
            keypresses.insert(0, Keycode.CONTROL)
        if shift_mod:
            keypresses.insert(0, Keycode.SHIFT)

        kbd.press(*keypresses)
        print(keycode)
        key_pixels[pixel_idx] = RED
        board_pix[0] = WHITE

    elif key_event.released:
        if keycode == Keycode.SHIFT:
            shift_mod = False
        elif keycode == Keycode.CONTROL:
            ctrl_mod = False

        kbd.release(keycode)
        key_pixels[pixel_idx] = WHITE
        board_pix[0] = BLUE
