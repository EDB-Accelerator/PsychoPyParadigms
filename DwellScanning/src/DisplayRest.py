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

def waitUserSpace(Df,params):
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q'] or c == ['Esc']:
            print('Q pressed. Forced Exit.')
            core.quit()

def DisplayRest(df,dfRaw,params,dict,dictRaw,win):

    # Record status
    dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Section"] = "DisplayRestScreen"
    dict["Image Displayed"] = "Message: Let's rest for a bit.  Press the spacebar when you are ready to keep playing."
    dict["Button Pressed"] = ""
    dict["Button Correct/Incorrect"] = ""
    dict["Button Response Time"] = ""
    dictRaw["Event"] = "Rest message shown (start)"
    DictWriteRaw(dfRaw, dictRaw, params)

    message = visual.TextStim(win,
                              text="Let's rest for a bit.  \n\n Press the spacebar when you are ready to keep playing.",
                              units='norm', wrapWidth=2,color='black')
    message.draw()
    win.flip()
    waitUserSpace(df, params)

    # Record status
    dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dictRaw["Event"] = dict["Image Displayed"] + " shown (end)"
    DictWriteRaw(dfRaw, dictRaw, params)
    DictWrite(df, params, dict)
