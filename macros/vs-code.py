

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'VS Code',     # Application name
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'BM up', [Keycode.COMMAND, Keycode.OPTION, Keycode.J]), #
        (0xFFFFFF, 'BM down', [Keycode.COMMAND, Keycode.OPTION, Keycode.L]), # Einfacher Keycode zum Testen
        (0xFFFFFF, 'BM ', [Keycode.COMMAND, Keycode.OPTION, Keycode.K]),
        # 2nd row ----------
        (0xFFFFFF, 'Ä', ['ä']), # Einfacher Keycode zum Testen
        (0xFFFFFF, 'Ö', ['ö']), # Einfacher Keycode zum Testen
        (0xFFFFFF, 'Ü', ['ü']), # Einfacher Keycode zum Testen  # 3rd row ----------
     (0xFFFFFF, 'Edtr <', [Keycode.CONTROL, '-']), #
           (0xFFFFFF, 'Edtr >', [Keycode.CONTROL,Keycode.SHIFT, '-']), #
        (0xFFFFFF, '[', ['[']), # Symbol: [
        # 4th row ----------
        (0xFFFFFF, ']', [']']), # Symbol: ]
        (0xFFFFFF, '{', ['{']), # Symbol: {
        (0xFFFFFF, '}', ['}']), # Symbol: }
        # Encoder button ---
        (0xFFFFFF, '', [Keycode.G]) # Einfacher Keycode zum Testen
    ]
