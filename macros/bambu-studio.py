from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Bambu Studio',  # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Import', [Keycode.COMMAND, Keycode.I]),
        (0xFFFFFF, 'Export G-code', [Keycode.COMMAND, Keycode.G]),
        (0xFFFFFF, 'Slice', [Keycode.COMMAND, Keycode.R]),
        # 2nd row ----------
        (0xFFFFFF, 'Arrange', [Keycode.A]),
        (0xFFFFFF, 'Copy', [Keycode.COMMAND, Keycode.C]),
        (0xFFFFFF, 'Paste', [Keycode.COMMAND, Keycode.V]),
        # 3rd row ----------
        (0xFFFFFF, 'Delete', [Keycode.DELETE]),
        (0xFFFFFF, 'Undo', [Keycode.COMMAND, Keycode.Z]),
        (0xFFFFFF, 'Redo', [Keycode.COMMAND, Keycode.SHIFT, Keycode.Z]),
        # 4th row ----------
        (0xFFFFFF, 'Top View', [Keycode.ONE]),
        (0xFFFFFF, 'Front View', [Keycode.TWO]),
        (0xFFFFFF, 'Save Project', [Keycode.COMMAND, Keycode.S]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, Keycode.R])
    ]
}
