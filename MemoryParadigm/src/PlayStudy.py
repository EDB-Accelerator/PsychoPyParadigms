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
PlayStudy.py

MemoryParadigm Task Psychopy3 Sub function.

This function is for displaying Study section.

Created on Thu Feb 18 14:28:39 EST 2021

@author: Kyunghun Lee
- Created on Thu Feb 18 14:28:39 EST 2021 by KL
"""

from psychopy import visual,core
import time,datetime
from DictWrite import SectionStart,SectionEnd,DictWriteRaw
from DrawButton import DrawButton

def PlayStudy(df,dfRaw,params,dict,dictRaw,win):

    imgGroup = ['barn', 'lobby', 'bath', 'temple', 'playground', 'entry', 'field', 'underwater']
    count = 1
    for i in range(1, 1 + 3):
        for j in range(len(imgGroup)):

            txt1 = visual.TextStim(win, text=str(count) + " of 24", height=30, bold=True,
                                   units='pix', pos=[0, 300], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
            txt1.draw();
            win.flip()
            core.wait(1.5)

            dict["Image Displayed #1"] =  "./img/" + imgGroup[j] + str(i) + ".jpg"
            dict["Image Displayed #2"] = "./img/" + imgGroup[j] + str(i + 3) + ".jpg"
            SectionStart(df, dfRaw, params, dict, dictRaw, "Study")

            img1 = visual.ImageStim(win=win, image=dict["Image Displayed #1"], units="pix", opacity=1,
                                    size=(250, 250),
                                    pos=[-128, 50])
            img2 = visual.ImageStim(win=win, image=dict["Image Displayed #2"], units="pix", opacity=1,
                                    size=(250, 250),
                                    pos=[128, 50])
            txt1.draw();img1.draw();img2.draw();
            win.flip()
            core.wait(5)
            SectionEnd(df, dfRaw, params, dict, dictRaw, "Study")
            count += 1

    # Second Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, "Instruction (last screen)")
    txt1 = visual.TextStim(win, text="You will be tested",
                           height=27,
                           units='pix', pos=[0, 60], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    txt2 = visual.TextStim(win, text="on these image pairs shortly.",
                           height=27,
                           units='pix', pos=[0, 30], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    txt3 = visual.TextStim(win, text="But first, let's do some other tests!",
                           height=27,
                           units='pix', pos=[0, 0], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    stims = [txt1,txt2,txt3]
    DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, [""], [0, -200], "Click here to continue")
    SectionEnd(df, dfRaw, params, dict, dictRaw, "Instruction (last screen)")
