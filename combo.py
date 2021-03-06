from microbit import *
from moonBuggy import *
import radio

radio.on()
radio.config(channel=0)   # change this!

def grabber_open():
    on_the_moon()
    pin16.write_analog(60)

def grabber_close():
    on_the_moon()
    pin16.write_analog(35)

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
        # NEW CODE HERE
        elif message == 'combo':            # combo move to open the grabber and drive forward at the same time
            display.show(Image.DUCK)
            drive(500, 500)
            grabber_open()
        # NEW CODE ENDS
        else:
            stop()
        sleep(time)
        stop()
