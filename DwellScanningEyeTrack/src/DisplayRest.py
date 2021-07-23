# Python3-based package
"""
MIT License

Copyright (c) 2021 NIMH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from psychopy import core,event,visual
import datetime,sys
import time

# Import defined functions
sys.path.insert(1, './src')
from DictWrite import DictWrite,DictWriteRaw
from StartMusic import playMusic,pauseMusic,stopMusic

def waitUserSpace(Df,params):
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q'] or c == ['Esc']:
            print('Q pressed. Forced Exit.')
            core.quit()

def DisplayRest(df,dfRaw,params,dict,dictRaw,win,sound1):

    # Record status
    dict["Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    startTime = time.time()
    dict["Section"] = "DisplayRestScreen"
    dict["Image Displayed"] = "Message: Let's rest for a bit.  Press the spacebar when you are ready to keep playing."
    dictRaw["Event"] = "Rest message shown (start)"
    DictWriteRaw(dfRaw, dictRaw, params)

    if params['Version'] != 2:

        message = visual.TextStim(win,
                                  text="Let's rest for a bit.  \n\n Press the spacebar when you are ready to keep playing.",
                                  units='norm', wrapWidth=2,color='black')
        message.draw()
        win.mouseVisible = False
        win.flip()
        sound1 = pauseMusic(sound1)
        waitUserSpace(df, params)
        sound1 = playMusic(sound1, params)
    else:
        message = visual.TextStim(win,
                                  text="Let's rest for a bit.",
                                  units='norm', wrapWidth=2,color='black')
        message.draw()
        core.wait(10)

    # Record status
    dict["End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Duration"] = time.time() - startTime
    dictRaw["Event"] = dict["Image Displayed"] + " shown (end)"
    DictWriteRaw(dfRaw, dictRaw, params)
    DictWrite(df, params, dict)
    win.close()
    return sound1
