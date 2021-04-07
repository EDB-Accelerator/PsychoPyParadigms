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
SelectLanguage.py

MemoryParadigm Task Psychopy3 Sub function.

This function is for displaying Instructions.

Created on Thu Feb 18 08:11:29 EST 2021

@author: Kyunghun Lee
- Created on Thu Feb 18 08:11:29 EST 2021 by KL
"""

from psychopy import visual
from psychopy.event import Mouse
from DictWrite import DictWriteRaw,SectionStart,SectionEnd,ResponseRecord
import glob
import random

def SelectEgocenticLocation(df,dfRaw,params,dict,dictRaw,win,imgFolder):

    # Initialization
    dict["Section"] = "Image Folder Shown:" + imgFolder
    dict["User Answer"] = ""

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    # Starting Screen
    if dict["Language"] == "English":
        txt1 = visual.TextStim(win, text="In which of the following images is the arrow pointing exactly towards "
                                         "the white spaceship (endpoint of the route)? ", height=20, bold=True,
                           units='pix', pos=[0, 350], wrapWidth=800, color=(-1, -1, -1), colorSpace='rgb')
    else:
        txt1 = visual.TextStim(win, text="In welke van de onderstaande afbeeldingen wijst de pijl precies naar het "
                                         "witte ruimteschip (eindpunt van de route)?", height=20, bold=True,
                           units='pix', pos=[0, 350], wrapWidth=800, color=(-1, -1, -1), colorSpace='rgb')


    # Find image file paths.
    imgFiles = glob.glob(imgFolder+ "*.png")
    for i in range(len(imgFiles)):
        if "_0" in imgFiles[i] or "-0" in imgFiles[i]:
            rightFile = imgFiles[i]
            break

    # Shuffle image file list.
    random.shuffle(imgFiles)
    rightAnswer = imgFiles.index(rightFile)

    # Image configurations.
    edgeLength = 250 * 0.7
    Vert = [[(-1 * edgeLength, -1 * edgeLength), (-1 * edgeLength, edgeLength),
             (edgeLength, edgeLength), (edgeLength, -1 * edgeLength)]]

    imgs = []
    shapes = []
    for i in range(6):
        imgs.append(visual.ImageStim(win=win, image=imgFiles[i],
                            units="pix", opacity=1,
                            size=(250, 250),
                            pos=[-300+300*(i%3), 160-280*(i//3)]))
    # Draw Redblock at image #0.
        shapes.append(visual.ShapeStim(win, vertices=Vert, units='pix', fillColor='white', lineWidth=0, size=.75,
                                  pos=imgs[i].pos))
        shapes[i].draw()
        imgs[i].draw()
    txt1.draw()

    # Continue Button
    position = [0,-300]
    imgButton = visual.ImageStim(win, image="./img/button/click1.png", units="pix", opacity=1,size=(360, 60),
                                 pos=position)
    txtButton = visual.TextStim(win, text="Continue", height=30, bold=True,
                                units='pix', pos=position, wrapWidth=1000, color=(-1, -1, -1),
                                colorSpace='rgb',opacity=1)
    imgButton.draw()
    txtButton.draw()
    win.flip()

    my_mouse = Mouse()
    clicked = False
    while (not clicked):
        for i in range(6):
            if dict["User Answer"] == str(i):
                shapes[i].fillColor = 'red'
            else:
                shapes[i].fillColor = 'white'

        if dict["User Answer"] != "":
            imgButton.image = "./img/button/click2.png"

        for i in range(6):
            shapes[i].draw()
            imgs[i].draw()
        imgButton.draw()
        txtButton.draw()
        txt1.draw()
        win.flip()
        if my_mouse.getPressed()[0] == 1:
            if dict["User Answer"] != "" and imgButton.contains(my_mouse):
                DictWriteRaw(dfRaw, dictRaw, params, "User Answered:" + dict["User Answer"])
                ResponseRecord(params, dict, dict["User Answer"], rightAnswer)
                clicked = True

            for i in range(6):
                if imgs[i].contains(my_mouse):
                    dict["User Answer"] = str(i)
            my_mouse.getPressed()[0] = 0

    SectionEnd(df, dfRaw, params, dict, dictRaw, dict["Section"])

