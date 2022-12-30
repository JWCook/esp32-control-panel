import board
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.neopixel import NeoPixel
from adafruit_seesaw.rotaryio import IncrementalEncoder
from adafruit_seesaw.seesaw import Seesaw
from digitalio import DigitalInOut, Direction, Pull

i2c = board.STEMMA_I2C()

# qt_enc1 = Seesaw(i2c, addr=0x36)
# qt_enc1.pin_mode(24, qt_enc1.INPUT_PULLUP)
# button1 = DigitalIO(qt_enc1, 24)
# encoder1 = IncrementalEncoder(qt_enc1)
# last_position1 = None
# button_held1 = False
# pixel1 = NeoPixel(qt_enc1, 6, 1)
# pixel1.brightness = 0.2
# pixel1.fill(0xFF0000)

# qt_enc2 = Seesaw(i2c, addr=0x37)
# qt_enc2.pin_mode(24, qt_enc2.INPUT_PULLUP)
# button2 = DigitalIO(qt_enc2, 24)
# encoder2 = IncrementalEncoder(qt_enc2)
# last_position2 = None
# button_held2 = False
# pixel2 = NeoPixel(qt_enc2, 6, 1)
# pixel2.brightness = 0.2
# pixel2.fill(0x0000FF)

qt_enc3 = Seesaw(i2c, addr=0x38)
qt_enc3.pin_mode(24, qt_enc3.INPUT_PULLUP)
button3 = DigitalIO(qt_enc3, 24)
encoder3 = IncrementalEncoder(qt_enc3)
last_position3 = None
button_held3 = False
pixel3 = NeoPixel(qt_enc3, 6, 1)
pixel3.brightness = 0.2
pixel3.fill(0x00FF00)


switch_1 = DigitalInOut(board.A0)
switch_1.direction = Direction.INPUT
switch_1.pull = Pull.UP
last_switch_1 = None


while True:

    # negate the position to make clockwise rotation positive
    # position1 = -encoder1.position
    # position2 = -encoder2.position
    position3 = -encoder3.position

    # if position1 != last_position1:
    #     last_position1 = position1
    #     print("Position 1: {}".format(position1))

    # if not button1.value and not button_held1:
    #     button_held1 = True
    #     pixel1.brightness = 0.5
    #     print("Button 1 pressed")

    # if button1.value and button_held1:
    #     button_held1 = False
    #     pixel1.brightness = 0.2
    #     print("Button 1 released")

    # if position2 != last_position2:
    #     last_position2 = position2
    #     print("Position 2: {}".format(position2))

    # if not button2.value and not button_held2:
    #     button_held2 = True
    #     pixel2.brightness = 0.5
    #     print("Button 2 pressed")

    # if button2.value and button_held2:
    #     button_held2 = False
    #     pixel2.brightness = 0.2
    #     print("Button 2 released")

    if position3 != last_position3:
        last_position3 = position3
        print("Position 3: {}".format(position3))

    if not button3.value and not button_held3:
        button_held3 = True
        pixel3.brightness = 0.5
        print("Button 3 pressed")

    if button3.value and button_held3:
        button_held3 = False
        pixel3.brightness = 0.2
        print("Button 3 released")

    if switch_1.value != last_switch_1:
        last_switch_1 = switch_1.value
        print("Switch 1: {}".format(switch_1.value))