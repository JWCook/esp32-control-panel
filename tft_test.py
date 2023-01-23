import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7789 import ST7789

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
TFT_CS = board.IO18
TFT_DC = board.IO12
RST = board.IO14


display_bus = displayio.FourWire(spi, command=TFT_DC, chip_select=TFT_CS, reset=RST)

display = ST7789(display_bus, width=280, height=240, rowstart=20, rotation=90)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(280, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(240, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xFF006C
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=2, x=35, y=35)
text = "Hello, World!\n\n\n\nBOTTOM TEXT"
text_area = label.Label(terminalio.FONT, text=text, color=0x00FFC5)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

while True:
    pass
