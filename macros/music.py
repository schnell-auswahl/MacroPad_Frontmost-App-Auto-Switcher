from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Musik',        # Application name; macOS liefert die lokalisierte App-Bezeichnung
    'macros': [            # List of button macros...
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0xFFFFFF, 'Prev', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0xFFFFFF, 'Next', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # 2nd row ----------
        (0xFFFFFF, 'Vol -', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0xFFFFFF, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0xFFFFFF, 'Vol +', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 3rd row ----------
        (0xFFFFFF, 'Shuffle', [Keycode.COMMAND, Keycode.S]),
        (0xFFFFFF, 'Repeat', [Keycode.COMMAND, Keycode.R]),
        (0xFFFFFF, 'Love', [Keycode.COMMAND, Keycode.L]),
        # 4th row ----------
        (0xFFFFFF, 'Search', [Keycode.COMMAND, Keycode.F]),
        (0xFFFFFF, 'Mini Player', [Keycode.COMMAND, Keycode.OPTION, Keycode.M]),
        (0xFFFFFF, 'New Playlist', [Keycode.COMMAND, Keycode.N]),
        # Encoder button ---
        (0xFFFFFF, '', [[ConsumerControlCode.PLAY_PAUSE]])
    ]
}
