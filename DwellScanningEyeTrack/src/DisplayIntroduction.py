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

import time,random,datetime,sys

# Import defined functions
sys.path.insert(1, './src')
# from TableWrite import TableWrite,TableWriteRaw
from DictWrite import DictWrite,DictWriteRaw
from GetKeyPress import GetKeyPress
from MusicControl import StopMusic
from psychopy import visual, event, core
from psychopy.visual import ShapeStim
from WaitUserSpace import WaitUserSpace

def pointFromCenter(n,center,standard):
    return int(center+n*(center*2)/standard)

def DisplayIntroduction(df,dfRaw,params,dict,dictRaw,win,tracker):
    r = 1000
    arrowLeft = [(-0.2 * r, 0.05 * r), (-0.2 * r, -0.05 * r), (0, -0.05 * r), (0, -0.1 * r), (0.2 * r, 0), (0, 0.1 * r),
                 (0, 0.05 * r)]
    arrowRight = [(0.2 * r, 0.05 * r), (0.2 * r, -0.05 * r), (0, -0.05 * r), (0, -0.1 * r), (-0.2 * r, 0), (0, 0.1 * r),
                  (0, 0.05 * r)]
    arrowLine = [(-0.2 * r, 0.05 * r), (-0.2 * r, -0.05 * r), (.2 * r, -.05 * r), (.2 * r, 0.05 * r)]

    arrowR = ShapeStim(win, vertices=arrowRight, units='pix', fillColor='black', size=.5, lineColor='black',
                       pos=[0, .1 * r])
    arrowL = ShapeStim(win, vertices=arrowLeft, units='pix', fillColor='black', size=.5, lineColor='black',
                       pos=[-0.3 * r, .1 * r])
    arrowLine = ShapeStim(win, vertices=arrowLine, units='pix', fillColor='black', size=.5, lineColor='black',
                          pos=[0.3 * r, .1 * r])

    messageR = visual.TextStim(win, text="Press the right\nbutton",
                               units='pix', wrapWidth=400, color="black", pos=[-0.3 * r, -.06 * r], height=30)
    messageL = visual.TextStim(win, text="Press the left\nbutton",
                               units='pix', wrapWidth=200, color="black", pos=[0 * r, -.06 * r], height=30)
    messageC = visual.TextStim(win, text="Do not press a \nbutton",
                               units='pix', wrapWidth=200, color="black", pos=[0.3 * r, -.06 * r], height=30)

    message = visual.TextStim(win,text="Press space bar to proceed.",units='pix', wrapWidth=1000, color='black',pos=[0,-200],height=40)
    arrowL.draw()
    arrowR.draw()
    arrowLine.draw()
    messageR.draw()
    messageL.draw()
    messageC.draw()
    message.draw()
    win.flip()

    # Record (start)
    dictRaw["Event"] = "Instruction Image (arrow) displayed (start)"
    DictWriteRaw(dfRaw, dictRaw, params)
    startTime = time.time()
    dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]

    WaitUserSpace()

    # Record (end)
    dictRaw["Event"] = "Instruction Image (arrow) displayed (end)"
    DictWriteRaw(dfRaw, dictRaw, params)
    dict["Image Displayed"] = "Instruction Image (arrow) displayed"
    dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Duration"] = time.time() - startTime
    DictWrite(df, params, dict)
