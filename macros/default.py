# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, '1', ['1']),
        (0xFFFFFF, '2', ['2']),
        (0xFFFFFF, '3', ['3']),
        # 2nd row ----------
        (0xFFFFFF, '4', ['4']),
        (0xFFFFFF, '5', ['5']),
        (0xFFFFFF, '6', ['6']),
        # 3rd row ----------
        (0xFFFFFF, '7', ['7']),
        (0xFFFFFF, '8', ['8']),
        (0xFFFFFF, '9', ['9']),
        # 4th row ----------
        (0xFFFFFF, '*', ['*']),
        (0xFFFFFF, '-', ['-']),
        (0xFFFFFF, '0', ['0']),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.BACKSPACE])
    ]
}
