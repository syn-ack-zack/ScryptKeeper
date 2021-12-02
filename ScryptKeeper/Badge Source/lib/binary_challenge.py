import bling
from usb_cdc import data as usbdata

def serialinput():
    usbdata.write(bytes("\n$> ",'utf-8'))
    usbdata.flush()
    s = usbdata.readline()
    return s

def initiate(pixels):
    pixels.fill(bling.EMPTY)
    pixels.show()
    pixels[0] = bling.PURPLE
    pixels[2] = bling.PURPLE
    pixels.show()
    num = serialinput()
    if num.rstrip().decode() == str(10):
        pixels.fill(bling.EMPTY)
        pixels.show()
        pixels[0] = bling.PURPLE
        pixels[1] = bling.PURPLE
        pixels[3] = bling.PURPLE
        pixels.show()
        num = serialinput()
        if num.rstrip().decode() == str(13):
            pixels.fill(bling.EMPTY)
            pixels.show()
            pixels[1] = bling.PURPLE
            pixels[3] = bling.PURPLE
            pixels.show()
            num = serialinput()
            if num.rstrip().decode() == str(5):
                return True
    return False