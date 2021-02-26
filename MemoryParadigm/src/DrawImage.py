
import time
from psychopy import visual,core
from DictWrite import DictWriteRaw,ResponseRecord,SectionStart,SectionEnd
from DrawButton import DrawButton
from psychopy.event import Mouse

XList = [-265,0,265]

def DrawImagePractice(df,dfRaw,params,dict,dictRaw,win,imgGroup,imgOrder,playType,answer):

    playType = "Practice"
    for i in range(len(imgOrder)):
        dict["Image Displayed #" + str(i+1)] = "./img/" + imgGroup + str(imgOrder[i]) + ".jpg"

    txt1 = visual.TextStim(win, text="Practice", height=30, bold=True,
                           units='pix', pos=[0,300], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    txt1.draw()
    imgs = []

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

        practiceCount = 0
        SectionStart(df, dfRaw, params, dict, dictRaw, "Practice try#" + str(practiceCount))

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
                        ResponseRecord(params, dict,str(userAnswer),str(answer))
                    continue
            shape1.draw()
            txt1.draw()
            for i in range(6):
                imgs[i].draw()
            win.flip()
            core.wait(1 / 300)
        SectionEnd(df, dfRaw, params, dict, dictRaw, "Practice try#" + str(practiceCount))
        practiceCount += 1

        if clicked == False or userAnswer != answer:
            SectionStart(df, dfRaw, params, dict, dictRaw, "Play Practice Again Screen")
            userAnswer = 0
            PlayAgainWarning(df,dfRaw,params,dict,dictRaw,win,playType)
            core.wait(1 / 300)
            SectionEnd(df, dfRaw, params, dict, dictRaw, "Play Practice Again Screen")
        else:
            SectionStart(df, dfRaw, params, dict, dictRaw, "Practice Success Screen")
            stims = []
            txts = []
            txts.append("Excellent!")
            txts.append("You will be asked to recall all 24 pairs.")
            txts.append("Let's start!")
            DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0, 150],"Click here to continue")
            SectionEnd(df, dfRaw, params, dict, dictRaw, "Practice Success Screen")
    win.flip()

def DrawImageTest(df,dfRaw,params,dict,dictRaw,win,imgGroup,imgOrder,playType,answer):

    playType = str(playType) + " of 24"

    for i in range(len(imgOrder)):
        dict["Image Displayed #" + str(i+1)] = "./img/" + imgGroup + str(imgOrder[i]) + ".jpg"
    txt1 = visual.TextStim(win, text=playType, height=30, bold=True,
                           units='pix', pos=[0,300], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    txt1.draw()
    imgs = []

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

    practiceCount = 0
    clicked = False
    while (not clicked):
        my_mouse = Mouse()
        clicked = False
        startTime = endTime = time.time()

        SectionStart(df, dfRaw, params, dict, dictRaw, "Test:" + playType + " (Try #" + str(practiceCount) +")")

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
                        ResponseRecord(params, dict, str(userAnswer), str(answer))
                    continue
            shape1.draw()
            txt1.draw()
            for i in range(6):
                imgs[i].draw()
            win.flip()
            core.wait(1 / 300)
        SectionEnd(df, dfRaw, params, dict, dictRaw, "Test:" + playType + "Try #" + str(practiceCount))
        practiceCount += 1

        if clicked == False:
            SectionStart(df, dfRaw, params, dict, dictRaw, "Time Out Warning Screen")
            PlayAgainWarning(df, dfRaw, params, dict, dictRaw, win, playType)
            core.wait(1 / 300)
            SectionEnd(df, dfRaw, params, dict, dictRaw, "Time Out Warning Screen")
    win.flip()

def PlayAgainWarning(df,dfRaw,params,dict,dictRaw,win,playType):
    if playType == "Practice":

        # Starting Screen
        txts = []
        txt1 = visual.TextStim(win, text="The image pair you learned was:", height=30, bold=True,
                               units='pix', pos=[0, 200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        img1 = visual.ImageStim(win=win, image=dict["Image Displayed #1"], units="pix", opacity=1,
                                size=(250, 250),
                                pos=[-128, 50])
        img2 = visual.ImageStim(win=win, image=dict["Image Displayed #2"], units="pix", opacity=1,
                                size=(250, 250),
                                pos=[128, 50])
        stims = [txt1,img1,img2]
        txts.append("You should click the image on the right.")
        DrawButton(df, dfRaw, params, dict, dictRaw,win,stims,txts,[0, -150],"Click here for instructions")
    else:
        dict["Image Displayed #1"] = params["Image Displayed #1"]
        txt1 = visual.TextStim(win, text="You are taking too long to respond.", height=30, bold=True,
                               units='pix', pos=[0, 200], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        txt2 = visual.TextStim(win, text="You should click the image that goes with this.", height=30, bold=True,
                               units='pix', pos=[0, 140], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
        img1 = visual.ImageStim(win=win, image=dict["Image Displayed #1"], units="pix", opacity=1,
                                size=(250, 250),
                                pos=[0, -40])
        stims = [txt1, txt2, img1]
        txts = [""]
        DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0, -200], "Click here to retry")
