from adafruit_hid.mouse import Mouse

def drawmorse(m,drawtype,length,repeat=1):
    x = 0
    if drawtype == 'dash':
        x = 10
    elif drawtype == 'dot':
        x = 5
    elif drawtype == "newline":
        reset = length * -1
        m.move(-22,5,0)
        length = 0
        return length
    for i in range(0,repeat):
        m.press(Mouse.LEFT_BUTTON)
        m.move(x,0,0)
        m.release(Mouse.LEFT_BUTTON)
        m.move(5,0,0)
        length += x
        length += 5
    return length

def spookymorse(m):
    length = 0
    length = drawmorse(m,'dot',length,4)
    length = drawmorse(m,'newline',length)
    
    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dot',length,4)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'dash',length,2)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dot',length,3)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dot',length,3)
    length = drawmorse(m,'dash',length,2)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'newline',length)

    
    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dot',length,3)
    length = drawmorse(m,'dash',length,2)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dot',length,3)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dot',length,2)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dash',length,2)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'newline',length)

    
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'dot',length,2)
    length = drawmorse(m,'newline',length)

    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'dash',length,2)
    length = drawmorse(m,'dot',length,1)
    length = drawmorse(m,'dash',length,1)
    length = drawmorse(m,'newline',length)