#import modules
from psychopy.visual import Window, Rect
from psychopy.event import  Mouse
from psychopy import core

#initialise screen and mouse
display = (1366,768)
win = Window(size=display, monitor="testMonitor",winType='pyglet',color='white', fullscr=False, units = 'pix')
mouse = Mouse(visible=True)

#create box object
# box = Rect(win,width=420,height=50, lineWidth = 3,lineColor='black', pos=(0,0), fillColor = (0.9,0.7,0.7))

#show box object until mouse click
# mouse_has_been_pressed = False
while True:  # keep looping. We will break this loop on a mouse press
    # print(mouse.getPressed)
    if mouse.getPressed()[0] == 1:  # check if click is within shape
        print("Left Clicked")
    # else:
    #     print("incorrect")
    if mouse.getPressed()[2] == 1:
        print("Right Clicked")
    core.wait(1/8)
# while True:
    # box.draw()

    # if mouse.isPressedIn(box, buttons=[0] ):  # left button press
    #     # mouse_has_been_pressed = True
    #     print(mouse_has_been_pressed)
    #
    # if not mouse.isPressedIn(box, buttons=[0] ) and mouse_has_been_pressed == True:
    #     # win.close()
    #     mouse_has_been_pressed = False
    #     print(mouse_has_been_pressed)

    # win.flip()






# from psychopy.hardware import keyboard
# from psychopy import core
#
# # https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
# #
# # kb = keyboard.Keyboard()
# # kp = kb.getKeys(waitRelease=False, clear=False)
# # if len(kp) > 0:
# #     if kp[-1].duration is None:
# #         dur = round(t-kp[-1].rt, 1)
# #         text.text = str(dur)
#
# from psychopy.iohub import launchHubServer
# from psychopy.core import getTime
#
# # Start the ioHub process. 'io' can now be used during the
# # experiment to access iohub devices and read iohub device events.
# io = launchHubServer()
#
# keyboard = io.devices.keyboard
#
# # Check for and print any Keyboard events received for 5 seconds.
# stime = getTime()
# while getTime()-stime < 5.0:
#     for e in keyboard.getEvents():
#         print(e)
#
# # Stop the ioHub Server
# io.quit()
#
#
# # # during your trial
# # kb.clock.reset()  # when you want to start the timer from
# # keys = kb.getKeys(['right', 'left', 'quit'], waitRelease=True)
# #
# # while True:
# #     keys = kb.getKeys(['right', 'left', 'quit'], waitRelease=False)
# #     keys2 = kb.getKeys(['right', 'left', 'quit'], waitRelease=True)
# #     for key in keys:
# #         print("keys",key.name, key.rt, key.duration)
# #     for key in keys2:
# #         print("keys2",key.name, key.rt, key.duration)
# #
# #     print(keys)
# #     core.wait(0.1)
# #
# # if 'quit' in keys:
# #     core.quit()
#
# # kb = KeyBoard()
# # wait for keypresses here
# # keys = kb.getKeys()
# # for thisKey in keys:
# #     if thisKey=='q':  # it is equivalent to the string 'q'
# #         core.quit()
# #     else:
# #         print(thisKey.name, thisKey.tDown, thisKey.rt)
# #
# # while True:
# #     kb = keyboard.Keyboard()
# #     kb.clock.reset()
# #     keys = kb.getKeys()
# #     for thisKey in keys:
# #         if thisKey == 'q':  # it is equivalent to the string 'q'
# #             core.quit()
# #         else:
# #             print(thisKey.name, thisKey.tDown, thisKey.rt)
#
# from pynput.keyboard import Key, Listener
#
# def on_press(key):
#     # print('{0} pressed'.format(
#     #     key))
#     print("pressed:",key)
#
# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False
#
# # Collect events until released
# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()