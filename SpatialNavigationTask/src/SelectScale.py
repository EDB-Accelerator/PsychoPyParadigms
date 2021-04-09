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

def SelectScale(df,dfRaw,params,dict,dictRaw,win,question):

    # Initialization
    dict["Section"] = "scale question shown:" + question
    dict["User Answer"] = ""

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    # Text message
    txt = visual.TextStim(win, text=question, height=20, bold=True,
                           units='pix', pos=[0, 300], wrapWidth=800, color=(-1, -1, -1), colorSpace='rgb')

    # Scale
    # scale = visual.RatingScale(win,
    #                            # markerStart=50,
    #                            singleClick=True,
    #                            lineColor='Black',pos=[0,0],
    #                            # low=1, high=7,
    #                            tickHeight=0.2,
    #                            # precision=1,
    #                            choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    #                            size=2, textSize=0.2,
    #                            acceptText='Continue', showValue=True, showAccept=True,
    #                            markerColor="Blue")  # markerstart=50
    # scale = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.3, pos=[0.0, -0.5],
    #                                  choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], tickHeight=1,
    #                                  markerColor="Blue",
    #                                  lineColor='Black'
    #                                  )
    scale = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.5],lineColor='Black',
                                     choices=['1', '2', '3', '4', '5', '6', '7'], tickHeight=-1)

    # ratingScale = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.5],
    #                                  choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], tickHeight=-1)

    while scale.noResponse:
        scale.draw()
        txt.draw()
        win.flip()

    # Get user input value.
    dict["User Answer"] = scale.getRating()

    DictWriteRaw(dfRaw, dictRaw, params, "User Answered:" + dict["User Answer"])
    ResponseRecord(params, dict, dict["User Answer"],"")

    SectionEnd(df, dfRaw, params, dict, dictRaw, dict["Section"])


