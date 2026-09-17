# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
A macro/hotkey program for Adafruit MACROPAD. Macro setups are stored in the
/macros folder (configurable below), load up just the ones you're likely to
use. Plug into computer's USB port, use dial to select an application macro
set, press MACROPAD keys to send key sequences and other USB protocols.

Extended with automatic profile switching based on the frontmost macOS
application (see host/frontmost_watcher.py) and an encoder button that cycles
the key backlight brightness instead of triggering a macro.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import time
import displayio
import terminalio
import usb_cdc
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'

# Maps the frontmost-app name reported by the host script to an App 'name'.
# macOS localizes some names (e.g. "Music" vs "Musik", "Calendar" vs
# "Kalender") - both variants are mapped here so it works regardless of your
# system language. To find the exact name for an app not listed here, see
# the "Finding the macOS name of an app" section in README.md.
APP_NAME_MAP = {
    'Safari': 'Mac Safari',
    'Code': 'VS Code',
    'Logic Pro': 'Logic Pro',
    'Live': 'Ableton Live',
    'Keynote': 'Keynote',
    'Pages': 'Pages',
    'Numbers': 'Numbers',
    'Microsoft Excel': 'Microsoft Excel',
    'Microsoft Word': 'Microsoft Word',
    'Mail': 'Mail',
    'Music': 'Musik',
    'Musik': 'Musik',
    'Bambu Studio': 'Bambu Studio',
    'Shapr3D': 'Shapr3D',
    'Calendar': 'Kalender',
    'Kalender': 'Kalender',
    'Obsidian': 'Obsidian',
}


# CLASSES AND FUNCTIONS ----------------

class App:
    """ Class representing a host-side application, for which we have a set
        of macro sequences. Project code was originally more complex and
        this was helpful, but maybe it's excessive now?"""
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']

    def switch(self):
        """ Activate application settings; update OLED labels and LED
            colors. """
        group[13].text = self.name   # Application name
        if self.name:
            rect.fill = 0xFFFFFF
        else: # empty app name indicates blank screen for which we dimm header
            rect.fill = 0x000000
        for i in range(12):
            if i < len(self.macros): # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
                group[i].text = ''
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()


# INITIALIZATION -----------------------

macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

# Set up displayio group with all the labels
group = displayio.Group()
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                             anchored_position=((macropad.display.width - 1) * x / 2,
                                                macropad.display.height - 1 -
                                                (3 - y) * 12),
                             anchor_point=(x / 2, 1.0)))
rect = Rect(0, 0, macropad.display.width, 13, fill=0xFFFFFF)
group.append(rect)
group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(macropad.display.width//2, 0),
                         anchor_point=(0.5, 0.0)))
macropad.display.root_group = group

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py') and not filename.startswith('._'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)

if not apps:
    group[13].text = 'NO MACRO FILES FOUND'
    macropad.display.refresh()
    while True:
        pass

def name_to_index(host_app_name):
    """ Find the apps[] index whose name matches the host's frontmost app,
        via APP_NAME_MAP or a direct name match. None if no macro page fits. """
    macro_name = APP_NAME_MAP.get(host_app_name, host_app_name)
    for i, one_app in enumerate(apps):
        if one_app.name == macro_name:
            return i
    return None


serial = usb_cdc.data  # second CDC port (enabled in boot.py) carries app names
serial_buffer = ""
current_host_app = None  # last frontmost-app name received from the host
HEARTBEAT = b"MACROPAD\n"  # lets the host identify this port, independent of USB path
HEARTBEAT_INTERVAL = 1  # seconds
last_heartbeat = time.monotonic()

# Encoder button cycles the (white) LED brightness in 4 steps, off to full,
# instead of triggering a per-app macro.
BRIGHTNESS_LEVELS = [0.0, 1 / 3, 2 / 3, 1.0]
brightness_index = len(BRIGHTNESS_LEVELS) - 1  # start at full brightness
macropad.pixels.brightness = BRIGHTNESS_LEVELS[brightness_index]

last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
last_manual_index = app_index  # fallback page when frontmost app has no macros
apps[app_index].switch()


# MAIN LOOP ----------------------------

while True:
    # Announce ourselves periodically so the host can find us on any USB port/hub.
    if serial is not None and time.monotonic() - last_heartbeat >= HEARTBEAT_INTERVAL:
        serial.write(HEARTBEAT)
        last_heartbeat = time.monotonic()

    # Read frontmost-app name from host (non-blocking) and auto-switch pages.
    if serial is not None and serial.in_waiting > 0:
        serial_buffer += serial.read(serial.in_waiting).decode("utf-8")
        while "\n" in serial_buffer:
            line, serial_buffer = serial_buffer.split("\n", 1)
            host_app = line.strip()
            if host_app and host_app != current_host_app:
                current_host_app = host_app  # new foreground app: re-evaluate
                match = name_to_index(host_app)
                new_index = match if match is not None else last_manual_index
                if new_index != app_index:
                    app_index = new_index
                    apps[app_index].switch()
                    last_position = macropad.encoder  # avoid encoder jump

    # Read encoder position. If it's changed, switch apps.
    position = macropad.encoder
    if position != last_position:
        app_index = position % len(apps)
        last_manual_index = app_index  # remember explicit user choice, stays until app changes
        apps[app_index].switch()
        last_position = position

    # Handle encoder button: cycles LED brightness (off -> full white), no macro.
    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch and not last_encoder_switch:
        brightness_index = (brightness_index + 1) % len(BRIGHTNESS_LEVELS)
        macropad.pixels.brightness = BRIGHTNESS_LEVELS[brightness_index]
        macropad.pixels.show()
    last_encoder_switch = encoder_switch

    event = macropad.keys.events.get()
    if not event or event.key_number >= len(apps[app_index].macros):
        continue  # No key events, or no corresponding macro, resume loop
    key_number = event.key_number
    pressed = event.pressed

    # If code reaches here, a key WAS pressed/released and there IS a
    # corresponding macro available for it...other situations are avoided by
    # 'continue' statements above which resume the loop.

    sequence = apps[app_index].macros[key_number][2]
    if pressed:
        # 'sequence' is an arbitrary-length list, each item is one of:
        # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
        # Negative integer: (absolute value) key released
        # Float (e.g. 0.25): delay in seconds
        # String (e.g. "Foo"): corresponding keys pressed & released
        # List []: one or more Consumer Control codes (can also do float delay)
        # Dict {}: mouse buttons/motion (might extend in future)
        macropad.pixels[key_number] = 0xFFFFFF
        macropad.pixels.show()
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.press(item)
                else:
                    macropad.keyboard.release(-item)
            elif isinstance(item, float):
                time.sleep(item)
            elif isinstance(item, str):
                macropad.keyboard_layout.write(item)
            elif isinstance(item, list):
                for code in item:
                    if isinstance(code, int):
                        macropad.consumer_control.release()
                        macropad.consumer_control.press(code)
                    if isinstance(code, float):
                        time.sleep(code)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.press(item['buttons'])
                    else:
                        macropad.mouse.release(-item['buttons'])
                macropad.mouse.move(item['x'] if 'x' in item else 0,
                                    item['y'] if 'y' in item else 0,
                                    item['wheel'] if 'wheel' in item else 0)
                if 'tone' in item:
                    if item['tone'] > 0:
                        macropad.stop_tone()
                        macropad.start_tone(item['tone'])
                    else:
                        macropad.stop_tone()
                elif 'play' in item:
                    macropad.play_file(item['play'])
    else:
        # Release any still-pressed keys, consumer codes, mouse buttons
        # Keys and mouse buttons are individually released this way (rather
        # than release_all()) because pad supports multi-key rollover, e.g.
        # could have a meta key or right-mouse held down by one macro and
        # press/release keys/buttons with others. Navigate popups, etc.
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.release(item)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.release(item['buttons'])
                elif 'tone' in item:
                    macropad.stop_tone()
        macropad.consumer_control.release()
        macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
        macropad.pixels.show()
