import time
from random import randint, seed
import gc

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255,25,0)
PURPLE = (100, 15, 230)
WHITE = (255,255,255)
EMPTY = (0, 0, 0)

num_pixels = 4
seed(time.time())

def lerp(x, x0, x1, y0, y1):
    # Clamp x within x0 and x1 bounds.
    if x > x1:
        x = x1
    if x < x0:
        x = x0
    # Calculate linear interpolation of y value.
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))

# Set all pixels to the specified color.
def fill_pixels(pixels,r, g, b,state_pixels):
    for i in range(0, state_pixels):
        pixels[i] = (r, g, b)
        pixels.write()

def color_gradient(start_r, start_g, start_b, end_r, end_g, end_b, pos):
    # Interpolate R,G,B values and return them as a color.
    red = lerp(pos, 0.0, 1.0, start_r, end_r)
    green = lerp(pos, 0.0, 1.0, start_g, end_g)
    blue = lerp(pos, 0.0, 1.0, start_b, end_b)

    return (red, green, blue)

def animate_gradient_fill(pixels,start_r, start_g, start_b, end_r, end_g, end_b,
                          duration_ms,state_pixels):
    start = time.monotonic()
    fill_pixels(pixels,start_r, start_g, start_b,state_pixels)
    delta = time.monotonic() - start
    while delta < duration_ms:
        pos = delta / duration_ms
        color = color_gradient(start_r, start_g, start_b,
                               end_r, end_g, end_b, pos)
        fill_pixels(pixels,int(color[0]), int(color[1]), int(color[2]),state_pixels)
        delta = time.monotonic() - start
    fill_pixels(pixels,end_r, end_g, end_b,state_pixels)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def jiggle(pixels,cybernetic):
    cybernetic.fill(CYAN)
    cybernetic.show()
    pixels[0] = CYAN
    pixels[1] = CYAN
    pixels.show()
    time.sleep(1)
    pixels.fill(EMPTY)
    pixels.show()
    pixels[2] = CYAN
    pixels[3] = CYAN
    time.sleep(1)
    pixels.show()
    pixels.fill(EMPTY)
    pixels.show()
    return

def color_chase(pixels, color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
        time.sleep(wait)
        pixels[i] = (EMPTY)
        pixels.show()
    time.sleep(0.5)

def kit(pixels,cybernetic,button):
    colors = [RED,YELLOW,BLUE,CYAN,GREEN,WHITE,ORANGE,PURPLE]
    r = randint(0,7)
    for i in range(4):
        if button.value:
            return
        pixels[i] = colors[r]
        pixels.show()
        time.sleep(0.07)
        pixels.fill(EMPTY)
        pixels.show()
    for i in reversed(range(4)):
        if button.value:
            return
        pixels[i] = colors[r]
        pixels.show()
        time.sleep(0.07)
        pixels.fill(EMPTY)
        pixels.show()

def shine(pixels,cybernetic,button):
    cybernetic.fill(YELLOW)
    cybernetic.show()
    for i in range(num_pixels):
        pixels[i] = WHITE
        time.sleep(0.02)
        pixels.show()
        time.sleep(0.01)
        pixels[i] = (YELLOW)
        pixels.show()
    time.sleep(0.5)


def rainbow_random(pixels,cybernetic,button):
    for j in range(255):
        for i in range(num_pixels):
            if button.value:
                return
            r = randint(0,3)
            rc_index = (i * 256 // num_pixels) + j
            pixels[r] = (wheel(rc_index & 255))
            pixels.show()

def pulsestatus(pixels,state):
    animate_gradient_fill(pixels,10, 0, 0, 255, 0, 0, 0.5,int(state))
    animate_gradient_fill(pixels,255, 0, 0, 20, 1, 1, 0.5,int(state))
    animate_gradient_fill(pixels,10, 0, 0, 255, 0, 0, 0.5,int(state))
    animate_gradient_fill(pixels,255, 0, 0, 20, 1, 1, 0.5,int(state))
    animate_gradient_fill(pixels,10, 0, 0, 255, 0, 0, 0.5,int(state))
    animate_gradient_fill(pixels,255, 0, 0, 20, 1, 1, 0.5,int(state))   

def electro(pixels,cybernetic,button):
    r = randint(0,3)
    r2 = randint(0,2)
    pixels.fill(EMPTY)
    pixels.show()
    cybernetic.fill(PURPLE)
    cybernetic.show()
    time.sleep(0.05)
    cybernetic.fill(BLUE)
    pixels[r] = (BLUE,PURPLE,WHITE)[r2]
    if button.value:
        return
    pixels.show()

def evil(pixels,cybernetic,button):
    cybernetic.fill(RED)
    cybernetic.show()
    animate_gradient_fill(pixels,10, 0, 0, 255, 0, 0, 0.5,4)
    animate_gradient_fill(pixels,255, 0, 0, 20, 1, 1, 0.5,4)

def flame(pixels,cybernetic,button):
    r = randint(0,3)
    r2 = randint(0,2)
    cybernetic.fill(YELLOW)
    cybernetic.show()
    time.sleep(0.01)
    cybernetic.fill(ORANGE)
    pixels[r] = (ORANGE,RED, EMPTY)[r2]
    pixels[2] = (ORANGE,ORANGE,RED)[r2]
    if button.value:
        return
    pixels.show()    

def police(pixels,cybernetic,button):
    cybernetic.fill(ORANGE)
    cybernetic.show()
    for i in range(num_pixels):
        if button.value:
            return
        r2 = randint(0,1)
        pixels[i] = (RED,BLUE)[r2]
        pixels.show()
        time.sleep(0.05)
        pixels.fill(EMPTY)
        pixels.show()

def xmas(pixels,cybernetic,button):
    cybernetic.fill(GREEN)
    cybernetic.show()
    for i in range(num_pixels):
        if button.value:
            return
        r2 = randint(0,1)
        pixels[i] = (RED,GREEN)[r2]
        pixels.show()
        time.sleep(0.1)
        pixels.fill(EMPTY)
        pixels.show()

def control(pixels,cybernetic,nosetouch,mouthtouch):
    gc.collect()
    modes = [kit,shine,electro,rainbow_random,xmas,police,flame,evil]
    selection = 0
    while True:
        modes[selection](pixels,cybernetic,nosetouch)
        if nosetouch.value:
            if selection < 7:
                selection += 1
                time.sleep(0.5)
            else:
                selection = 0
                time.sleep(0.5)
            gc.collect()
        if mouthtouch.value:
            return
