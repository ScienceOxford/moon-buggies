from microbit import *
import radio

radio.on()
radio.config(channel=0) #CHANGE CHANNEL

def do(message):
    radio.send(str(message))

def instructions():
    radio.send('earth')
    sleep(100)
    radio.send('grab 5')
    sleep(100)
    radio.send('forward 500 2000')
    sleep(100)
    radio.send('left 500 500')
    sleep(100)
    radio.send('forward 500 1000')
    sleep(100)
    radio.send('grab 2')
    sleep(100)

do('forward 500 2000')
do('grab 5')
instructions()
