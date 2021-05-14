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

from psychopy import visual,core
import datetime,sys,time
from GetKeyPress import GetKeyPress

# Import defined functions
sys.path.insert(1, './src')
from DictWrite import DictWrite,DictWriteRaw

def DisplayMatrix(df,dfRaw,img,params,dict,dictRaw,win,tracker):

    imgStim = visual.ImageStim(win=win, image=img, units="pix", opacity=1, size=(params['screenSize'][1],params['screenSize'][1]))
    imgStim.draw()
    circle = visual.Circle(win=win, units="pix", fillColor='black', lineColor='white', edges=1000, pos=(0,0),
                           radius=10)
    if params['circle']:
        circle.draw()
    win.flip()

    # Send message Eyetracker
    faceLocations =  params['faceLocations']

    for i in range(len(faceLocations)):
        x1, y1, x2, y2 = faceLocations[i][0], faceLocations[i][1], faceLocations[i][2], faceLocations[i][3]
        tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (i, x1, y1, x2, y2, 'Face' + str(i)))

    resolution = params['screenSize']
    tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (
        "./img/FixationCross/blank.jpg", resolution[0] / 2, resolution[1] / 2, resolution[0], resolution[1]))
    # tk.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % ('img/Anger-Neutral/6N-10A/block1matrix1.jpeg', resolution[0]/2,resolution[1]/2,resolution[1],resolution[1]))

    # tk.sendMessage('!V IMGLOAD TOP_LEFT %s %d %d %d %d' % (
    # "./img/FixationCross/blank.jpg", 0,0,resolution[0], resolution[1]))
    # tk.sendMessage('!V IMGLOAD TOP_LEFT %s %d %d %d %d' % ('img/Anger-Neutral/6N-10A/block1matrix1.jpeg', 0,0,resolution[1],resolution[1]))
    tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (
    img, resolution[0] / 2, resolution[1] / 2, resolution[1], resolution[1]))

    # Record status
    dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Section"] = "DisplayMatrix"
    dict["Image Displayed"] = img
    dict["Button Pressed"] = ""
    dict["Button Correct/Incorrect"] = ""
    dict["Button Response Time"] = ""
    dictRaw["Event"] = str(img) + " shown (start)"
    # dfRaw = TableWriteRaw(dfRaw, dictRaw)
    DictWriteRaw(dfRaw, dictRaw, params)

    # Wait for 6 seconds
    # startTime = time.time()
    # while (time.time() - startTime < 6):
    #     GetKeyPress()
    #     core.wait(1 / 300)

    startTime = time.time()
    while (time.time() - startTime < 6):
        GetKeyPress()
        position = tracker.getPosition()
        if position is None or type(position) == int:
            continue

        # Thresholding
        position[0] = params['screenSize'][0] if position[0] > params['screenSize'][0] else position[0]
        position[0] = -1 * params['screenSize'][0] if position[0] < -1 * params['screenSize'][0] else position[0]
        position[1] = params['screenSize'][1] if position[1] > params['screenSize'][1] else position[1]
        position[1] = -1 * params['screenSize'][1] if position[1] < -1 * params['screenSize'][1] else position[1]

        circle.pos = position
        imgStim.draw()
        if params['circle']:
            circle.draw()
        win.flip()
        core.wait(1 / 300)

    # Record status
    dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dictRaw["Event"] = str(img) + " shown (end)"
    DictWriteRaw(dfRaw, dictRaw, params)
    DictWrite(df, params, dict)

    # End Eyetracker
    # Eyetracker label (end and new start)
    tracker.sendMessage('TRIAL_RESULT 0')
    tracker.sendMessage('TRIALID %d' % params["eyeIdx"])
    params["eyeIdx"] += 1
