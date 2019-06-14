from microbit import *

servo = 35

def servo_write():
    pin1.write_analog(servo)
    print(str(servo))

servo_write()

while True:
    if button_a.was_pressed():
        servo += 5
        servo_write()
    elif button_b.was_pressed():
        servo -= 5
        servo_write()
