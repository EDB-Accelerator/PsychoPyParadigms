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

MemoryParadigm Task Psychopy3 Sub function.

This function is for displaying Instructions.

Created on Thu Feb 18 08:11:29 EST 2021

@author: Kyunghun Lee
- Created on Thu Feb 18 08:11:29 EST 2021 by KL
"""

from psychopy import visual,core
import time,datetime
from psychopy.event import Mouse
from DictWrite import DictWrite,DictWriteRaw

# Output Summary Header Initialization
# Header = ["SubjectID","Session","Section","Section Start Time","Section End Time","Section Time","ImageCount",
#           "Image Displayed #1","Image Displayed #2"]

# Output Raw Header Initialization
# HeaderRaw = ["TimeStamp","expName","subjectID","Session","Event"]

def PlayInstruction(df,dfRaw,params,dict,dictRaw,win,fType):
    # Initialization
    dict["Section"] = "Instruction"
    startTime = time.time()
    dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Image Displayed #1"] = "./img/example1.jpg"
    dict["Image Displayed #2"] = "./img/example2.jpg"

    my_mouse = Mouse()

    # Starting Screen
    txt1 = visual.TextStim(win, text="Image Pairs Test", height=40, bold=True,
                           units='pix', pos=[0, 200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    img1 = visual.ImageStim(win=win, image=dict["Image Displayed #1"], units="pix", opacity=1,
                            size=(250, 250),
                            pos=[-128, 50])
    img2 = visual.ImageStim(win=win, image=dict["Image Displayed #2"], units="pix", opacity=1,
                            size=(250, 250),
                            pos=[128, 50])
    imgButton = visual.ImageStim(win=win, image="./img/button/click1.png", units="pix", opacity=1,
                                 size=(360, 60),
                                 pos=[0, -180])
    txtButton = visual.TextStim(win, text="Click here for instructions", height=30, bold=True,
                                units='pix', pos=[0, -180], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb',
                                opacity=1)

    txt1.draw();imgButton.draw();txtButton.draw();img1.draw();img2.draw()
    win.flip()
    DictWriteRaw(dfRaw, dictRaw, params, "Instruction shown (Image Pairs Test Instruction)")

    clicked = False
    while not clicked:
        if imgButton.contains(my_mouse):
            imgButton.image = "./img/button/click2.png"
            txt1.draw();
            imgButton.draw();
            txtButton.draw();
            img1.draw();
            img2.draw()
            win.flip()
            if my_mouse.getPressed()[0] == 1:
                clicked = True
                DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
        else:
            imgButton.image = "./img/button/click1.png"
            txt1.draw();
            imgButton.draw();
            txtButton.draw();
            img1.draw();
            img2.draw()
            win.flip()
        core.wait(1 / 300)

    # Second Screen
    DictWriteRaw(dfRaw, dictRaw, params, "Instruction shown (Actual Instruction Screen)")
    txt1 = visual.TextStim(win, text="Instructions:", height=30, bold=True,
                           units='pix', pos=[-70, 250], wrapWidth=2, color=(-1, -1, -1), colorSpace='rgb')
    img1 = visual.ImageStim(win=win, image="./img/example1.jpg", units="pix", opacity=1,
                            size=(250, 250),
                            pos=[-128, 50])
    img2 = visual.ImageStim(win=win, image="./img/example2.jpg", units="pix", opacity=1,
                            size=(250, 250),
                            pos=[128, 50])


    txt1.draw();img1.draw();img2.draw();imgButton.draw();txtButton.draw()
    if fType == 'Study':
        txt2 = visual.TextStim(win, text="You will see 24 image pairs, like above.",
                               height=27,
                               units='pix', pos=[0, -140], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        txt3 = visual.TextStim(win, text="Learn which images go together.",
                               height=27,
                               units='pix', pos=[0, -170], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        txt4 = visual.TextStim(win, text="Later you will be tested on that!",
                               height=27,
                               units='pix', pos=[0, -200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        imgButton = visual.ImageStim(win=win, image="./img/button/click1.png", units="pix", opacity=1,
                                     size=(360, 60),
                                     pos=[0, -300])
        txtButton = visual.TextStim(win, text="Click here to continue", height=30, bold=True,
                                    units='pix', pos=[0, -300], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb',
                                    opacity=1)

    elif fType == 'Test':
        DictWriteRaw(dfRaw, dictRaw, params, "Instruction shown (Actual Instruction Screen)")
        txt2 = visual.TextStim(win, text="Let's test your memory for the images",
                               height=27,
                               units='pix', pos=[0, -140], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        txt3 = visual.TextStim(win, text="you learned a few minutes ago.",
                               height=27,
                               units='pix', pos=[0, -170], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        imgButton = visual.ImageStim(win=win, image="./img/button/click1.png", units="pix", opacity=1,
                                     size=(360, 60),
                                     pos=[0, -250])
        txtButton = visual.TextStim(win, text="Click here to continue", height=30, bold=True,
                                    units='pix', pos=[0, -250], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb',
                                    opacity=1)

    txt2.draw()
    txt3.draw()
    if fType == 'Study':
        txt4.draw()

    win.flip()
    my_mouse = Mouse()
    clicked = False
    while not clicked:
        if imgButton.contains(my_mouse):
            imgButton.image = "./img/button/click2.png"
            txt1.draw()
            txt2.draw()
            txt3.draw()
            if fType == 'Study':
                txt4.draw()
            imgButton.draw()
            txtButton.draw()
            img1.draw()
            img2.draw()
            win.flip()
            if my_mouse.getPressed()[0] == 1:
                DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
                clicked = True
        else:
            imgButton.image = "./img/button/click1.png"
            txt1.draw()
            txt2.draw()
            txt3.draw()
            if fType == 'Study':
                txt4.draw()
            imgButton.draw()
            txtButton.draw()
            img1.draw()
            img2.draw()
            win.flip()
        core.wait(1 / 300)

    clicked = False
    while not clicked:
        if my_mouse.getPressed():
            clicked = True

# Last screen (only test case)
    if fType == "Test":
        DictWriteRaw(dfRaw, dictRaw, params, "Instruction shown (Third screen)")
        txt1 = visual.TextStim(win, text="Instructions:", height=30, bold=True,
                               units='pix', pos=[-70, 250], wrapWidth=2, color=(-1, -1, -1), colorSpace='rgb')
        # lines are ok; use closeShape=False
        edgeLength = 250 * 0.7
        Vert = [[(-1*edgeLength, -1*edgeLength), (-1*edgeLength, edgeLength),
                      (edgeLength, edgeLength), (edgeLength, -1*edgeLength)]]
        shape1 = visual.ShapeStim(win, vertices=Vert, units='pix',fillColor='red', lineWidth=0, size=.75, pos=[0, 50])
        img1 = visual.ImageStim(win=win, image="./img/example1.jpg", units="pix", opacity=1,
                                size=(250, 250),
                                pos=[0, 50])

        txt2 = visual.TextStim(win, text="For practice, click the image",
                               height=27,
                               units='pix', pos=[0, -140], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        txt3 = visual.TextStim(win, text="that goes together with this.",
                               height=27,
                               units='pix', pos=[0, -170], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        txt4 = visual.TextStim(win, text="(hint: it's a bridge!)",
                               height=27,
                               units='pix', pos=[0, -200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        imgButton = visual.ImageStim(win=win, image="./img/button/click1.png", units="pix", opacity=1,
                                     size=(360, 60),
                                     pos=[0, -300])
        txtButton = visual.TextStim(win, text="Click here to continue", height=30, bold=True,
                                    units='pix', pos=[0, -300], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb',
                                    opacity=1)
        txt1.draw();
        txt2.draw()
        txt3.draw()
        txt4.draw()
        shape1.draw()
        img1.draw()
        win.flip()

        my_mouse = Mouse()
        clicked = False
        while not clicked:
            if imgButton.contains(my_mouse):
                imgButton.image = "./img/button/click2.png"
                txt1.draw();txt2.draw();txt3.draw();txt4.draw()
                imgButton.draw();txtButton.draw()
                shape1.draw();img1.draw()
                win.flip()
                if my_mouse.getPressed()[0] == 1:
                    DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
                    clicked = True
            else:
                imgButton.image = "./img/button/click1.png"
                txt1.draw();txt2.draw();txt3.draw();txt4.draw()
                imgButton.draw();txtButton.draw()
                shape1.draw();img1.draw()
                win.flip()
            core.wait(1 / 300)

        clicked = False
        while not clicked:
            if my_mouse.getPressed():
                clicked = True

    # Record the result.
    dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Section Time"] = time.time() - startTime
    params["ImageCount"] = ""
    DictWriteRaw(dfRaw, dictRaw, params,"Instruction End")
    DictWrite(df, params, dict)
