# The ScryptKeeper

## 2021 Hackers Teaching Hackers Badge

<img src="https://user-images.githubusercontent.com/2582445/144517951-0769373b-a938-4fa1-9a49-e73bf93c29ff.jpg" width="600" height="700">

The ScryptKeeper is a HID device programmable and powered by CircuitPython.
The USB-C port provides two serial streams, one of which is a Python REPL, 
allowing for interactive scripting live on the the device. As a HID platform, 
full keyboard and mouse emulation is possible and programmable by you.

The initial configuration of the badge is in a locked state restricting most features. This is visually indicated by observing one or more of the brain LEDs periodically pulsing red. Each LED represents a challenge gate, solving all four challenges allows access to increased functionality and the original CircuitPython features. When plugging in the unlocked badge you will now see two USB devices, this new one offers access to the Python REPL which allows you to interactively execute code on the badge. 

Visit here for a walkthrough of the challenges: https://github.com/syn-ack-zack/ScryptKeeper/wiki/Badge-Walkthrough

Learn More about CircuitPython: https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython

To demonstrate the HID capabilities of this fully armed and operational ScryptKeeper, the following functionality is controlled
via capacitive touch areas on the badge. 

Bling Mode
---
- **Description**: RGB fun makes purdy lights
- **Activate Bling Mode**: Touch Front Brain
- **Next Bling Animation**: Touch Nose
- **Exit Bling Mode**: Hold Mouth

Mouse Jiggler
---
- **Description**: Uses mouse emulation to jiggle mouse 5px every 3 seconds
- **Activate Jiggler**: Touch Nose while USB is plugged in
- **Exit Jiggler**: Hold Nose

Ducky Payload
---
- **Description**: Just like a USB Rubber Ducky, perform HID attacks with the Ducky Scripting language
- **Modify**: Edit 'duckyscript.txt' to alter the launched payload
- **Launch Payload**: Touch Mouth while USB is plugged in 

