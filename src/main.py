from time import sleep

import board
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.neopixel import NeoPixel as SSNeoPixel
from adafruit_seesaw.rotaryio import IncrementalEncoder
from adafruit_seesaw.seesaw import Seesaw
from adafruit_ssd1327 import SSD1327
from digitalio import DigitalInOut, Direction, Pull
from displayio import I2CDisplay, release_displays
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
    def __init__(self, idx, pin):
        super().__init__(idx)
        self.io = DigitalInOut(pin)
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
    def __init__(self, idx, pin):
        self.io = DigitalInOut(pin)
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


class RGBPushButton(PushButton):
    def __init__(self, idx, pin, r_pin, g_pin, b_pin):
        super().__init__(idx, pin)

        self.red_led = DigitalInOut(r_pin)
        self.red_led.switch_to_output()

        self.grn_led = DigitalInOut(g_pin)
        self.grn_led.switch_to_output()

        self.blu_led = DigitalInOut(b_pin)
        self.blu_led.switch_to_output()

    def set_color(self, r=False, g=False, b=False):
        print(f'RGBPushButton {self.idx} set_color: r={r}, g={g}, b={b}')
        # Pull-down is on, so we invert the value
        self.red_led.value = not r
        self.grn_led.value = not g
        self.blu_led.value = not b


# print(dir(board))
board_pixels = NeoPixel(board.NEOPIXEL, 1)
board_pixels.fill((10, 10, 0))
i2c = board.STEMMA_I2C()


release_displays()
display_bus = I2CDisplay(i2c, device_address=0x3D)
display = SSD1327(display_bus, width=128, height=128)


# encoder_1 = RotaryEncoder(1, i2c, 0x36)
# encoder_2 = RotaryEncoder(2, i2c, 0x37)
# encoder_3 = RotaryEncoder(3, i2c, 0x38)

switch_1 = ToggleSwitch(1, board.A0)
switch_2 = ToggleSwitch(2, board.A1)
switch_3 = ToggleSwitch(3, board.A2)
switch_4 = ToggleSwitch(4, board.A3)

# button_1 = RGBPushButton(1, board.D13, board.D12, board.D27, board.D33)
button_1 = PushButton(2, board.D13)
button_2 = PushButton(2, board.D12)
button_3 = PushButton(3, board.D27)
button_4 = PushButton(4, board.D33)
button_5 = PushButton(5, board.D15)
button_6 = PushButton(6, board.D32)
button_7 = PushButton(7, board.D14)
button_8 = PushButton(8, board.A4)

board_pixels.fill((0, 0, 10))

# while True:
#     button_1.set_color(r=True)
#     sleep(1)
#     button_1.set_color(g=True)
#     sleep(1)
#     button_1.set_color(b=True)
#     sleep(1)

devices = [
    # encoder_1,
    # encoder_2,
    # encoder_3,
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

import displayio
import terminalio
from adafruit_display_text import label

WIDTH = 128
HEIGHT = 128
BORDER = 1
FONTSCALE = 1


def display_demo():

    splash = displayio.Group()
    display.show(splash)

    # Draw a background rectangle, but not the full display size
    color_bitmap = displayio.Bitmap(
        display.width - BORDER * 2, display.height - BORDER * 2, 1
    )
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White
    bg_sprite = displayio.TileGrid(
        color_bitmap, pixel_shader=color_palette, x=BORDER, y=BORDER
    )
    splash.append(bg_sprite)

    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(
        display.width - BORDER * 4, display.height - BORDER * 4, 1
    )
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x888888  # Gray
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=BORDER * 2, y=BORDER * 2
    )
    splash.append(inner_sprite)

    # Draw a label
    text = "Hello World!"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)


display_demo()


while True:
    for device in devices:
        device.read()

# import pwmio
# red_led = pwmio.PWMOut(board.A5, frequency=5000, duty_cycle=65535)
# red_led = pwmio.PWMOut(board.A5, frequency=5000, duty_cycle=0)
print(red_led)

# while True:
#    red_led.duty_cycle = 65535
#    sleep(1)
#    red_led.duty_cycle = 0
#    sleep(1)

# while True:
#    for i in range(100):
#        # PWM LED up and down
#        if i < 50:
#            red_led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
#        else:
#            red_led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
#        sleep(0.01)
