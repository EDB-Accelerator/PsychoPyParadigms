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

from psychopy import visual
from psychopy.event import Mouse
from DictWrite import DictWriteRaw,SectionStart,SectionEnd,ResponseRecord

def SelectFourOption(df,dfRaw,params,dict,dictRaw,win,question,answerOption):

    # Initialization
    dict["Section"] = "Question shown:" + question
    dict["User Answer"] = ""

    edgeLength = 40 * 0.74
    Vert1 = [[(-7 * edgeLength, -1 * edgeLength), (-7 * edgeLength, 1* edgeLength),
              (7*edgeLength, 1 * edgeLength), (7*edgeLength, -1 * edgeLength)]]

    edgeLength = 40 * 0.76
    Vert2 = [[(-7 * edgeLength, -1 * edgeLength), (-7 * edgeLength, 1 * edgeLength),
             (7*edgeLength, 1 * edgeLength), (7*edgeLength, -1 * edgeLength)]]

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    # Starting Screen
    txt = visual.TextStim(win, text=question, height=30, bold=True,
                           units='pix', pos=[0, 300], wrapWidth=800, color=(-1, -1, -1), colorSpace='rgb')

    opts = []
    shapes1 = []
    shapes2 = []
    for i in range(len(answerOption)):
        opt = visual.TextStim(win, text=answerOption[i], height=30, bold=True,
                        units='pix', pos=[0,150-i*100], wrapWidth=1000,
                        color=(-1, -1, -1),
                        colorSpace='rgb', opacity=1)

        shape1 = visual.ShapeStim(win, vertices=Vert1, units='pix', fillColor='white', lineWidth=0, size=.75,
                                   pos=[0,150-i*100])
        shape2 = visual.ShapeStim(win, vertices=Vert2, units='pix', fillColor='black', lineWidth=0, size=.75,
                                   pos=[0,150-i*100])

        opts.append(opt)
        shapes1.append(shape1)
        shapes2.append(shape2)

    position = [0,-300]
    imgButton = visual.ImageStim(win, image="./img/button/click1.png", units="pix", opacity=1,size=(360, 60),
                                 pos=position)
    txtButton = visual.TextStim(win, text="Continue", height=30, bold=True,
                                units='pix', pos=position, wrapWidth=1000, color=(-1, -1, -1),
                                colorSpace='rgb',opacity=1)

    my_mouse = Mouse()
    clicked = False
    while (not clicked):
        for i in range(len(opts)):
            if dict["User Answer"] == answerOption[i]:
                shapes1[i].fillColor = 'yellow'
            else:
                shapes1[i].fillColor = 'white'

        if dict["User Answer"] != "":
            imgButton.image = "./img/button/click2.png"

        for i in range(len(opts)):
            shapes2[i].draw()
            shapes1[i].draw()
            opts[i].draw()
        imgButton.draw()
        txtButton.draw()
        txt.draw()
        win.flip()
        if my_mouse.getPressed()[0] == 1:
            if dict["User Answer"] != "" and imgButton.contains(my_mouse):
                DictWriteRaw(dfRaw, dictRaw, params, "User Answered:" + dict["User Answer"])
                ResponseRecord(params, dict, dict["User Answer"], "")
                clicked = True

            for i in range(len(opts)):
                if opts[i].contains(my_mouse):
                    dict["User Answer"] = answerOption[i]
            my_mouse.getPressed()[0] = 0

    SectionEnd(df, dfRaw, params, dict, dictRaw, dict["Section"])


