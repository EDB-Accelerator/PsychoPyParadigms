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
DrawButton.py

MemoryParadigm Task Psychopy3 Sub function.

This function is for displaying button to continue.

Created on Thu Feb 25 13:46:31 EST 2021

@author: Kyunghun Lee
- Created on Thu Feb 25 13:46:31 EST 2021 by KL
"""

from psychopy import visual,core
from DictWrite import DictWriteRaw,ResponseRecord
from psychopy.event import Mouse

def DrawButton(df, dfRaw, params, dict, dictRaw,win,stims,txts,position,buttonMessage):
    txtStims = []
    for i in range(len(txts)):
        txtStims.append(visual.TextStim(win, text=txts[i], height=30, bold=True,units='pix',
                                        pos=[position[0], position[1]-60*i], wrapWidth=1000, color=(-1, -1, -1), colorSpace='rgb'))

    imgButton = visual.ImageStim(win, image="./img/button/click1.png", units="pix", opacity=1,size=(360, 60),
                                 pos=[position[0], (txtStims[-1].pos)[1]-60])
    txtButton = visual.TextStim(win, text=buttonMessage, height=30, bold=True,
                                units='pix', pos=[position[0], (txtStims[-1].pos)[1]-60], wrapWidth=1000, color=(-1, -1, -1),
                                colorSpace='rgb',opacity=1)

    my_mouse = Mouse()
    clicked = False
    while (not clicked):
        if imgButton.contains(my_mouse):
            imgButton.image = "./img/button/click2.png"
            for i in range(len(txtStims)):
                txtStims[i].draw()
            imgButton.draw();
            txtButton.draw();
            for stim in stims:
                stim.draw()
            win.flip()
            if my_mouse.getPressed()[0] == 1:
                clicked = True
                DictWriteRaw(dfRaw, dictRaw, params, "Mouse clicked")
                ResponseRecord(params, dict,"Continue Clicked","")
        else:
            imgButton.image = "./img/button/click1.png"
            for i in range(len(txtStims)):
                txtStims[i].draw()
            imgButton.draw();
            txtButton.draw();
            for stim in stims:
                stim.draw()
            win.flip()
        core.wait(1 / 300)
    core.wait(1 / 300)
