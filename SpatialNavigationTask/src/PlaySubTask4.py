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
PlayInstruction.py

This function is for displaying Instructions.

Created on Thu Feb 18 08:11:29 EST 2021

@author: Kyunghun Lee
- Created on Thu Feb 18 08:11:29 EST 2021 by KL
"""

from DictWrite import DictWriteRaw,SectionStart,SectionEnd
from DrawButton import DrawButton
from SelectTwoOption import SelectTwoOption
import random

def PlaySubTask4(df,dfRaw,params,dict,dictRaw,win,version):

    # Initialization
    dict["Section"] = "Subtask 4 Introduction"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    stims = []
    txts = []
    if dict["Language"] == "English":
        txts.append("You will see an object from the video. Where is the white spaceship (endpoint of the route) "
                    "located when you are standing at the location of this object? Choose the image with the arrow "
                    "pointing in the right direction.")
    else:
        txts.append("Je ziet steeds een voorwerp uit de video. Waar bevindt het witte ruimteschip "
                    "(eindpunt van de route) zich wanneer je bij het voorwerp bent? Kies het plaatje "
                    "met de pijl die de juiste kant op wijst.")

    DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0,150], "Continue")

    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])

    imgList = [1,2,3,4,5,6,7,8]
    if version == 1:
        answerList = ["","Left","Left","Right","Left","Right","Right","Right","Left"]
    else:
        answerList = ["", "Right", "Left", "Left", "Right", "Left", "Left", "Right", "Right"]

    # Shuffle image and select 4 images.
    random.shuffle(imgList)
    imgList = imgList[:4]

    for i in range(len(imgList)):
        imgFile = "./img/Version"+str(version)+"/Task/PathRoute/Q" + str(imgList[i]) + ".png"
        SelectTwoOption(df,dfRaw,params,dict,dictRaw,win,imgFile,["Left","Right"],30,answerList[imgList[i]])
