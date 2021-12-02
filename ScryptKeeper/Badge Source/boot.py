import board
import storage 
import usb_cdc
import touchio

state = 1

try:
    with open("state", "r") as fp:
            state = fp.read()
            fp.close()
except OSError as e:
    print("Failed to read file! Is File System Read Only?")

if int(state) != 5:
    storage.remount("/",False)
    storage.disable_usb_drive()
    usb_cdc.enable(console=False, data=True)
else:
    usb_cdc.enable(console=True, data=True)