
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-thermistor/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/thermistor/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Thermistor/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_Thermistor/actions/
    :alt: Build Status

Thermistors are resistors that predictably change resistance with temperature.
This driver uses an analog reading and math to determine the temperature. They
are commonly used as a low cost way to measure temperature.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-thermistor/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-thermistor

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-thermistor

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-thermistor

Usage Example
=============

The hardest part of using the driver is its initialization. Here is an example
for the thermistor on the Circuit Playground and Circuit Playground Express. Its
a 10k series resistor, 10k nominal resistance, 25 celsius nominal temperature and
3950 B coefficient.

.. code-block : python

    import adafruit_thermistor
    import board
    thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)
    print(thermistor.temperature)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_thermistor/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
