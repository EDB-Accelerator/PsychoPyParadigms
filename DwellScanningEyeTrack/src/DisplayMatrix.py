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

This function is for displaying Matrix.

Created on Wed Feb  3 13:34:46 EST 2021

@author: Kyunghun Lee
- Created on Wed Feb  3 13:34:46 EST 2021 by KL
"""

from psychopy import visual,core,event
import datetime,sys,time
from GetKeyPress import GetKeyPress
import os

# Import defined functions
sys.path.insert(1, './src')
from DictWrite import DictWrite,DictWriteRaw
# from StartMusic import playMusic,pauseMusic,stopMusic
from MusicControl import PauseMusic,UnpauseMusic,StopMusic

def DisplayMatrix(df,dfRaw,img,params,dict,dictRaw,win,tracker,labels,emotion):

    rectangles = []
    resolution = params['screenSize']
    for i in range(4):
        for j in range(4):
            gap = 287.5 * 2 / 3 * resolution[1] / 768
            length = 177 * resolution[1] / 768
            oPoint = 287.5 * resolution[1] / 768
            print(str(-oPoint + j * gap), str(oPoint - i * gap))
            rectangles.append(visual.Rect(win=win, units="pix", width=length, height=length,
                                          pos=(-oPoint + j * gap, oPoint - i * gap), fillColor='null', lineColor='null'))
            # rectangles[-1].draw()
    imgStim = visual.ImageStim(win=win, image=img, units="pix", opacity=1, size=(params['screenSize'][1],params['screenSize'][1]))
    imgStim.draw()

    angryRectangles = []
    neutralRectangles = []
    for i in range(len(rectangles)):
        if labels[i]==True:
            angryRectangles.append(rectangles[i])
            if params['circle']:
                angryRectangles[-1].lineColor = 'red'
                # rectangles[i].lineColor = 'red'
                # rectangles[i].draw()
        else:
            neutralRectangles.append(rectangles[i])

    circle = visual.Circle(win=win, units="pix", fillColor='black', lineColor='white', edges=1000, pos=(0,0),
                           radius=10)
    if params['circle']:
        for rectangle in angryRectangles:
            rectangle.draw()
        circle.draw()
    win.flip()

    # Send message Eyetracker
    faceLocations = params['faceLocations']

    if params['EyeLinkSupport']:
        for i in range(len(faceLocations)):
            x1, y1, x2, y2 = faceLocations[i][0], faceLocations[i][1], faceLocations[i][2], faceLocations[i][3]
            if labels[i]:
                tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (i, x1, y1, x2, y2, 'Face' + str(i) + '(' + emotion + ')'))
            else:
                tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (i, x1, y1, x2, y2, 'Face' + str(i)))

        resolution = params['screenSize']
        tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (
            "./img/FixationCross/blank.jpg", resolution[0] / 2, resolution[1] / 2, resolution[0], resolution[1]))
        tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (img, resolution[0] / 2, resolution[1] / 2, resolution[1], resolution[1]))

    # Record status
    dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    sectionStartTime = time.time()
    dict["Section"] = "DisplayMatrix"
    dict["Image Displayed"] = img
    # dict["Button Pressed"] = ""
    # dict["Button Correct/Incorrect"] = ""
    # dict["Button Response Time"] = ""
    dictRaw["Event"] = str(img) + " shown (start)"
    # dfRaw = TableWriteRaw(dfRaw, dictRaw)
    DictWriteRaw(dfRaw, dictRaw, params)

    # Wait for 6 seconds
    # startTime = time.time()
    # while (time.time() - startTime < 6):
    #     GetKeyPress()
    #     core.wait(1 / 300)

    startTime = time.time()
    # musicPause = False
    c = ''
    while (c != ['p']):
        if time.time() - startTime >= params['faceMatrixDuration']:
            break
        # GetKeyPress()
        c = event.getKeys()
        if c == ['q']:
            print('Q pressed. Forced Exit.')
            if params['musicMode'] != 'off':
                # sound1 = stopMusic(sound1)
                StopMusic()
            core.quit()

        if params['EyeLinkSupport']:
            position = tracker.getPosition()
            if position is None or type(position) == int:
                continue

        # Thresholding
        if params['EyeLinkSupport']:
            position[0] = params['screenSize'][0] if position[0] > params['screenSize'][0] else position[0]
            position[0] = -1 * params['screenSize'][0] if position[0] < -1 * params['screenSize'][0] else position[0]
            position[1] = params['screenSize'][1] if position[1] > params['screenSize'][1] else position[1]
            position[1] = -1 * params['screenSize'][1] if position[1] < -1 * params['screenSize'][1] else position[1]

        if params['EyeLinkSupport']:
            circle.pos = position
        imgStim.draw()

        if params['circle']:
            for rectangle in angryRectangles:
                rectangle.draw()
            circle.draw()

        if params['musicMode'] == 'onlyWhenStareAt':
            # eyeOnAngryFace = False
            # for rectangle in angryRectangles:
            #     if rectangle.contains(circle.pos):
            #         # sound1 = pauseMusic(sound1)
            #         PauseMusic()
            #         eyeOnAngryFace = True
            #         # musicPause = True
            eyeOnNeutralFace = False
            for rectangle in neutralRectangles:
                if rectangle.contains(circle.pos):
                    # sound1 = pauseMusic(sound1)
                    UnpauseMusic()
                    eyeOnNeutralFace = True
                    # musicPause = True
            # if not eyeOnAngryFace and musicPause:
            if not eyeOnNeutralFace:
                # UnpauseMusic()
                PauseMusic()

            # if rectangles[0].contains(circle.pos):
            #     UnpauseMusic()
            # else:
            #     PauseMusic()
        elif params['musicMode'] == 'allTheTime':
            # sound1 = playMusic(sound1,params)
            UnpauseMusic()

        win.flip()
        core.wait(1 / 100)

    if params['musicMode'] == 'onlyWhenStareAt':
        # sound1 = playMusic(sound1,params)
        UnpauseMusic()
        # resumeMusic(sound)
        # if musicPause:
        #     UnpauseMusic()
        #     musicPause = False

    # Record status
    dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Duration"] = time.time() - sectionStartTime
    dictRaw["Event"] = str(img) + " shown (end)"
    DictWriteRaw(dfRaw, dictRaw, params)
    DictWrite(df, params, dict)

    # End Eyetracker
    # Eyetracker label (end and new start)

    if params['EyeLinkSupport']:

        tracker.sendMessage('TRIAL_RESULT 0')
        tracker.sendMessage('TRIALID %d' % params["eyeIdx"])
    params["eyeIdx"] += 1

    # return sound1


