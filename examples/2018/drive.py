from microbit import *
from moonBuggy import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()
radio.config(channel=0) #CHANGE THIS!

time = 500

while True:
    message = radio.receive()
    if message is not None:
        if message == 'forward':
            display.show(Image.ARROW_N)
            drive(500, 500)
        elif message == 'left':
            display.show(Image.ARROW_W)
            drive(-500, 500)
        elif message == 'right':
            display.show(Image.ARROW_E)
            drive(500, -500)
        elif message == 'backward':
            display.show(Image.ARROW_S)
            drive(-500, -500)
        elif message == 'stop':
            display.show(Image.HAPPY)
            stop()
        
        # add new code here
        
        else:
            stop()
        sleep(time)
        stop()
