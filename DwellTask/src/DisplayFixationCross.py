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
DisplayFixationCross.py

DwellTask Psychopy3 Sub function.

This function is for displaying Fixation Cross.

Created on Wed Feb  3 13:33:38 EST 2021

@author: Kyunghun Lee
- Created on Wed Feb  3 13:33:38 EST 2021 by KL
"""

from psychopy import visual,event,core
import time,random,datetime,sys

# Import defined functions
sys.path.insert(1, './src')
from TableWrite import TableWrite,TableWriteRaw

def DisplayFixationCross(df,dfRaw,params,dict,dictRaw,win):

    # Initialization
    fCS = 0.1 # size (for brevity)
    fCP = [0,0] # position (for brevity)
    boldOption = ['Horizontal','Vertical']
    dict["Section"] = "DisplayFixationCross"
    dict["Button Pressed"] = "Not answered"
    dict["Button Correct/Incorrect"] = ""
    dict["Button Response Time"] = ""

    # Get the random seed:
    randN = random.randint(0,1)
    bold = boldOption[randN]

    if bold is 'Horizontal':
        fixation1 = visual.ShapeStim(win, lineColor='#000000', lineWidth=3.0, vertices=(
        (fCP[0], fCP[1]), (fCP[0], fCP[1] + fCS / 2), (fCP[0], fCP[1] - fCS / 2)), units='height', closeShape=False,
                                     name='fixCross');
        fixation2 = visual.ShapeStim(win, lineColor='#000000', lineWidth=10.0,
                                     vertices=((fCP[0] - fCS / 2, fCP[1]), (fCP[0] + fCS / 2, fCP[1])), units='height',
                                     closeShape=False, name='fixCross');
    elif bold is 'Vertical':
        fixation1 = visual.ShapeStim(win, lineColor='#000000', lineWidth=10.0, vertices=(
        (fCP[0], fCP[1]), (fCP[0], fCP[1] + fCS / 2), (fCP[0], fCP[1] - fCS / 2)), units='height', closeShape=False,
                                     name='fixCross');
        fixation2 = visual.ShapeStim(win, lineColor='#000000', lineWidth=3.0,
                                     vertices=((fCP[0] - fCS / 2, fCP[1]), (fCP[0] + fCS / 2, fCP[1])), units='height',
                                     closeShape=False, name='fixCross');
    fixation1.draw()
    fixation2.draw()

    # Flip Window (display FixationCross image)
    win.flip()
    dictRaw["Event"] = bold + " shown (start)"
    dfRaw = TableWriteRaw(dfRaw,dictRaw)

    # Show scale and measure the elapsed wall-clock time.
    keys = []
    startTime = endTime = time.time()
    dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    core.wait(0.15)
    while (endTime - startTime < 1):
        keys = event.getKeys()
        endTime = time.time()
        if keys == ['1'] or keys == ['2']:
            dictRaw["Event"] = keys[0] + " pressed"
            dfRaw = TableWriteRaw(dfRaw, dictRaw)
            dict["Button Pressed"] = keys[0]
            dict["Button Response Time"] = endTime - startTime
            dict["Button Correct/Incorrect"] = "Correct" if randN+1 == int(keys[0]) else "Incorrect"
            break
        core.wait(1 / 300)
    while (endTime - startTime < 1):
        endTime = time.time()
        core.wait(1 / 300)

    dictRaw["Event"] = bold + " shown (end)"
    dfRaw = TableWriteRaw(dfRaw,dictRaw)
    dict["Image Displayed"] = bold
    dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    return TableWrite(df,params,dict),dfRaw

