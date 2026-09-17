# SPDX-License-Identifier: MIT

# Second USB-CDC data port, used for host <-> MacroPad communication (independent of the REPL console)
import usb_cdc

usb_cdc.enable(console=True, data=True)
