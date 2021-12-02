# SPDX-FileCopyrightText: 2021 James Carr
#
# SPDX-License-Identifier: Unlicense

from adafruit_simplemath import map_unconstrained_range


def test_map_unconstrained_range():
    assert map_unconstrained_range(-40, 32, 212, 0, 100) == -40.0
    assert map_unconstrained_range(50, 32, 212, 0, 100) == 10.0
    assert map_unconstrained_range(392, 32, 212, 0, 100) == 200.0
