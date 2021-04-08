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
from SelectTwoClosestImages import SelectTwoClosestImages
import random

def PlaySubTask5(df,dfRaw,params,dict,dictRaw,win,version):

    # Initialization
    dict["Section"] = "Subtask 5 Introduction"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    stims = []
    txts = []
    if dict["Language"] == "English":
        txts.append("You will now see three objects from the video. Two of these objects are closest together "
                    "(as the crow flies). Click on these two objects.")
    else:
        txts.append("Je ziet nu steeds 3 voorwerpen uit de video. Twee van deze voorwerpen liggen het dichtst "
                    "(hemelsbreed) bij elkaar . Klik op deze twee voorwerpen.")

    DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0,150], "Continue")

    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])

    imgList = [1,2,3,4]
    version = 1
    if version == 1:
        answerList = ["4,6","3,5","6,7","7,8"]
    else:
        answerList = ["3,4", "3,5", "6,7", "7,8"]

    # Shuffle image and select 4 images.
    random.shuffle(imgList)

    for i in range(len(imgList)):
        imgFolder = "./img/Version"+str(version)+"/Task/PathSurvey/Q" + str(imgList[i]) + "/"
        rightAnswer = answerList[imgList[i]]
        SelectTwoClosestImages(df,dfRaw,params,dict,dictRaw,win,imgFolder,rightAnswer)
