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

from psychopy import visual,core,event
import time,random,datetime,sys

# Import defined functions
sys.path.insert(1, './src')
# from TableWrite import TableWrite,TableWriteRaw
from DictWrite import DictWrite,DictWriteRaw
from GetKeyPress import GetKeyPress
from MusicControl import StopMusic
from psychopy.visual import ShapeStim
import os.path

def pointFromCenter(n,center,standard):
    return int(center+n*(center*2)/standard)

def DisplayFixationCross(df,dfRaw,params,dict,dictRaw,win,tracker):
    # After Calibration before fixation cross
    tracker.sendMessage('TRIAL_RESULT 0')

    # Initialization
    r = 1000
    dict["Section"] = "DisplayFixationArrow"

    # Get the random seed:
    bold = (params['fixationOrder']).pop()

    if bold == 'l':
        bold = 'Left Arrow'
    elif bold == 'r':
        bold = 'Right Arrow'
    else:
        bold = 'Line'


    if bold == 'Left Arrow':
        arrowLeft = [(-0.2 * r, 0.05 * r), (-0.2 * r, -0.05 * r), (0, -0.05 * r), (0, -0.1 * r), (0.2 * r, 0),
                     (0, 0.1 * r),(0, 0.05 * r)]
        arrowStim = ShapeStim(win, vertices=arrowLeft, units='pix', fillColor='black', size=.5, lineColor='black',
                           pos=[0,0])
        imgScreenShot = 'img/FixationCross/left.jpg'
    elif bold == 'Right Arrow':
        arrowRight = [(0.2 * r, 0.05 * r), (0.2 * r, -0.05 * r), (0, -0.05 * r), (0, -0.1 * r), (-0.2 * r, 0),
                      (0, 0.1 * r),(0, 0.05 * r)]
        arrowStim = ShapeStim(win, vertices=arrowRight, units='pix', fillColor='black', size=.5, lineColor='black',
                           pos=[0,0])
        imgScreenShot = 'img/FixationCross/right.jpg'
    else: # Line
        arrowLine = [(-0.2 * r, 0.05 * r), (-0.2 * r, -0.05 * r), (.2 * r, -.05 * r), (.2 * r, 0.05 * r)]
        arrowStim = ShapeStim(win, vertices=arrowLine, units='pix', fillColor='black', size=.5, lineColor='black',
                              pos=[0,0])
        imgScreenShot = 'img/FixationCross/line.jpg'

    # Flip Window (display FixationCross image)
    arrowStim.draw()
    win.flip()

    if os.path.exists(imgScreenShot) == False:
        win.getMovieFrame()  # Defaults to front buffer, I.e. what's on screen now.
        win.saveMovieFrames(imgScreenShot)

    # Eyetracker label (start)
    resolution = params['screenSize']
    tracker.sendMessage('TRIALID %d' % params["eyeIdx"])
    params["eyeIdx"] += 1
    tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (
        "./img/FixationCross/blank.jpg", resolution[0] / 2, resolution[1] / 2, resolution[0], resolution[1]))
    # tracker.sendMessage('!V IMGLOAD CENTER %s %d %d' % ("./img/FixationCross/" + bold + ".jpg", params['screenSize'][0] / 2, params['screenSize'][1] / 2))
    tracker.sendMessage('!V IMGLOAD CENTER %s %d %d' % (imgScreenShot, params['screenSize'][0] / 2,
                                                        params['screenSize'][1] / 2))
    tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (
    1, pointFromCenter(-100, params['screenSize'][0] / 2, params['screenSize'][0]),
    pointFromCenter(-60, params['screenSize'][1] / 2, params['screenSize'][1]),
    pointFromCenter(100, params['screenSize'][0] / 2, params['screenSize'][0]),
    pointFromCenter(60, params['screenSize'][1] / 2, params['screenSize'][1]), 'Fixation:'+bold))

    dictRaw["Event"] = bold + " shown (start)"
    DictWriteRaw(dfRaw,dictRaw,params)

    # Show scale and measure the elapsed wall-clock time.
    startTime = time.time()
    dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    # core.wait(0.15)
    # c = event.getKeys()
    circle = visual.Circle(win=win, units="pix", fillColor='black', lineColor='white', edges=1000, pos=(0,0),
                           radius=10)
    if params['circle']:
        circle.draw()
    arrowStim.draw()

    # while time.time() - startTime < 1:
    #     core.wait(1 / 120)

    # Get user input.
    c = []
    event.clearEvents()
    while time.time() - startTime < 1:
        core.wait(1 / 120)
        if c == []:
            # c = GetKeyPress()
            # event.clearEvents()
            c = event.getKeys()
        if len(c) >= 1:
            dictRaw["Event"] = "User Response:" + c[0]
            DictWriteRaw(dfRaw, dictRaw, params)


    if c == ['q'] or c == ['Q']:
        print('Q pressed. Forced Exit.')
        StopMusic()
        core.quit()
    if len(c) >= 1:
        c = c[0]
    else:
        c = "No Response"

    # Record Result
    dictRaw["Event"] = bold + " shown (end)"
    DictWriteRaw(dfRaw, dictRaw, params)
    dict["Image Displayed"] = bold
    dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Duration"] = time.time() - startTime
    dict["User Response"] = c
    DictWrite(df, params, dict)
    dict["User Response"] = ""

    # End Eyetracker
    # Eyetracker label (end and new start)
    tracker.sendMessage('TRIAL_RESULT 0')
    tracker.sendMessage('TRIALID %d' % params["eyeIdx"])
    params["eyeIdx"] += 1

def DisplayFixationOld(df,dfRaw,params,dict,dictRaw,win,tracker):
    # UnpauseMusic()

    # After Calibration before fixation cross
    tracker.sendMessage('TRIAL_RESULT 0')

    # Initialization
    fCS = 0.1 # size (for brevity)
    fCP = [0,0] # position (for brevity)
    boldOption = ['Horizontal','Vertical']
    dict["Section"] = "DisplayFixationCross"
    # dict["Button Pressed"] = "Not answered"
    # dict["Button Correct/Incorrect"] = ""
    # dict["Button Response Time"] = ""

    # Get the random seed:
    randN = random.randint(0,1)
    bold = boldOption[randN]

    if bold == 'Horizontal':
        fixation1 = visual.ShapeStim(win, lineColor='#000000', lineWidth=3.0, vertices=(
        (fCP[0], fCP[1]), (fCP[0], fCP[1] + fCS / 2), (fCP[0], fCP[1] - fCS / 2)), units='height', closeShape=False,
                                     name='fixCross');
        fixation2 = visual.ShapeStim(win, lineColor='#000000', lineWidth=10.0,
                                     vertices=((fCP[0] - fCS / 2, fCP[1]), (fCP[0] + fCS / 2, fCP[1])), units='height',
                                     closeShape=False, name='fixCross');
    elif bold == 'Vertical':
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

    # Eyetracker label (start)
    resolution = params['screenSize']
    tracker.sendMessage('TRIALID %d' % params["eyeIdx"])
    params["eyeIdx"] += 1
    tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (
        "./img/FixationCross/blank.jpg", resolution[0] / 2, resolution[1] / 2, resolution[0], resolution[1]))
    tracker.sendMessage('!V IMGLOAD CENTER %s %d %d' % ("./img/FixationCross/" + bold + ".jpg", params['screenSize'][0] / 2, params['screenSize'][1] / 2))
    tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (
    1, pointFromCenter(-100, params['screenSize'][0] / 2, params['screenSize'][0]),
    pointFromCenter(-60, params['screenSize'][1] / 2, params['screenSize'][1]),
    pointFromCenter(100, params['screenSize'][0] / 2, params['screenSize'][0]),
    pointFromCenter(60, params['screenSize'][1] / 2, params['screenSize'][1]), 'Fixation Cross'))

    dictRaw["Event"] = bold + " shown (start)"
    DictWriteRaw(dfRaw,dictRaw,params)

    # Show scale and measure the elapsed wall-clock time.
    startTime = time.time()
    dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    # core.wait(0.15)
    # c = event.getKeys()
    circle = visual.Circle(win=win, units="pix", fillColor='black', lineColor='white', edges=1000, pos=(0,0),
                           radius=10)
    if params['circle']:
        circle.draw()
    fixation1.draw()
    fixation2.draw()

    # while time.time() - startTime < 1:
    #     core.wait(1 / 120)

    # Get user input.
    c = []
    event.clearEvents()
    while time.time() - startTime < 1:
        core.wait(1 / 120)
        if c == []:
            # c = GetKeyPress()
            # event.clearEvents()
            c = event.getKeys()
        if len(c) >= 1:
            dictRaw["Event"] = "User Response:" + c[0]
            DictWriteRaw(dfRaw, dictRaw, params)


    if c == ['q'] or c == ['Q']:
        print('Q pressed. Forced Exit.')
        StopMusic()
        core.quit()
    if len(c) >= 1:
        c = c[0]
    else:
        c = "No Response"
    # while (c != ['space']):
    #     # print(c)
    #     core.wait(1 / 120)
    #     # import asyncio, threading
    #     # loop = asyncio.get_event_loop()
    #     # t = threading.Thread(target=event.getKeys(), args=())
    #     # t.start()
    #
    #     c = event.getKeys()
    #     position = tracker.getPosition()
    #     if position is None or type(position) == int:
    #         continue
    #
    #     # Thresholding
    #     position[0] = params['screenSize'][0] if position[0]>params['screenSize'][0] else position[0]
    #     position[0] = -1*params['screenSize'][0] if position[0] < -1 * params['screenSize'][0] else position[0]
    #     position[1] = params['screenSize'][1] if position[1]>params['screenSize'][1] else position[1]
    #     position[1] = -1*params['screenSize'][1] if position[1] < -1 * params['screenSize'][1] else position[1]
    #
    #
    #     # gazeTime = 0
    #
    #     # while abs(position[0])<80 and abs(position[1]) <80:
    #     #     gazeTime = time.time() - startTime
    #     #     positionTmp = position
    #     #     position = tracker.getPosition()
    #     #
    #     #     if position is None:
    #     #         position = positionTmp
    #     #         # continue
    #     #
    #     #     circle.pos = position
    #     #     if params['circle']:
    #     #         circle.draw()
    #     #     fixation1.draw()
    #     #     fixation2.draw()
    #     #     win.flip()
    #
    #     circle.pos = position
    #     if params['circle']:
    #         circle.draw()
    #     fixation1.draw()
    #     fixation2.draw()
    #     win.flip()
    #
    #     # if gazeTime > 1:
    #         # break

    # Record Result
    dictRaw["Event"] = bold + " shown (end)"
    DictWriteRaw(dfRaw, dictRaw, params)
    dict["Image Displayed"] = bold
    dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Duration"] = time.time() - startTime
    dict["User Response"] = c
    DictWrite(df, params, dict)
    dict["User Response"] = ""

    # End Eyetracker
    # Eyetracker label (end and new start)
    tracker.sendMessage('TRIAL_RESULT 0')
    tracker.sendMessage('TRIALID %d' % params["eyeIdx"])
    params["eyeIdx"] += 1

