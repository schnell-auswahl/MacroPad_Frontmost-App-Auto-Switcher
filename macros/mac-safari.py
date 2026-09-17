# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Mac Safari', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, '< Back', [Keycode.COMMAND, '[']),
        (0xFFFFFF, 'Fwd >', [Keycode.COMMAND, ']']),
        (0xFFFFFF, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0xFFFFFF, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0xFFFFFF, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0xFFFFFF, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0xFFFFFF, 'Reload', [Keycode.COMMAND, 'r']),
        (0xFFFFFF, 'Home', [Keycode.COMMAND, 'H']),
        (0xFFFFFF, 'Private', [Keycode.COMMAND, 'N']),
        # 4th row ----------
        (0xFFFFFF, 'Ada', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                           'www.adafruit.com\n']),   # Adafruit in new window
        (0xFFFFFF, 'Digi', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0xFFFFFF, 'Hacks', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                             'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
