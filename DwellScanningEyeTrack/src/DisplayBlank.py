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

"""
DisplayBlank.py

DwellTask Psychopy3 Sub function.

This function is for displaying blank part.

Created on Wed Feb  3 13:32:56 EST 2021

@author: Kyunghun Lee
- Created on Wed Feb  3 13:32:56 EST 2021 by KL
"""

from psychopy import core
import random,datetime,sys
import time

# Import defined functions
sys.path.insert(1, './src')
from DictWrite import DictWrite,DictWriteRaw
from GetKeyPress import GetKeyPress

def DisplayBlank(df,dfRaw,params,dict,dictRaw,win,tracker,blankTime):
    # UnpauseMusic()

    # Select BlankTime duration randomly.
    # blankTime = params['blankTime']
    # # blankTime = [2]
    # blankDuration = random.choice(blankTime)
    blankDuration = blankTime

    # Record status
    dict["Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    startTime = time.time()
    dict["Section"] = "DisplayBlank"
    dict["Image Displayed"] = "Blank for " + str(blankDuration) + " sec"
    # dict["Button Pressed"] = ""
    # dict["Button Correct/Incorrect"] = ""
    # dict["Button Response Time"] = ""
    dictRaw["Event"] = dict["Image Displayed"] + "shown (start)"

    DictWriteRaw(dfRaw, dictRaw, params)

    win.flip()

    resolution = params['screenSize']
    tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (
        "./img/FixationCross/blank.jpg", resolution[0] / 2, resolution[1] / 2, resolution[0], resolution[1]))

    # core.wait(blankDuration)
    startTime = time.time()
    while (time.time() - startTime < blankDuration):
        GetKeyPress()
        core.wait(1 / 300)

    # Record status
    dict["End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Duration"] = time.time() - startTime
    dictRaw["Event"] = dict["Image Displayed"] + " shown (end)"
    DictWriteRaw(dfRaw, dictRaw, params)
    DictWrite(df, params, dict)

    # End Eyetracker
    # Eyetracker label (end and new start)
    # tracker.sendMessage('TRIAL_RESULT 0')
    # tracker.sendMessage('TRIALID %d' % params["eyeIdx"])
    # params["eyeIdx"] += 1
