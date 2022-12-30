import board
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.neopixel import NeoPixel
from adafruit_seesaw.rotaryio import IncrementalEncoder
from adafruit_seesaw.seesaw import Seesaw
from digitalio import DigitalInOut, Direction, Pull


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

        self.pixel = NeoPixel(self.seesaw, 6, 1)
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
    def __init__(self, idx, pin):
        super().__init__(idx)
        self.pin = pin
        self.pin.direction = Direction.INPUT
        self.pin.pull = Pull.UP
        self.last_value = None

    def read(self):
        value = self.pin.value
        if value != self.last_value:
            self.last_value = value
            print("Switch {}: {}".format(self.idx, value))
        return value


class PushButton(InputDevice):
    def __init__(self, idx, pin):
        self.pin = pin
        self.pin.direction = Direction.INPUT
        self.pin.pull = Pull.UP

        self.idx = idx
        self.last_value = False

    def read(self):
        value = not self.pin.value
        if value != self.last_value:
            self.last_value = value
            print("Button {}: {}".format(self.idx, value))
        return value


i2c = board.STEMMA_I2C()

# encoder_1 = RotaryEncoder('rotary 1', i2c, 0x36)
# encoder_2 = RotaryEncoder('rotary 2', i2c, 0x37)
encoder_3 = RotaryEncoder(3, i2c, 0x38)

switch_1 = ToggleSwitch(1, DigitalInOut(board.A0))
switch_2 = ToggleSwitch(2, DigitalInOut(board.A1))
switch_3 = ToggleSwitch(3, DigitalInOut(board.A2))
switch_4 = ToggleSwitch(4, DigitalInOut(board.A3))

button_1 = PushButton(1, DigitalInOut(board.D13))
button_2 = PushButton(2, DigitalInOut(board.D12))
button_3 = PushButton(3, DigitalInOut(board.D27))
button_4 = PushButton(4, DigitalInOut(board.D33))
button_5 = PushButton(5, DigitalInOut(board.D15))
button_6 = PushButton(6, DigitalInOut(board.D32))
button_7 = PushButton(7, DigitalInOut(board.D14))
button_8 = PushButton(8, DigitalInOut(board.A4))

devices = [
    # encoder_1,
    # encoder_2,
    encoder_3,
    switch_1,
    switch_2,
    switch_3,
    switch_4,
    button_1,
    button_2,
    button_3,
    button_4,
    button_5,
    button_6,
    button_7,
    button_8,
]


while True:
    for device in devices:
        device.read()
