from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Obsidian',    # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'New Note', [Keycode.COMMAND, Keycode.N]),
        (0xFFFFFF, 'Quick Switch', [Keycode.COMMAND, Keycode.O]),
        (0xFFFFFF, 'Command Pal', [Keycode.COMMAND, Keycode.P]),
        # 2nd row ----------
        (0xFFFFFF, 'Bold', [Keycode.COMMAND, Keycode.B]),
        (0xFFFFFF, 'Italic', [Keycode.COMMAND, Keycode.I]),
        (0xFFFFFF, 'Link', [Keycode.COMMAND, Keycode.K]),
        # 3rd row ----------
        (0xFFFFFF, 'Toggle Edit', [Keycode.COMMAND, Keycode.E]),
        (0xFFFFFF, 'Search All', [Keycode.COMMAND, Keycode.SHIFT, Keycode.F]),
        (0xFFFFFF, 'Graph View', [Keycode.COMMAND, Keycode.G]),
        # 4th row ----------
        (0xFFFFFF, '< Back', [Keycode.COMMAND, '[']),
        (0xFFFFFF, 'Fwd >', [Keycode.COMMAND, ']']),
        (0xFFFFFF, 'Settings', [Keycode.COMMAND, ',']),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, Keycode.N])
    ]
}
