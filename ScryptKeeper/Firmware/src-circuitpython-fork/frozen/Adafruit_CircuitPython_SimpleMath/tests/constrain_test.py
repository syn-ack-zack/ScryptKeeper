# SPDX-FileCopyrightText: 2021 Dan Halbert for Adafruit Industries
# SPDX-FileCopyrightText: 2021 James Carr
#
# SPDX-License-Identifier: Unlicense

from adafruit_simplemath import constrain


def test_constrain():
    assert constrain(1, 1, 10) == 1
    assert constrain(10, 1, 10) == 10
    assert constrain(0, 1, 10) == 1
    assert constrain(11, 1, 10) == 10

    # Check out_min > out_max
    assert constrain(5, 10, 0) == 5
    assert constrain(-5, 10, 0) == 0
    assert constrain(15, 10, 0) == 10
