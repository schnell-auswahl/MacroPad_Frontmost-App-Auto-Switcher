from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Kalender',    # Application name; macOS liefert die lokalisierte App-Bezeichnung
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'New Event', [Keycode.COMMAND, Keycode.N]),
        (0xFFFFFF, 'Today', [Keycode.COMMAND, Keycode.T]),
        (0xFFFFFF, 'Find', [Keycode.COMMAND, Keycode.F]),
        # 2nd row ----------
        (0xFFFFFF, 'Day', [Keycode.COMMAND, Keycode.ONE]),
        (0xFFFFFF, 'Week', [Keycode.COMMAND, Keycode.TWO]),
        (0xFFFFFF, 'Month', [Keycode.COMMAND, Keycode.THREE]),
        # 3rd row ----------
        (0xFFFFFF, '< Prev', [Keycode.COMMAND, Keycode.LEFT_ARROW]),
        (0xFFFFFF, 'Year', [Keycode.COMMAND, Keycode.FOUR]),
        (0xFFFFFF, 'Next >', [Keycode.COMMAND, Keycode.RIGHT_ARROW]),
        # 4th row ----------
        (0xFFFFFF, 'Refresh', [Keycode.COMMAND, Keycode.R]),
        (0xFFFFFF, 'Get Info', [Keycode.COMMAND, Keycode.I]),
        (0xFFFFFF, 'Delete', [Keycode.COMMAND, Keycode.BACKSPACE]),
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.COMMAND, Keycode.N])
    ]
}
