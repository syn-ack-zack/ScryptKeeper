# SPDX-FileCopyrightText: 2021 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

from adafruit_simplemath import map_range


def test_map_range():
    assert map_range(1, 0, 10, 0, 100) == 10.0
    assert map_range(-1, 0, 10, 0, 100) == 0
    assert map_range(11, 0, 10, 0, 100) == 100
    assert map_range(5, 0, 10, 0, 5) == 2.5
    assert map_range(1, 10, 0, 0, 5) == 4.5
    assert map_range(1, 0, 10, 10, 0) == 9.0
    assert map_range(10, 1, 10, 1, 20) == 20.0
    # Tests for out-of-range descending output order
    assert map_range(11, 1, 10, 20, 1) == 1.0
    assert map_range(-1, 1, 10, 20, 1) == 20.0
