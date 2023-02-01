import board
import displayio
import terminalio
from adafruit_bitmap_font.bitmap_font import load_font
from adafruit_display_text.label import Label
from adafruit_st7789 import ST7789

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
TFT_CS = board.IO18
TFT_DC = board.IO12
RST = board.IO14

FONT_JBM = load_font('fonts/JetBrainsMono_12.pcf')
FONT_FA = load_font('fonts/forkawesome-12.pcf')

display_bus = displayio.FourWire(spi, command=TFT_DC, chip_select=TFT_CS, reset=RST)
display = ST7789(display_bus, width=280, height=240, rowstart=20, rotation=90)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(280, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF006C

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
# inner_bitmap = displayio.Bitmap(280, 220, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0x00FF00
# inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=0, y=12)
# splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=2, x=20, y=15)
text = f'{chr(0xF322)} ' * 8
text = f'{text}\n' * 6

# text_area = Label(terminalio.FONT, text=text, color=0x00FFC5)
# text_area = Label(FONT_FA, text=text, color=0x00FFC5)

ICON_PLAY = chr(0xF04B)
ICON_PAUSE = chr(0xF04C)
ICON_FAST_FORWARD = chr(0xF04E)
ICON_REWIND = chr(0xF04A)
ICON_STOP = chr(0xF04D)
ICON_VOLUME_UP = chr(0xF028)
ICON_VOLUME_DOWN = chr(0xF027)
ICON_VOLUME_MUTE = chr(0xF026)

ICON_SAVE = chr(0xF0C7)
ICON_SEARCH = chr(0xF002)
ICON_CUT = chr(0xF0C4)
ICON_COPY = chr(0xF0C5)
ICON_PASTE = chr(0xF0EA)
ICON_UNDO = chr(0xF0E2)
ICON_REDO = chr(0xF01E)
ICON_TRASH = chr(0xF1F8)
ICON_DELETE = chr(0xF56D)

ICON_IMAGE = chr(0xF03E)
ICON_UPLOAD = chr(0xF093)
ICON_DOWNLOAD = chr(0xF019)
ICON_POWER = chr(0xF011)
ICON_BATTERY = chr(0xF578)
ICON_BATTERY_50 = chr(0xF57D)
ICON_BATTERY_EMPTY = chr(0xF579)
ICON_BATTERY_CHARGE = chr(0xF584)

ICON_ARROW_UP = chr(0xF062)
ICON_ARROW_DOWN = chr(0xF063)
ICON_ARROW_LEFT = chr(0xF060)
ICON_ARROW_RIGHT = chr(0xF061)
ICON_CHECK = chr(0xF00C)
ICON_CROSS = chr(0xF00D)
ICON_STAR = chr(0xF005)

ICON_GPS = chr(0xE248)
ICON_WIFI = chr(0xF1EB)
ICON_BLUETOOTH = chr(0xF294)
ICON_BELL = chr(0xF0F3)
ICON_PYTHON = chr(0xE235)


icons = [
    [
        ICON_PLAY,
        ICON_PAUSE,
        ICON_REWIND,
        ICON_FAST_FORWARD,
        ICON_STOP,
        ICON_VOLUME_UP,
        ICON_VOLUME_DOWN,
        ICON_VOLUME_MUTE,
    ],
    [
        ICON_SAVE,
        ICON_SEARCH,
        ICON_CUT,
        ICON_COPY,
        ICON_PASTE,
        ICON_UNDO,
        ICON_REDO,
        ICON_TRASH,
        ICON_DELETE,
    ],
    [
        ICON_IMAGE,
        ICON_UPLOAD,
        ICON_DOWNLOAD,
        ICON_POWER,
        ICON_BATTERY,
        ICON_BATTERY_50,
        ICON_BATTERY_EMPTY,
        ICON_BATTERY_CHARGE,
    ],
    [
        ICON_ARROW_UP,
        ICON_ARROW_DOWN,
        ICON_ARROW_LEFT,
        ICON_ARROW_RIGHT,
        ICON_CHECK,
        ICON_CROSS,
        ICON_STAR,
    ],
    [
        ICON_GPS,
        ICON_WIFI,
        ICON_BLUETOOTH,
        ICON_BELL,
        ICON_PYTHON,
    ],
    [
        ICON_PYTHON,
    ],
]

text_area = Label(
    FONT_JBM, text='\n'.join([' '.join(i) for i in icons]), color=0x00FFC5
)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

while True:
    pass
