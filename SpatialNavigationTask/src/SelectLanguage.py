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

from psychopy import visual,core
from psychopy.event import Mouse
from DictWrite import DictWriteRaw,SectionStart,SectionEnd,ResponseRecord

def SelectLanguage(df,dfRaw,params,dict,dictRaw,win):
    # Initialization
    dict["Section"] = "Select Language"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])
    txt1 = visual.TextStim(win, text="Please select language.", height=40, bold=True,
                           units='pix', pos=[0, 200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')

    img1 = visual.TextStim(win, text="English", height=30, bold=True,
                    units='pix', pos=[-150,-50], wrapWidth=1000,
                    color=(-1, -1, -1),
                    colorSpace='rgb', opacity=1)
    img2 = visual.TextStim(win, text="Dutch", height=30, bold=True,
                    units='pix', pos=[150,-50], wrapWidth=1000,
                    color=(-1, -1, -1),
                    colorSpace='rgb', opacity=1)

    edgeLength = 100 * 0.74
    Vert = [[(-1 * edgeLength, -0.7 * edgeLength), (-1 * edgeLength, 0.7 * edgeLength),
             (edgeLength, 0.7 * edgeLength), (edgeLength, -0.7 * edgeLength)]]

    shape1 = visual.ShapeStim(win, vertices=Vert, units='pix', fillColor='white', lineWidth=0, size=.75, pos=[-150,-50])
    shape3 = visual.ShapeStim(win, vertices=Vert, units='pix', fillColor='white', lineWidth=0, size=.75, pos=[150,-50])

    edgeLength = 100 * 0.76
    Vert = [[(-1 * edgeLength, -0.7 * edgeLength), (-1 * edgeLength, 0.7 * edgeLength),
             (edgeLength, 0.7 * edgeLength), (edgeLength, -0.7 * edgeLength)]]

    shape2 = visual.ShapeStim(win, vertices=Vert, units='pix', fillColor='black', lineWidth=0, size=.75, pos=[-150,-50])
    shape4 = visual.ShapeStim(win, vertices=Vert, units='pix', fillColor='black', lineWidth=0, size=.75, pos=[150,-50])

    my_mouse = Mouse()
    clicked = False
    while (not clicked):
        if img1.contains(my_mouse):
            shape1.fillColor = 'yellow'
        else:
            shape1.fillColor = 'white'

        if img2.contains(my_mouse):
            shape3.fillColor = 'yellow'
        else:
            shape3.fillColor = 'white'

        shape2.draw()
        shape1.draw()
        shape4.draw()
        shape3.draw()
        txt1.draw()
        img1.draw()
        img2.draw()
        win.flip()
        if my_mouse.getPressed()[0] == 1:
            if img1.contains(my_mouse) or img2.contains(my_mouse):
                clicked = True

                if img1.contains(my_mouse):
                    dict["Language"] = "English"
                elif img2.contains(my_mouse):
                    dict["Language"] = "Dutch"
                DictWriteRaw(dfRaw, dictRaw, params, "Language selected:" + dict["Language"])
                ResponseRecord(params, dict,"Language selected:" + dict["Language"],"")
        # core.wait(1 / 300)
    core.wait(1 / 300)

    SectionEnd(df, dfRaw, params, dict, dictRaw, dict["Section"])


