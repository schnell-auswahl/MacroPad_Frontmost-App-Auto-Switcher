from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Pages',        # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Bold', [Keycode.COMMAND, Keycode.B]),
        (0xFFFFFF, 'Italic', [Keycode.COMMAND, Keycode.I]),
        (0xFFFFFF, 'Underline', [Keycode.COMMAND, Keycode.U]),
        # 2nd row ----------
        (0xFFFFFF, 'Save', [Keycode.COMMAND, Keycode.S]),
        (0xFFFFFF, 'Find', [Keycode.COMMAND, Keycode.F]),
        (0xFFFFFF, 'Comment', [Keycode.COMMAND, Keycode.OPTION, Keycode.K]),
        # 3rd row ----------
        (0xFFFFFF, 'Bullets', [Keycode.COMMAND, Keycode.SHIFT, Keycode.L]),
        (0xFFFFFF, 'Link', [Keycode.COMMAND, Keycode.K]),
        (0xFFFFFF, 'Word Count', [Keycode.COMMAND, Keycode.SHIFT, Keycode.OPTION, Keycode.W]),
        # 4th row ----------
        (0xFFFFFF, 'Zoom In', [Keycode.COMMAND, '=']),
        (0xFFFFFF, 'Zoom Out', [Keycode.COMMAND, '-']),
        (0xFFFFFF, 'New Page', [Keycode.COMMAND, Keycode.RETURN]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, Keycode.S])
    ]
}
