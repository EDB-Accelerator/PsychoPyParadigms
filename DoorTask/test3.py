from psychopy.hardware import joystick
from psychopy import visual

joystick.backend='pyglet'  # must match the Window
win = visual.Window([400,400], winType='pyglet')

nJoys = joystick.getNumJoysticks()  # to check if we have any
id = 0
joy = joystick.Joystick(id)  # id must be <= nJoys - 1

# nAxes = joy.getNumAxes()  # for interest
while True:  # while presenting stimuli
    joy.getY()
    a = joy.getY()
    if a==1:
        print(a)
    elif a==-1:
        print(a)
    if sum(joy.getAllButtons()) != 0:
        break

    # ...
    win.flip()  # flipping implicitly updates the joystick info