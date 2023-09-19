from time import sleep

import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.neopixel import NeoPixel as SSNeoPixel
from adafruit_seesaw.rotaryio import IncrementalEncoder
from adafruit_seesaw.seesaw import Seesaw
from digitalio import DigitalInOut, Direction, Pull
from neopixel import NeoPixel


class InputDevice:
    def __init__(self, idx):
        self.idx = idx

    def read(self):
        raise NotImplementedError


class RotaryEncoder(InputDevice):
    def __init__(self, idx, i2c, address):
        super().__init__(idx)
        self.seesaw = Seesaw(i2c, addr=address)
        self.seesaw.pin_mode(24, self.seesaw.INPUT_PULLUP)
        self.button = DigitalIO(self.seesaw, 24)
        self.encoder = IncrementalEncoder(self.seesaw)

        self.pixel = SSNeoPixel(self.seesaw, 6, 1)
        self.pixel.brightness = 0.2
        self.pixel.fill(0x00FF00)

        self.last_position = None
        self.last_button_value = False

    def read(self):
        position = -self.encoder.position
        if position != self.last_position:
            self.last_position = position
            print("Rotary {} position: {}".format(self.idx, position))

        button_value = not self.button.value
        if button_value and not self.last_button_value:
            self.pixel.brightness = 0.5
            print("Rotary {} button pressed".format(self.idx))
        elif self.button.value and self.last_button_value:
            self.pixel.brightness = 0.2
            print("Rotary {} button released".format(self.idx))
        self.last_button_value = button_value

        return position


class ToggleSwitch(InputDevice):
    def __init__(self, idx, pin=None, io=None):
        super().__init__(idx)
        self.io = io or DigitalInOut(pin)
        self.io.direction = Direction.INPUT
        self.io.pull = Pull.UP
        self.last_value = None

    def read(self):
        value = self.io.value
        if value != self.last_value:
            self.last_value = value
            print("Switch {}: {}".format(self.idx, value))
        return value


class PushButton(InputDevice):
    def __init__(self, idx, pin=None, io=None):
        self.io = io or DigitalInOut(pin)
        self.io.direction = Direction.INPUT
        self.io.pull = Pull.UP

        self.idx = idx
        self.last_value = False

    def read(self):
        value = not self.io.value
        if value != self.last_value:
            self.last_value = value
            print("Button {}: {}".format(self.idx, value))
            if value:
                board_pixels.fill((0, 10, 0))
                # sleep(0.5)
                # board_pixels.fill((0, 0, 10))
            else:
                board_pixels.fill((0, 0, 10))
        return value


board_pixels = NeoPixel(board.NEOPIXEL, 1)
board_pixels.fill((0, 10, 10))

i2c = busio.I2C(board.SCL, board.SDA)
# i2c = board.STEMMA_I2C()
expander = MCP23017(i2c, address=0x20)

# encoder_1 = RotaryEncoder(1, i2c, 0x36)
# encoder_2 = RotaryEncoder(2, i2c, 0x37)
# encoder_3 = RotaryEncoder(3, i2c, 0x38)

switch_1 = ToggleSwitch(1, expander.get_pin(1))
# switch_2 = ToggleSwitch(2, board.A1)
# switch_3 = ToggleSwitch(3, board.A2)
# switch_4 = ToggleSwitch(4, board.A3)

button_1 = PushButton(2, expander.get_pin(0))
# button_2 = PushButton(2, board.D12)
# button_3 = PushButton(3, board.D27)
# button_4 = PushButton(4, board.D33)
# button_5 = PushButton(5, board.D15)
# button_6 = PushButton(6, board.D32)
# button_7 = PushButton(7, board.D14)
# button_8 = PushButton(8, board.A4)

board_pixels.fill((0, 0, 10))

devices = [
    # encoder_1,
    # encoder_2,
    # encoder_3,
    switch_1,
    # switch_2,
    # switch_3,
    # switch_4,
    button_1,
    # button_2,
    # button_3,
    # button_4,
    # button_5,
    # button_6,
    # button_7,
    # button_8,
]


while True:
    for device in devices:
        device.read()
