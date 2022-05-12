from microbit import *
import radio

LF = pin13
LB = pin12
RF = pin15
RB = pin14

def stop():
    LF.write_analog(0)
    LB.write_analog(0)
    RF.write_analog(0)
    RB.write_analog(0)
    display.show(Image.TARGET)

# Inputs between 0-1023 to control both motors
def drive(L, R):
    # Below controls the left wheel: forward, backward, stop at given speed
    if L > 0 and L <= 1023:
        LF.write_analog(abs(L))  # go forwards at speed given
        LB.write_analog(0)         # don't go backwards
    elif L < 0 and L >= -1023:
        LF.write_analog(0)         # don't go forwards
        LB.write_analog(abs(L))  # go backwards at speed given
    else:
        LF.write_analog(0)         # stop the left wheel
        LB.write_analog(0)
    # Below controls the right wheel: forward, backward, stop at given speed
    if R > 0 and R <= 1023:
        RF.write_analog(abs(R))  # go forwards at speed given
        RB.write_analog(0)         # don't go backwards
    elif R < 0 and R >= -1023:
        RF.write_analog(0)         # don't go forwards
        RB.write_analog(abs(R))  # go backwards at speed given
    else:
        RF.write_analog(0)         # stop the right wheel
        RB.write_analog(0)

def mistake(error):
    stop()
    display.show(error)
    sleep(5000)
    stop()

radio.on()
radio.config(channel=0, queue=10) #CHANGE CHANNEL

on_the_moon = True
directions = ['forward', 'forwards', 'left', 'right', 'backward', 'backwards']
grabber = {'1': 30, '2': 35, '3': 40, '4': 45, '5': 50, '6': 55}

while True:
    message = (radio.receive())
    if message is not None and len(str(message).lower().split()) > 0: # if message is received and contains at least one "word"
        message = message.lower()
        if message == 'earth':
            on_the_moon = False
        elif message == 'moon':
            on_the_moon = True
        elif message == 'stop':
            stop()

        else:
            message = message.split()

            if on_the_moon is True:
                sleep(1255)

            if message[0] in directions:
                try:
                    speed = int(message[1])
                    if speed > 1023:
                        speed = 1023
                    elif speed < 400:
                        speed = 400

                    time = int(message[2])
                    if time > 10000:
                        time = 10000
                    elif time < 100:
                        time = 100

                    if message[0] == 'forward' or message[0] == 'forwards':
                        drive(speed, speed)
                    elif message[0] == 'left':
                        drive(-speed, speed)
                    elif message[0] == 'right':
                        drive(speed, -speed)
                    elif message[0] == 'backward' or message[0] == 'backwards':
                        drive(-speed, -speed)

                    sleep(time)
                    stop()

                except:
                    mistake(2) # if a direction but not given both speed and time

            elif message[0] == 'grab':
                try:
                    if message[1] in grabber:
                        pin16.write_analog(grabber[message[1]])
                        sleep(1000)
                    else:
                        mistake(3) # if grab but option is not correct
                except:
                    mistake(4) # if grab but nothing else
            else:
                mistake(1) # if not in directions or grab, you spelt something wrong
