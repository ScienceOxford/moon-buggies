from microbit import *
from moonBuggy import *
import radio

radio.on()
radio.config(channel=0) # change this!

def grabber_open():
    on_the_moon()
    pin16.write_analog(60)

def grabber_close():
    on_the_moon()
    pin16.write_analog(35)

# NEW CODE HERE
def time_500():
    global time     # needed to allow the function to affect the main 'time' variable
    on_the_moon()
    time = 500      # the time in miliseconds before the buggy will do the next command

def time_1000():
    global time
    on_the_moon()
    time = 1000
# NEW CODE ENDS

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
        elif message == 'time 500':
            time_500()
        elif message == 'time 1000':
            time_1000()
        # NEW CODE ENDS
        else:
            stop()
        sleep(time)
        stop()
