from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

# Line-following robot code for microbit with L9110s motor driver
# Thanks to MultiWingSpan, whose code for the Bit:Bot was a great starting point
# http://www.multiwingspan.co.uk/micro.php?page=botline

radio.on()
radio.config(channel=12)

LF = pin14
LB = pin13
RF = pin12
RB = pin15

# 1023 turns the motors off; 0 turns them on at full speed
def stop():
    LF.write_analog(1023)
    LB.write_analog(1023)
    RF.write_analog(1023)
    RB.write_analog(1023)
    #display.show(Image.HAPPY)


# Inputs between 0-1023 to control both motors
def drive(L, R):
    # Below controls the left wheel: forward, backward, stop at given speed
    if L > 0 and L <= 1023:
        LF.write_analog(abs(L-1023))  # go forwards at speed given
        LB.write_analog(1023)         # don't go backwards
    elif L < 0 and L >= -1023:
        LF.write_analog(1023)         # don't go forwards
        LB.write_analog(abs(L+1023))  # go backwards at speed given
    else:
        LF.write_analog(1023)         # stop the left wheel
        LB.write_analog(1023)
    # Below controls the right wheel: forward, backward, stop at given speed
    if R > 0 and R <= 1023:
        RF.write_analog(abs(R-1023))  # go forwards at speed given
        RB.write_analog(1023)         # don't go backwards
    elif R < 0 and R >= -1023:
        RF.write_analog(1023)         # don't go forwards
        RB.write_analog(abs(R+1023))  # go backwards at speed given
    else:
        RF.write_analog(1023)         # stop the right wheel
        RB.write_analog(1023)

stop()

while True:
    message = radio.receive()
    if message is not None:
        try:
            # split message into ["direction", "speed", "time"] e.g. ["forward", "500", "800"]
            command = message.split()
            direction = command[0]
            try:
                speed = int(command[1])
            except:
                speed = 500
            try:
                time = int(command[2])
            except:
                time = 500
            sleep(1255)     # delay between Earth & Moon
            if direction == 'forward':
                display.show(Image.ARROW_N)
                drive(speed, speed)
                sleep(time)
            elif direction == 'left':
                display.show(Image.ARROW_W)
                drive(-speed, speed)
                sleep(time)
            elif direction == 'right':
                display.show(Image.ARROW_E)
                drive(speed, -speed)
                sleep(time)
            elif direction == 'backward':
                display.show(Image.ARROW_S)
                drive(-speed, -speed)
                sleep(time)
        except:
            # if message not in correct format, show error, then move on
            stop()
            display.show(Image.SQUARE)
            pass
    else:
        stop()
        display.show(Image.SQUARE_SMALL)
