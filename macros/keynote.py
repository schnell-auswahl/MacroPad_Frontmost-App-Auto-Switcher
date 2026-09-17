from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Keynote',      # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Play', [Keycode.COMMAND, Keycode.OPTION, Keycode.P]),
        (0xFFFFFF, 'New Slide', [Keycode.COMMAND, Keycode.SHIFT, Keycode.N]),
        (0xFFFFFF, 'Skip', [Keycode.COMMAND, Keycode.SHIFT, Keycode.RIGHT_ARROW]),
        # 2nd row ----------
        (0xFFFFFF, 'Duplicate', [Keycode.COMMAND, Keycode.D]),
        (0xFFFFFF, 'Group', [Keycode.COMMAND, Keycode.OPTION, Keycode.G]),
        (0xFFFFFF, 'Ungroup', [Keycode.COMMAND, Keycode.OPTION, Keycode.SHIFT, Keycode.G]),
        # 3rd row ----------
        (0xFFFFFF, 'Align', [Keycode.COMMAND, Keycode.K]),
        (0xFFFFFF, 'Bring Front', [Keycode.COMMAND, Keycode.SHIFT, Keycode.F]),
        (0xFFFFFF, 'Send Back', [Keycode.COMMAND, Keycode.SHIFT, Keycode.B]),
        # 4th row ----------
        (0xFFFFFF, 'Zoom In', [Keycode.COMMAND, '=']),
        (0xFFFFFF, 'Zoom Out', [Keycode.COMMAND, '-']),
        (0xFFFFFF, 'Save', [Keycode.COMMAND, Keycode.S]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, Keycode.OPTION, Keycode.P])
    ]
}
