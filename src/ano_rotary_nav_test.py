import time, gc, os
import neopixel
import board, digitalio
import feathers3
import board
import digitalio
import rotaryio


# Show available memory and flash size
print("Memory Info - gc.mem_free()")
print("---------------------------")
print("{} Bytes\n".format(gc.mem_free()))

flash = os.statvfs('/')
flash_size = flash[0] * flash[2]
flash_free = flash[0] * flash[3]

print("Flash - os.statvfs('/')")
print("---------------------------")
print("Size: {} Bytes\nFree: {} Bytes\n".format(flash_size, flash_free))

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.RGB)
feathers3.set_ldo2_power(True)
color_index = 0

# The pin assignments for the breakout pins. Update this is you are not using a Feather.
ENCA = board.IO17
ENCB = board.IO18
SW1 = board.IO14
SW2 = board.IO12
SW3 = board.IO6
SW4 = board.IO5
SW5 = board.IO36

# Rotary encoder setup
encoder = rotaryio.IncrementalEncoder(ENCA, ENCB)
last_position = 0

# Button pin setup
buttons = []
for button_pin in (SW1, SW2, SW3, SW4, SW5):
    pin = digitalio.DigitalInOut(button_pin)
    pin.switch_to_input(digitalio.Pull.UP)
    buttons.append(pin)

while True:
    position = encoder.position
    if position != last_position:
        print("Position: {}".format(position))
        if position < last_position:
            color_index -= 1
        else:
            color_index += 1
        last_position = position

        r,g,b = feathers3.rgb_color_wheel( color_index )
        pixel[0] = ( r, g, b, 0.5)
        if color_index == 255:
            color_index = 0
            feathers3.led_blink()
        elif color_index == 0:
            color_index = 254
            feathers3.led_blink()

    if not buttons[0].value:
        print("Center button!")

    if not buttons[1].value:
        print("Up button!")

    if not buttons[2].value:
        print("Left button!")

    if not buttons[3].value:
        print("Down button!")

    if not buttons[4].value:
        print("Right button!")

    time.sleep(0.01)

