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
from DictWrite import DictWrite,DictWriteRaw

def PlayTest(df,dfRaw,params,dict,dictRaw,win):

    dict["Section"] = "Practice Section"

    dict["Image Displayed #1"] = "./img/example1.jpg"
    dict["Image Displayed #2"] = "./img/example2.jpg"
    dict["Image Displayed #3"] = "./img/example3.jpg"
    dict["Image Displayed #4"] = "./img/example4.jpg"
    dict["Image Displayed #5"] = "./img/example5.jpg"
    dict["Image Displayed #6"] = "./img/example6.jpg"
    DrawImage(df, dfRaw, params, dict, dictRaw, win, "Practice",1)
    win.flip()

    # DictWriteRaw(dfRaw, dictRaw, params, "Image Displayed")
    # DictWriteRaw(dfRaw, dictRaw, params, "Practice shown")
    #
    #
    #
    # imgGroup = ['barn', 'lobby', 'bath', 'temple', 'playground', 'entry', 'field', 'underwater']
    # count = 1
    # for i in range(1, 1 + 3):
    #     for j in range(len(imgGroup)):
    #
    #         txt1 = visual.TextStim(win, text=str(count) + " of 24", height=30, bold=True,
    #                                units='pix', pos=[0, 300], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    #         txt1.draw();
    #         win.flip()
    #         core.wait(1.5)
    #         imgFile1 = "./img/" + imgGroup[j] + str(i) + ".jpg"
    #         imgFile2 = "./img/" + imgGroup[j] + str(i + 3) + ".jpg"
    #
    #         # Record
    #         dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    #         startTime = time.time()
    #         DictWriteRaw(dfRaw, dictRaw, params, imgFile1 +" and " +imgFile2 + " displayed. (start)")
    #
    #         img1 = visual.ImageStim(win=win, image=imgFile1, units="pix", opacity=1,
    #                                 size=(250, 250),
    #                                 pos=[-128, 50])
    #         img2 = visual.ImageStim(win=win, image=imgFile2, units="pix", opacity=1,
    #                                 size=(250, 250),
    #                                 pos=[128, 50])
    #         txt1.draw();img1.draw();img2.draw();
    #         win.flip()
    #         core.wait(5)
    #
    #         dict["Image Displayed #1"] = imgFile1
    #         dict["Image Displayed #2"] = imgFile2
    #         dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    #         dict["Section Time"] = time.time() - startTime
    #         params["ImageCount"] = count
    #         DictWriteRaw(dfRaw, dictRaw, params, imgFile1 +" and " +imgFile2 + " displayed. (end)")
    #         DictWrite(df, params, dict)
    #         count += 1
    #
    # DictWriteRaw(dfRaw, dictRaw, params, "Test Section Ended.")

def ButtonDraw(win,stims,txts,position,buttonMessage):
    txtStims = []
    for i in range(len(txts)):
        txtStims.append(visual.TextStim(win, text=txts[i], height=30, bold=True,units='pix', pos=[position[0], position[1]-60*i], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb'))
        # txtStims[i].draw()
    imgButton = visual.ImageStim(win, image="./img/button/click1.png", units="pix", opacity=1,size=(360, 60),pos=[position[0], (txtStims[-1].pos)[1]-60])
    txtButton = visual.TextStim(win, text=buttonMessage, height=30, bold=True,
                                units='pix', pos=[position[0], (txtStims[-1].pos)[1]-60], wrapWidth=1000, color=(-1, -1, -1),
                                colorSpace='rgb',opacity=1)
    # imgButton.draw();
    # txtButton.draw();
    # DictWriteRaw(dfRaw, dictRaw, params, "Instruction shown (Play again")
    my_mouse = Mouse()
    clicked = False
    while (not clicked):
        if imgButton.contains(my_mouse):
            imgButton.image = "./img/button/click2.png"
            # txt1.draw();
            # txt2.draw()
            for i in range(len(txtStims)):
                txtStims[i].draw()
            imgButton.draw();
            txtButton.draw();
            for stim in stims:
                stim.draw()
            win.flip()
            if my_mouse.getPressed()[0] == 1:
                clicked = True
                # DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
        else:
            imgButton.image = "./img/button/click1.png"
            # txt1.draw();
            # txt2.draw()
            for i in range(len(txtStims)):
                txtStims[i].draw()
            imgButton.draw();
            txtButton.draw();
            # img1.draw();
            # img2.draw()
            for stim in stims:
                stim.draw()
            win.flip()
        core.wait(1 / 300)
    core.wait(1 / 300)

def DrawImage(df,dfRaw,params,dict,dictRaw,win,playType,answer):
    txt1 = visual.TextStim(win, text=playType, height=30, bold=True,
                           units='pix', pos=[-70, 300], wrapWidth=2, color=(-1, -1, -1), colorSpace='rgb')
    txt1.draw()
    imgs = []
    XList = [-265,0,265]
    # Image configurations.
    for i in range(6):
        imgs.append(visual.ImageStim(win=win, image=dict["Image Displayed #" + str(i+1)],
                            units="pix", opacity=1,
                            size=(250, 250),
                            pos=[XList[i%3], 135- 270*(i//3)]))

    # Draw Redblock at image #0.
    edgeLength = 250 * 0.7
    Vert = [[(-1 * edgeLength, -1 * edgeLength), (-1 * edgeLength, edgeLength),
             (edgeLength, edgeLength), (edgeLength, -1 * edgeLength)]]
    shape1 = visual.ShapeStim(win, vertices=Vert, units='pix', fillColor='red', lineWidth=0, size=.75, pos=imgs[0].pos)
    shape2 = visual.ShapeStim(win, vertices=Vert, units='pix', fillColor='red', lineWidth=0, size=.75, pos=imgs[0].pos)
    shape1.draw()

    userAnswer = 0
    while (userAnswer != answer):
        my_mouse = Mouse()
        clicked = False
        startTime = endTime = time.time()
        while (not clicked) and endTime-startTime < 10:
            endTime = time.time()
            for i in range(1,6):
                if imgs[i].contains(my_mouse):
                    shape2.pos = imgs[i].pos
                    shape2.draw()
                    if my_mouse.getPressed()[0] == 1:
                        userAnswer = i
                        clicked = True
                        DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
                    continue
            shape1.draw()
            for i in range(6):
                imgs[i].draw()
            win.flip()
            core.wait(1 / 300)
        if playType == "Practice":
            if clicked == False or userAnswer != answer:
                userAnswer = 0
                clicked = False
                PlayAgainWarning(df,dfRaw,params,dict,dictRaw,win,playType)
                core.wait(1 / 300)
            else:
                txts = []
                txts.append("Excellent!")
                txts.append("You will be asked to recall all 24 pairs.")
                txts.append("Let's start!")

                ButtonDraw(win, [], txts, [0, 50], "Click here to continue")


def PlayAgainWarning(df,dfRaw,params,dict,dictRaw,win,playType):
    my_mouse = Mouse()
    if playType == "Practice":

        # Starting Screen
        txts = []
        stims = []
        txt1 = visual.TextStim(win, text="The image pair you learned was:", height=30, bold=True,
                               units='pix', pos=[0, 200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        img1 = visual.ImageStim(win=win, image=dict["Image Displayed #1"], units="pix", opacity=1,
                                size=(250, 250),
                                pos=[-128, 50])
        img2 = visual.ImageStim(win=win, image=dict["Image Displayed #2"], units="pix", opacity=1,
                                size=(250, 250),
                                pos=[128, 50])
        stims = [txt1,img1,img2]
        # txt2 = visual.TextStim(win, text="You should click the image on the right.", height=30, bold=True,
        #                        units='pix', pos=[0, -140], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        txts.append("You should click the image on the right.")
        ButtonDraw(win,stims,txts,[0, -150],"Click here for instructions")

        # imgButton = visual.ImageStim(win=win, image="./img/button/click1.png", units="pix", opacity=1,
        #                              size=(360, 60),
        #                              pos=[0, -200])
        # txtButton = visual.TextStim(win, text="Click here for instructions", height=30, bold=True,
        #                             units='pix', pos=[0, -200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb',
        #                             opacity=1)

        # txt1.draw();txt2.draw()
        # imgButton.draw();
        # txtButton.draw();
        # img1.draw();
        # img2.draw()
        # win.flip()
        # DictWriteRaw(dfRaw, dictRaw, params, "Instruction shown (Play again")
        #
        # clicked = False
        # while (not clicked):
        #     if imgButton.contains(my_mouse):
        #         imgButton.image = "./img/button/click2.png"
        #         txt1.draw();txt2.draw()
        #         imgButton.draw();
        #         txtButton.draw();
        #         img1.draw();
        #         img2.draw()
        #         win.flip()
        #         if my_mouse.getPressed()[0] == 1:
        #             clicked = True
        #             DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
        #     else:
        #         imgButton.image = "./img/button/click1.png"
        #         txt1.draw();txt2.draw()
        #         imgButton.draw();
        #         txtButton.draw();
        #         img1.draw();
        #         img2.draw()
        #         win.flip()
        #     core.wait(1 / 300)
        # clicked = False
        # core.wait(1 / 300)

def PlayAgainWarning(df,dfRaw,params,dict,dictRaw,win,playType):
    my_mouse = Mouse()
    if playType == "Practice":

        # Starting Screen
        stims = []
        txts = []
        txt1 = visual.TextStim(win, text="The image pair you learned was:", height=30, bold=True,
                               units='pix', pos=[0, 200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        img1 = visual.ImageStim(win=win, image=dict["Image Displayed #1"], units="pix", opacity=1,
                                size=(250, 250),
                                pos=[-128, 50])
        img2 = visual.ImageStim(win=win, image=dict["Image Displayed #2"], units="pix", opacity=1,
                                size=(250, 250),
                                pos=[128, 50])
        # txt2 = visual.TextStim(win, text="You should click the image on the right.", height=30, bold=True,
        #                        units='pix', pos=[0, -140], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        # imgButton = visual.ImageStim(win=win, image="./img/button/click1.png", units="pix", opacity=1,
        #                              size=(360, 60),
        #                              pos=[0, -200])
        # txtButton = visual.TextStim(win, text="Click here for instructions", height=30, bold=True,
        #                             units='pix', pos=[0, -200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb',
        #                             opacity=1)
        stims = [txt1,img1,img2]
        txts.append("You should click the image on the right.")
        ButtonDraw(win, stims, txts, [0, -150], "Click here for instructions")

        # txt1.draw();txt2.draw()
        # imgButton.draw();
        # txtButton.draw();
        # img1.draw();
        # img2.draw()
        # win.flip()
        # DictWriteRaw(dfRaw, dictRaw, params, "Instruction shown (Play again")
        #
        # clicked = False
        # while (not clicked):
        #     if imgButton.contains(my_mouse):
        #         imgButton.image = "./img/button/click2.png"
        #         txt1.draw();txt2.draw()
        #         imgButton.draw();
        #         txtButton.draw();
        #         img1.draw();
        #         img2.draw()
        #         win.flip()
        #         if my_mouse.getPressed()[0] == 1:
        #             clicked = True
        #             DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
        #     else:
        #         imgButton.image = "./img/button/click1.png"
        #         txt1.draw();txt2.draw()
        #         imgButton.draw();
        #         txtButton.draw();
        #         img1.draw();
        #         img2.draw()
        #         win.flip()
        #     core.wait(1 / 300)
        # clicked = False
        # core.wait(1 / 300)

