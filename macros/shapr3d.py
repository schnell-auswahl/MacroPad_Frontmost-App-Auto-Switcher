from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Shapr3D',      # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Sketch', [Keycode.S]),
        (0xFFFFFF, 'Extrude', [Keycode.E]),
        (0xFFFFFF, 'Fillet', [Keycode.F]),
        # 2nd row ----------
        (0xFFFFFF, 'Move', [Keycode.M]),
        (0xFFFFFF, 'Rotate', [Keycode.R]),
        (0xFFFFFF, 'Scale', [Keycode.L]),
        # 3rd row ----------
        (0xFFFFFF, 'Undo', [Keycode.COMMAND, Keycode.Z]),
        (0xFFFFFF, 'Redo', [Keycode.COMMAND, Keycode.SHIFT, Keycode.Z]),
        (0xFFFFFF, 'Hide', [Keycode.H]),
        # 4th row ----------
        (0xFFFFFF, 'Measure', [Keycode.D]),
        (0xFFFFFF, 'Zoom Fit', [Keycode.Z]),
        (0xFFFFFF, 'Save', [Keycode.COMMAND, Keycode.S]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.S])
    ]
}
