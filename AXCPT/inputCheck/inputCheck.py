from psychopy import core,event,visual
import os

win = visual.Window(monitor="testMonitor", color="black", size=[1024,768],winType='pyglet')
# Global Exit
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

message = visual.TextStim(win, text="Press Enter any input (type 'q' to exit)")
message.draw()
win.flip()
c = ['']
while (c!= ["good thing"]):
    core.wait(1 / 120)
    c = event.waitKeys()  # read a character
    print(str(c))
    message = visual.TextStim(win, text="Your input (type 'q' to exit):")
    message2 = visual.TextStim(win, text=str(c),
                               units='norm', wrapWidth=1000, color="red", pos=[0, -0.5])
    message.draw()
    message2.draw()
    win.flip()
