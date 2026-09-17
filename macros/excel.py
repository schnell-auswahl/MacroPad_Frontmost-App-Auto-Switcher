from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Microsoft Excel',  # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Bold', [Keycode.COMMAND, Keycode.B]),
        (0xFFFFFF, 'AutoSum', [Keycode.SHIFT, '=']),
        (0xFFFFFF, 'Fill Down', [Keycode.COMMAND, Keycode.D]),
        # 2nd row ----------
        (0xFFFFFF, 'New Row', [Keycode.CONTROL, Keycode.SHIFT, '=']),
        (0xFFFFFF, 'Delete Row', [Keycode.CONTROL, '-']),
        (0xFFFFFF, 'Undo', [Keycode.COMMAND, Keycode.Z]),
        # 3rd row ----------
        (0xFFFFFF, 'Filter', [Keycode.COMMAND, Keycode.SHIFT, Keycode.L]),
        (0xFFFFFF, 'Freeze', [Keycode.OPTION, Keycode.W, Keycode.F]),
        (0xFFFFFF, 'Format Cells', [Keycode.COMMAND, Keycode.ONE]),
        # 4th row ----------
        (0xFFFFFF, 'Format $', [Keycode.COMMAND, Keycode.SHIFT, Keycode.FOUR]),
        (0xFFFFFF, 'Save', [Keycode.COMMAND, Keycode.S]),
        (0xFFFFFF, 'New Sheet', [Keycode.SHIFT, Keycode.F11]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, Keycode.S])
    ]
}
