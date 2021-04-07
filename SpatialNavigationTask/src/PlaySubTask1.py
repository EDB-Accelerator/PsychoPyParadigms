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

from psychopy import visual,core
from DictWrite import DictWriteRaw,SectionStart,SectionEnd
from DrawButton import DrawButton


def PlaySubTask1(df,dfRaw,params,dict,dictRaw,win):
    # Initialization
    dict["Section"] = "Subtask 1 Introduction"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    stims = []
    txts = []
    if dict["Language"] == "English":
        txts.append("You will see several objects. For every object, indicate "
                    "whether you saw this object in the video. The green button means you saw it, "
                    "the red button means you did not see it. Click ‘continue’ to go to the next question. ")
    else:
        txts.append("Je ziet een aantal voorwerpen. Geef voor ieder voorwerp aan of je dit hebt gezien in de video. "
                    "De groene knop voor wel gezien, de rode knop voor niet gezien. Druk op verder om naar de volgende "
                    "vraag te gaan.")

    DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0,150], "Continue")

    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])


    img = "./img/Version1/Tasks/AllocentricLocation/Q1.png"
    SelectTwoOption(df,dfRaw,params,dict,dictRaw,win,img)

