
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-focaltouch/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/focaltouch/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_FocalTouch/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_FocalTouch/actions/
    :alt: Build Status

CircuitPython driver for common low-cost FocalTech capacitive touch chips.
Currently supports FT6206 & FT6236

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-focaltouch/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-focaltouch

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-focaltouch

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-focaltouch

Usage Example
=============

.. code-block:: python

	import time
	import board
	import busio
	import adafruit_focaltouch

	# Create library object (named "ft") using a Bus I2C port
	i2c = busio.I2C(board.SCL, board.SDA)

	ft = adafruit_focaltouch.Adafruit_FocalTouch(i2c, debug=False)

	while True:
	    # if the screen is being touched print the touches
	    if ft.touched:
		print(ft.touches)
	    else:
		print('no touch')

	    time.sleep(.15)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_FocalTouch/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
