from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Mail',         # Application name (muss zu APP_NAME_MAP in code.py passen)
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'New Mail', [Keycode.COMMAND, Keycode.N]),
        (0xFFFFFF, 'Reply', [Keycode.COMMAND, Keycode.R]),
        (0xFFFFFF, 'Reply All', [Keycode.COMMAND, Keycode.SHIFT, Keycode.R]),
        # 2nd row ----------
        (0xFFFFFF, 'Forward', [Keycode.COMMAND, Keycode.SHIFT, Keycode.F]),
        (0xFFFFFF, 'Send', [Keycode.COMMAND, Keycode.SHIFT, Keycode.D]),
        (0xFFFFFF, 'Archive', [Keycode.COMMAND, Keycode.SHIFT, Keycode.A]),
        # 3rd row ----------
        (0xFFFFFF, 'Delete', [Keycode.COMMAND, Keycode.BACKSPACE]),
        (0xFFFFFF, 'Search', [Keycode.COMMAND, Keycode.OPTION, Keycode.F]),
        (0xFFFFFF, 'Flag', [Keycode.COMMAND, Keycode.SHIFT, Keycode.L]),
        # 4th row ----------
        (0xFFFFFF, 'Get Mail', [Keycode.SHIFT, Keycode.COMMAND, Keycode.N]),
        (0xFFFFFF, 'Junk', [Keycode.COMMAND, Keycode.J]),
        (0xFFFFFF, 'Next', [Keycode.COMMAND, Keycode.RIGHT_BRACKET]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, Keycode.N])
    ]
}
