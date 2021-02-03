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
import datetime,sys

# Import defined functions
sys.path.insert(1, './src')
from TableWrite import TableWrite,TableWriteRaw

def DisplayMatrix(df,dfRaw,img,params,dict,dictRaw,win):
    imgStim = visual.ImageStim(win=win, image=img, units="pix", opacity=1, size=params['screenSize'])
    imgStim.draw()
    win.flip()

    # Record status
    dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Section"] = "DisplayMatrix"
    dict["Image Displayed"] = img
    dict["Button Pressed"] = ""
    dict["Button Correct/Incorrect"] = ""
    dict["Button Response Time"] = ""
    dictRaw["Event"] = str(img) + " shown (start)"
    dfRaw = TableWriteRaw(dfRaw, dictRaw)

    # Wait for 6 seconds
    core.wait(6)

    # Record status
    dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dictRaw["Event"] = str(img) + " shown (end)"
    dfRaw = TableWriteRaw(dfRaw, dictRaw)

    return TableWrite(df,params,dict),dfRaw
