from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Numbers',      # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Bold', [Keycode.COMMAND, Keycode.B]),
        (0xFFFFFF, 'Sum', [Keycode.SHIFT, '=']),
        (0xFFFFFF, 'Fill Down', [Keycode.COMMAND, Keycode.D]),
        # 2nd row ----------
        (0xFFFFFF, 'New Row', [Keycode.COMMAND, Keycode.RETURN]),
        (0xFFFFFF, 'New Col', [Keycode.OPTION, Keycode.RETURN]),
        (0xFFFFFF, 'Delete Row', [Keycode.COMMAND, Keycode.BACKSPACE]),
        # 3rd row ----------
        (0xFFFFFF, 'Freeze', [Keycode.COMMAND, Keycode.OPTION, Keycode.NINE]),
        (0xFFFFFF, 'Filter', [Keycode.COMMAND, Keycode.OPTION, Keycode.F]),
        (0xFFFFFF, 'Sort', [Keycode.COMMAND, Keycode.OPTION, Keycode.S]),
        # 4th row ----------
        (0xFFFFFF, 'Format $', [Keycode.COMMAND, Keycode.OPTION, Keycode.FOUR]),
        (0xFFFFFF, 'Save', [Keycode.COMMAND, Keycode.S]),
        (0xFFFFFF, 'Function', [Keycode.EQUALS]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, Keycode.S])
    ]
}
