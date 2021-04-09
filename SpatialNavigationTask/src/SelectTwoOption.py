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

def SelectTwoOption(df,dfRaw,params,dict,dictRaw,win,img,answerOption,answerOptionSize,rightAnswer):

    # Initialization
    dict["Section"] = "Image shown: " + img
    dict["User Answer"] = ""

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    # Starting Screen
    if dict["Language"] == "English":
        txt1 = visual.TextStim(win, text="In which direction did the route continue?", height=20, bold=True,
                           units='pix', pos=[0, 350], wrapWidth=800, color=(-1, -1, -1), colorSpace='rgb')
    else:
        txt1 = visual.TextStim(win, text="Welke kant ben je hier op gegaan?", height=20, bold=True,
                           units='pix', pos=[0, 350], wrapWidth=800, color=(-1, -1, -1), colorSpace='rgb')


    img = visual.ImageStim(win=win, image=img, units="pix", opacity=1,
                            size=(250, 250),
                            pos=[0, 150])

    opt1 = visual.TextStim(win, text=answerOption[0], height=answerOptionSize, bold=True,
                    units='pix', pos=[-150,-50], wrapWidth=1000,
                    color=(-1, -1, -1),
                    colorSpace='rgb', opacity=1)
    opt2 = visual.TextStim(win, text=answerOption[1], height=answerOptionSize, bold=True,
                    units='pix', pos=[150,-50], wrapWidth=1000,
                    color=(-1, -1, -1),
                    colorSpace='rgb', opacity=1)

    position = [0,-200]
    imgButton = visual.ImageStim(win, image="./img/button/click1.png", units="pix", opacity=1,size=(360, 60),
                                 pos=position)
    txtButton = visual.TextStim(win, text="Continue", height=30, bold=True,
                                units='pix', pos=position, wrapWidth=1000, color=(-1, -1, -1),
                                colorSpace='rgb',opacity=1)

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
        if (opt1.contains(my_mouse) or dict["User Answer"] == answerOption[0]) and dict["User Answer"] != answerOption[1]:
            shape1.fillColor = 'yellow'
            shape3.fillColor = 'white'
        else:
            shape1.fillColor = 'white'

        if (opt2.contains(my_mouse) or dict["User Answer"] == answerOption[1]) and dict["User Answer"] != answerOption[0]:
            shape3.fillColor = 'yellow'
            shape1.fillColor = 'white'
        else:
            shape3.fillColor = 'white'

        if dict["User Answer"] == answerOption[0] or dict["User Answer"] == answerOption[1]:
            imgButton.image = "./img/button/click2.png"

        txt1.draw()
        shape2.draw()
        shape1.draw()
        shape4.draw()
        shape3.draw()
        imgButton.draw()
        txtButton.draw()
        img.draw()
        opt1.draw()
        opt2.draw()
        win.flip()
        if my_mouse.getPressed()[0] == 1:
            if (dict["User Answer"] == answerOption[0] or dict["User Answer"] == answerOption[1]) and imgButton.contains(my_mouse):
                DictWriteRaw(dfRaw, dictRaw, params, "User Answered:" + dict["User Answer"])
                ResponseRecord(params, dict, dict["User Answer"], rightAnswer)
                clicked = True

            if opt1.contains(my_mouse) or opt2.contains(my_mouse):
                if opt1.contains(my_mouse):
                    dict["User Answer"] = answerOption[0]
                elif opt2.contains(my_mouse):
                    dict["User Answer"] = answerOption[1]

                my_mouse.getPressed()[0] = 0

        # core.wait(1 / 300)
    # core.wait(1 / 300)

    SectionEnd(df, dfRaw, params, dict, dictRaw, dict["Section"])


