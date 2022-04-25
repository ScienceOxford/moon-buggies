from microbit import *
from moonBuggy import *
import radio

radio.on()
radio.config(channel=0)   # change this!

def grabber_open():
    on_the_moon()
    display.show(Image.CONFUSED)

def grabber_close():
    on_the_moon()
    display.show(Image.CONFUSED)

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
        elif message == 'open':
            grabber_open()
        elif message == 'close':
            grabber_close()
        else:
            stop()
        sleep(time)
        stop()
