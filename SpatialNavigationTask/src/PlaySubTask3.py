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

from DictWrite import DictWriteRaw,SectionStart,SectionEnd
from DrawButton import DrawButton
from SelectLocation import SelectLocation
import random

def PlaySubTask3(df,dfRaw,params,dict,dictRaw,win,version):

    # Initialization
    dict["Section"] = "Subtask 3 Introduction"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    stims = []
    txts = []
    if dict["Language"] == "English":
        txts.append("You will see an object from the video and a map of the environment. "
                    "Indicate on the map where you saw this object. Pick one of the four possible locations. ")
    else:
        txts.append("Je ziet een voorwerp uit de video en een plattegrond van de omgeving. Geef op de plattegrond "
                    "aan waar je dit voorwerp bent tegengekomen. Kies een van de vier mogelijke locaties.")

    DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0,150], "Continue")

    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])

    imgList = [1,2,3,4,5,6,7,8]
    if version == 1:
        answerList = ["", "C", "B", "D", "B", "D", "C", "D", "B"]
    else:
        answerList = ["", "B", "C", "D", "A", "B", "C", "D", "A"]

    # Shuffle image and select 4 images.
    random.shuffle(imgList)
    imgList = imgList[:4]

    for i in range(len(imgList)):
        imgFile = "./img/Version"+str(version)+"/Task/AllocentricLocation/Q" + str(imgList[i]) + "_LM.png"
        mapFile = "./img/Version"+str(version)+"/Task/AllocentricLocation/Q" + str(imgList[i]) + ".png"
        SelectLocation(df,dfRaw,params,dict,dictRaw,win,imgFile,mapFile,answerList[imgList[i]])
