# SPDX-FileCopyrightText: 2017 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_hid.mouse.Mouse`
====================================================

* Author(s): Dan Halbert
"""
import time

from . import find_device


class Mouse:
    """Send USB HID mouse reports."""

    LEFT_BUTTON = 1
    """Left mouse button."""
    RIGHT_BUTTON = 2
    """Right mouse button."""
    MIDDLE_BUTTON = 4
    """Middle mouse button."""

    def __init__(self, devices):
        self._mouse_device = find_device(devices, usage_page=0x1, usage=0x02)

        # Reuse this bytearray to send mouse reports.
        # report[0] buttons pressed (LEFT, MIDDLE, RIGHT)
        # report[1] x movement
        # report[2] y movement
        # report[3] wheel movement
        self.report = bytearray(4)

        # Do a no-op to test if HID device is ready.
        # If not, wait a bit and try once more.
        try:
            self._send_no_move()
        except OSError:
            time.sleep(1)
            self._send_no_move()

    def press(self, buttons):
        self.report[0] |= buttons
        self._send_no_move()

    def release(self, buttons):
        self.report[0] &= ~buttons
        self._send_no_move()

    def release_all(self):
        """Release all the mouse buttons."""
        self.report[0] = 0
        self._send_no_move()

    def click(self, buttons):
        self.press(buttons)
        self.release(buttons)

    def move(self, x=0, y=0, wheel=0):
        # Send multiple reports if necessary to move or scroll requested amounts.
        while x != 0 or y != 0 or wheel != 0:
            partial_x = self._limit(x)
            partial_y = self._limit(y)
            partial_wheel = self._limit(wheel)
            self.report[1] = partial_x & 0xFF
            self.report[2] = partial_y & 0xFF
            self.report[3] = partial_wheel & 0xFF
            self._mouse_device.send_report(self.report)
            x -= partial_x
            y -= partial_y
            wheel -= partial_wheel

    def _send_no_move(self):
        """Send a button-only report."""
        self.report[1] = 0
        self.report[2] = 0
        self.report[3] = 0
        self._mouse_device.send_report(self.report)

    @staticmethod
    def _limit(dist):
        return min(127, max(-127, dist))
