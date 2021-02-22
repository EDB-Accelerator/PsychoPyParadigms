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
from psychopy.event import Mouse
from DictWrite import DictWrite,DictWriteRaw

def PlayStudy(df,dfRaw,params,dict,dictRaw,win):

    dict["Section"] = "Study Section"

    imgGroup = ['barn', 'lobby', 'bath', 'temple', 'playground', 'entry', 'field', 'underwater']
    count = 1
    for i in range(1, 1 + 3):
        for j in range(len(imgGroup)):

            txt1 = visual.TextStim(win, text=str(count) + " of 24", height=30, bold=True,
                                   units='pix', pos=[0, 300], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
            txt1.draw();
            win.flip()
            core.wait(1.5)
            imgFile1 = "./img/" + imgGroup[j] + str(i) + ".jpg"
            imgFile2 = "./img/" + imgGroup[j] + str(i + 3) + ".jpg"

            # Record
            dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
            startTime = time.time()
            DictWriteRaw(dfRaw, dictRaw, params, imgFile1 +" and " +imgFile2 + " displayed. (start)")

            img1 = visual.ImageStim(win=win, image=imgFile1, units="pix", opacity=1,
                                    size=(params['screenSize'][0] / 3, params['screenSize'][1] / 3),
                                    pos=[-150, 50])
            img2 = visual.ImageStim(win=win, image=imgFile2, units="pix", opacity=1,
                                    size=(params['screenSize'][0] / 3, params['screenSize'][1] / 3),
                                    pos=[150, 50])
            txt1.draw();img1.draw();img2.draw();
            win.flip()
            core.wait(5)

            dict["Image Displayed #1"] = imgFile1
            dict["Image Displayed #2"] = imgFile2
            dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
            dict["Section Time"] = time.time() - startTime
            params["ImageCount"] = count
            DictWriteRaw(dfRaw, dictRaw, params, imgFile1 +" and " +imgFile2 + " displayed. (end)")
            DictWrite(df, params, dict)
            count += 1

    # Second Screen
    txt1 = visual.TextStim(win, text="You will be tested",
                           height=27,
                           units='pix', pos=[0, 60], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    txt2 = visual.TextStim(win, text="on these image pairs shortly.",
                           height=27,
                           units='pix', pos=[0, 30], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')
    txt3 = visual.TextStim(win, text="But first, let's do some other tests!",
                           height=27,
                           units='pix', pos=[0, 0], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb')

    imgButton = visual.ImageStim(win=win, image="./img/button/click1.png", units="pix", opacity=1,
                                 size=(360, 60),
                                 pos=[0, -100])
    txtButton = visual.TextStim(win, text="Click here to continue", height=30, bold=True,
                                units='pix', pos=[0, -100], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb',
                                opacity=1)

    # Last Screen
    my_mouse = Mouse()
    txt1.draw()
    txt2.draw()
    txt3.draw()
    imgButton.draw()
    txtButton.draw()
    win.flip()
    DictWriteRaw(dfRaw, dictRaw, params, "Last screen (at Study Section) displayed.")

    clicked = False
    while not clicked:
        if imgButton.contains(my_mouse):
            imgButton.image = "./img/button/click2.png"
            txt1.draw()
            txt2.draw()
            txt3.draw()
            imgButton.draw()
            txtButton.draw()
            win.flip()
            if my_mouse.getPressed()[0] == 1:
                clicked = True
                DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
        else:
            imgButton.image = "./img/button/click1.png"
            txt1.draw()
            txt2.draw()
            txt3.draw()
            imgButton.draw()
            txtButton.draw()
            win.flip()
        core.wait(1 / 300)

    DictWriteRaw(dfRaw, dictRaw, params, "Study Section Ended.")
