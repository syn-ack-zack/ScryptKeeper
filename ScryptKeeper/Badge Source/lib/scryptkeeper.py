"""

The ScryptKeeper
Hackers Teaching Hackers 2021
@syn-ack-zack

"""
import time
import gc
gc.collect()

import board
import neopixel
from usb_cdc import data as usbdata
from busio import UART as busiouart
from digitalio import DigitalInOut, Direction, Pull
import touchio
import supervisor 
from usb_hid import devices
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_ducky import Ducky
import binary_challenge
from spookymorse import spookymorse
import bling

def writeserial(str):
    usbdata.flush()
    usbdata.write(bytes(str,'utf-8'))

def serialinput():
    usbdata.write(bytes("\r\n$> ",'utf-8'))
    usbdata.timeout = 10
    s = usbdata.readline()
    usbdata.write(bytes(s))
    return s.decode('utf-8')

state = 0
pixel_pin = board.NEOPIXEL
num_pixels = 4
ORDER = neopixel.GRB

cybernetic = neopixel.NeoPixel(
    pixel_pin, 1, brightness=0.7, auto_write=True, pixel_order=ORDER
)
pixels = neopixel.NeoPixel(
    board.MOSI, num_pixels, brightness=1.0, auto_write=True, pixel_order=ORDER
)

gc.collect()
leye = DigitalInOut(board.SCK)
leye.direction = Direction.OUTPUT

def writestate(num):
    global state
    try:
        with open("state", "w") as fp:
                fp.write(bytes(str(num),'ascii'))
                fp.close()
                state = int(num)
                return True
    except OSError as e:
        return False

def readstate():
    global state
    try:
        with open("state", "r") as fp:
                state = int(fp.read())
                fp.close()
                return True
    except OSError as e:
        return False

def bootgate():
    global state
    nosetouch = touchio.TouchIn(board.A0)
    mouthtouch = touchio.TouchIn(board.A2)

    time.sleep(1)
    cybernetic.fill(bling.RED)
    cybernetic.show()
    pixels.fill(bling.RED)
    pixels.show()
    time.sleep(1)
    while int(state) < 2:
        bling.color_chase(pixels,bling.ORANGE,0.1)
        bling.pulsestatus(pixels,state)
        writeserial("\r\n[*] Scrypt Locked! Hold Nose to begin activation sequence...\r\n")
        if nosetouch.value:
            writeserial("\r\n[+] Sequence Activated! The ScryptKeeper is COUNTING on your demise...\r\n")
            if binary_challenge.initiate(pixels):
                writestate(2) # LEVEL 2
                state = 2
                writeserial("\r\n[+] Accepted!\r\n")
                writeserial("\r\n[+] HTH{B1N4RYFLU3NT}")
            else:
                writeserial("\r\n[-] Denied!\r\n")

    while int(state) < 3:
        bling.color_chase(pixels,bling.ORANGE,0.07)
        bling.pulsestatus(pixels,state)
        writeserial("\r\n[!] 42706d20416b7a677862536d6d786d7a20716120656d697a71766f2069206c71616f6371616d2e204e71766c2062706d20446d766c777a20514c2069766c20587a776c636b6220514c202d205042507b44514c3a58514c7d \r\n---\r\n[*] Hold Nose to enter flag\r\n")
        if nosetouch.value:
            writeserial("Response:\r\n")
            serial = serialinput().rstrip()
            if serial == "HTH{045E:001B}" or serial == "HTH{045e:001b}":
                writestate(3) #LEVEL 3
                state = 3
                writeserial("\r\n[+] Response OK!\r\n")
            else:
                writeserial("\r\n[-] Denied!\r\n")
    m = Mouse(devices)
    while int(state) < 4:
        bling.color_chase(pixels,bling.ORANGE,0.04)
        writeserial("\r\n[!] The ScryptKeeper is dying to tell you a secret...Hold his Mouth to let him speak...\r\n[*] Hold Nose to enter flag\r\n")
        bling.pulsestatus(pixels,state)
        if nosetouch.value:
            serial = serialinput().rstrip()
            if serial == "HTH{S3ANC3SIGNAL}" or serial == "HTH(S3ANC3SIGNAL)":
                writestate(4) #LEVEL 4
                state = 4
                writeserial("\r\n[+] Response OK!\r\n")
            else:
                writeserial("\r\n[-] Denied!\r\n")
        if mouthtouch.value:
            pixels.fill(bling.CYAN)
            pixels.show()
            spookymorse(m)
    uart = busiouart(board.TX, board.RX, baudrate=115200)
    s = bytearray("HTH{3n73rTh3SCRYPT}\r\n".encode())
    while int(state) == 4:
        bling.color_chase(pixels,bling.ORANGE,0.02)
        bling.pulsestatus(pixels,state)
        uart.write(s)
        writeserial("\r\n[*] You ART not going to believe where the ScryptKeeper hid this one...\r\n[*] Transmitting!\r\n[*] Hold nose to enter flag\r\n")
        if nosetouch.value:
            serial = serialinput()
            if serial.rstrip() == "HTH{3n73rTh3SCRYPT}":
                    writestate(5) #LEVEL 5
                    state = 5
                    writeserial("\r\n[+] Response OK!\r\n")
                    writeserial("\r\n[+] Scrypt Unlocked! Reboot Badge to unlock filesystem\r\n")
            else:
                writeserial("\r\n[-] Denied! \r\n")
    mouthtouch.deinit()
    nosetouch.deinit()
 
def main_menu():
    mouthtouch = touchio.TouchIn(board.A2)
    cortextouch = touchio.TouchIn(board.A1)
    nosetouch = touchio.TouchIn(board.A0)
    while True:
        cybernetic.fill(bling.GREEN)
        cybernetic.show()
        bling.color_chase(pixels,bling.PURPLE,0.1)
        gc.collect()
        writeserial("\r\n\r\nTouch Menu\r\n----------\r\nFrontal Lobe: Bling\r\nNose: Mouse Jiggler\r\nMouth: Launch Ducky Payload\r\n")
        if cortextouch.value:
            writeserial("\r\n[*] Press Nose to Cycle Bling. Press Mouth to Return.\r\n")
            bling.control(pixels,cybernetic,nosetouch,mouthtouch)
            gc.collect()
            time.sleep(0.9) #Pause so button press doesn't register immediately on return
        if nosetouch.value and supervisor.runtime.usb_connected:
            m = Mouse(devices)  #do not initialize hid objects unless we have usb power - avoids crash
            keyboard = Keyboard(devices)
            keyboard_layout = KeyboardLayoutUS(keyboard)
            while True:
                bling.jiggle(pixels,cybernetic)
                m.move(-5,0,0)
                m.move(5,0,0)
                writeserial("\r\n[!] Jiggle!")
                if nosetouch.value or not supervisor.runtime.usb_connected:
                    gc.collect()
                    break
        if mouthtouch.value and supervisor.runtime.usb_connected:
            m = Mouse(devices)  #do not initialize hid objects unless we have usb power - avoids crash
            keyboard = Keyboard(devices)
            keyboard_layout = KeyboardLayoutUS(keyboard)
            bling.color_chase(pixels,bling.YELLOW,0.1)
            duck = Ducky("duckyscript.txt", keyboard, keyboard_layout)
            result = True
            writeserial("\r\n[+] Executing payload!\r\n")
            while result is not False:
                pixels.fill(bling.ORANGE)
                pixels.show()
                try:
                    result = duck.loop()
                except:
                    writeserial("\r\n[-] Ducky payload failed!\r\n")
                pixels.fill(bling.GREEN)
                pixels.show()
            gc.collect()

def main():
    readstate()
    gc.collect()
    leye.value = True
    writeserial("\r\n[*] Initializing ScryptKeeper boot sequence...\r\n")
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    cybernetic.fill(bling.GREEN)
    cybernetic.show()
    writeserial("\r\n[*] ScryptKeeper OS v6.66\r\n[*] Checking State...\r\n")
    if int(state) < 5:
        writeserial("\r\n[!] Not so fast Scrypt Kiddies! \r\n\r\n[-] Filesystem Locked!\r\n[-] REPL Disabled!\r\n[-] USB Mass Storage Disabled!\r\n\r\n[!] Initiating Challenge Protocol...\r\n")
        bootgate()
        gc.collect()
    else:
        writeserial("\r\n[+] OK! Scrypt Access Granted!\r\n")
    main_menu()