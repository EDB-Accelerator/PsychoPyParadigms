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

def SelectTwoClosestImages(df,dfRaw,params,dict,dictRaw,win,imgFolder,rightAnswer):

    # Initialization
    dict["Section"] = "Image Folder Shown:" + imgFolder
    dict["User Answer"] = ""

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    # Starting Screen
    if dict["Language"] == "English":
        txt1 = visual.TextStim(win, text="Selecteer de twee voorwerpen die het dichtst bij elkaar liggen:", height=20, bold=True,
                           units='pix', pos=[0, 350], wrapWidth=800, color=(-1, -1, -1), colorSpace='rgb')
    else:
        txt1 = visual.TextStim(win, text="Select the two objects that were closest together:", height=20, bold=True,
                           units='pix', pos=[0, 350], wrapWidth=800, color=(-1, -1, -1), colorSpace='rgb')

    # Find image file paths.
    imgFiles = glob.glob(imgFolder+ "*.png")

    # Shuffle image file list.
    random.shuffle(imgFiles)
    imgIndex = []
    for i in range(len(imgFiles)):
        imgIndex.append(int(imgFiles[i].split('/')[-1].split('.png')[0]))

    # Image configurations.
    edgeLength = 280 * 0.7
    Vert = [[(-1 * edgeLength, -1 * edgeLength), (-1 * edgeLength, edgeLength),
             (edgeLength, edgeLength), (edgeLength, -1 * edgeLength)]]

    imgs = []
    shapes = []
    for i in range(len(imgFiles)):
        imgs.append(visual.ImageStim(win=win, image=imgFiles[i],
                            units="pix", opacity=1,
                            size=(280, 280),
                            pos=[-300+300*(i%3), 0]))
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

    my_mouse = Mouse()
    clicked = False
    while (not clicked):
        for i in range(len(imgFiles)):
            if str(imgIndex[i]) in dict["User Answer"]:
                shapes[i].fillColor = 'red'
            else:
                shapes[i].fillColor = 'white'

        if dict["User Answer"] != "":
            imgButton.image = "./img/button/click2.png"

        for i in range(len(imgFiles)):
            shapes[i].draw()
            imgs[i].draw()
        imgButton.draw()
        txtButton.draw()
        txt1.draw()
        win.flip()
        if my_mouse.getPressed()[0] == 1:
            if len(dict["User Answer"]) == 3 and imgButton.contains(my_mouse):
                DictWriteRaw(dfRaw, dictRaw, params, "User Answered:" + dict["User Answer"])

                # Sort Answer
                num1 = int(dict["User Answer"][0])
                num2 = int(dict["User Answer"][-1])
                if num1 < num2:
                    dict["User Answer"] = str(num1) + ',' + str(num2)
                else:
                    dict["User Answer"] = str(num2) + ',' + str(num1)

                ResponseRecord(params, dict, dict["User Answer"], rightAnswer)
                clicked = True

            for i in range(len(imgFiles)):
                if imgs[i].contains(my_mouse):
                    if len(dict["User Answer"]) == 0:
                        dict["User Answer"] = str(imgIndex[i])
                    elif len(dict["User Answer"]) == 1 and str(imgIndex[i]) not in dict["User Answer"]:
                        dict["User Answer"] += ',' + str(imgIndex[i])
                    else:
                        if str(imgIndex[i]) not in dict["User Answer"]:
                            dict["User Answer"] = dict["User Answer"][-1]
                            dict["User Answer"] += ',' + str(imgIndex[i])

            my_mouse.getPressed()[0] = 0

    SectionEnd(df, dfRaw, params, dict, dictRaw, dict["Section"])

