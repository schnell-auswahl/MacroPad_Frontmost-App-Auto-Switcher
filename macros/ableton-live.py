from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Ableton Live',  # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Play', [' ']),
        (0xFFFFFF, 'Record', [Keycode.F9]),
        (0xFFFFFF, 'Stop', [Keycode.KEYPAD_ZERO]),
        # 2nd row ----------
        (0xFFFFFF, 'New Scene', [Keycode.COMMAND, Keycode.I]),
        (0xFFFFFF, 'Loop', [Keycode.COMMAND, Keycode.L]),
        (0xFFFFFF, 'Undo', [Keycode.COMMAND, Keycode.Z]),
        # 3rd row ----------
        (0xFFFFFF, 'Warp', [Keycode.COMMAND, Keycode.W]),
        (0xFFFFFF, 'Quantize', [Keycode.COMMAND, Keycode.U]),
        (0xFFFFFF, 'Group', [Keycode.COMMAND, Keycode.G]),
        # 4th row ----------
        (0xFFFFFF, 'Zoom Fit', [Keycode.COMMAND, Keycode.OPTION, Keycode.O]),
        (0xFFFFFF, 'Save', [Keycode.COMMAND, Keycode.S]),
        (0xFFFFFF, 'Tap Tempo', [Keycode.F1]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.SPACE])
    ]
}
