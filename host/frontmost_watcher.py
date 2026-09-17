#!/usr/bin/env python3
"""Sends the macOS frontmost-app name to the MacroPad over its USB data serial port.

Finds the correct port automatically (by vendor ID + heartbeat handshake), so it
keeps working no matter which USB port/hub the MacroPad is plugged into.

Requires: pyserial, pyobjc-framework-Cocoa
    pip install pyserial pyobjc-framework-Cocoa
"""

import time
import serial
from serial.tools import list_ports
from AppKit import NSWorkspace

ADAFRUIT_VID = 0x239A
HANDSHAKE = "MACROPAD"  # must match code.py's heartbeat on the MacroPad
BAUD = 9600
POLL_INTERVAL = 0.3
IDENTIFY_TIMEOUT = 2.5  # > HEARTBEAT_INTERVAL in code.py, so we don't miss a beat
SCAN_RETRY_DELAY = 3


def get_frontmost_app_name():
    app = NSWorkspace.sharedWorkspace().frontmostApplication()
    return app.localizedName() if app else ""


def candidate_ports():
    return [p.device for p in list_ports.comports() if p.vid == ADAFRUIT_VID]


def find_data_port():
    """Probe every Adafruit CDC port and return the one sending our heartbeat."""
    for device in candidate_ports():
        try:
            with serial.Serial(device, BAUD, timeout=IDENTIFY_TIMEOUT) as probe:
                deadline = time.time() + IDENTIFY_TIMEOUT
                while time.time() < deadline:
                    line = probe.readline().decode("utf-8", "ignore").strip()
                    if line == HANDSHAKE:
                        return device
        except serial.SerialException:
            continue
    return None


def run():
    while True:
        device = find_data_port()
        if device is None:
            print("MacroPad not found, retrying...", flush=True)
            time.sleep(SCAN_RETRY_DELAY)
            continue
        print("connected to", device, flush=True)
        try:
            with serial.Serial(device, BAUD, timeout=1) as ser:
                last_name = None
                while True:
                    name = get_frontmost_app_name()
                    if name and name != last_name:
                        ser.write((name + "\n").encode("utf-8"))
                        last_name = name
                    time.sleep(POLL_INTERVAL)
        except serial.SerialException as e:
            print("serial error:", e, flush=True)
            time.sleep(SCAN_RETRY_DELAY)  # MacroPad unplugged, rescan later


if __name__ == "__main__":
    run()
