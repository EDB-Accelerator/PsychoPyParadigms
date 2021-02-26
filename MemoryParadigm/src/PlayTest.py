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
PlayTest.py

MemoryParadigm Task Psychopy3 Sub function.

This function is for displaying Test section.

Created on Tue Feb 23 15:59:05 EST 2021

@author: Kyunghun Lee
- Created on Tue Feb 23 15:59:05 EST 2021 by KL
"""

from psychopy import visual,core
import time,datetime
from psychopy.event import Mouse
from DictWrite import SectionStart,SectionEnd,DictWriteRaw
from DrawButton import DrawButton
from DrawImage import DrawImageTest,DrawImagePractice

def PlayTest(df,dfRaw,params,dict,dictRaw,win):
    # Practice Section
    # dict["Section"] = "Practice"
    DrawImagePractice(df, dfRaw, params, dict, dictRaw, win,"example",[1,2,3,4,5,6],"Practice",1)
    # SectionEnd(df, dfRaw, params, dict, dictRaw, "Practice")

    # Test
    dict["Section"] = "Test"
    imgGroup = ['barn', 'lobby', 'bath', 'temple', 'playground', 'entry', 'field', 'underwater']
    imgOrders = [
        [1, 6, 7, 4, 5, 8],
        [1, 7, 8, 5, 6, 4],
        [1, 5, 8, 4, 6, 7],
        [1, 8, 6, 5, 4, 7],
        [1, 5, 4, 8, 7, 6],
        [1, 8, 5, 6, 4, 3],
        [1, 6, 8, 5, 7, 4],
        [1, 5, 4, 7, 6, 8],
    ]
    for i in range(24):
        imgOrder = imgOrders[i%8]
        if i>=8:
            imgOrder[0] += 1
        DrawImageTest(df, dfRaw, params, dict, dictRaw, win, imgGroup[i%8], imgOrder, i+1, 1);
        core.wait(0.5)




