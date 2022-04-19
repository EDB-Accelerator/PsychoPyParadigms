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

from psychopy import visual,core
from DictWrite import DictWriteRaw,SectionStart,SectionEnd
from DrawButton import DrawButton


def PlayInstruction(df,dfRaw,params,dict,dictRaw,win):
    # Initialization
    dict["Section"] = "Instruction"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    # Starting Screen
    txt1 = visual.TextStim(win, text="Instruction", height=40, bold=True,
                           units='pix', pos=[0, 300], wrapWidth=300, color=(-1, -1, -1), colorSpace='rgb')
    stims = [txt1]
    txts = []
    if dict["Language"] == "English":
        if params['Version'] == 1:
            txts.append("The experiment is about to begin.")
            txts.append(
                "You are an astronaut sent to a newly discovered planet. Your job is to explore the planet and return to your spaceship. You will walk a route through a forest where you will encounter various objects.")
            txts.append(
                "You will see a video of this exploration. Your mission is to remember as much information about the environment as possible. You will get questions about this later.")
            txts.append("Pay attention! When the video starts you cannot pause or restart it.")
        elif params['Version'] == 2:
            txts.append("The experiment is about to begin.")
            txts.append(
                "You are an astronaut sent to a hostile, scary planet. Your job is to explore this dangerous planet and return safely to your spaceship.")
            txts.append(
                ". You will walk a route through a forest where you will encounter various objects. You will see a video of this exploration. Your mission is to remember as much information about the environment as possible. You will get questions about this later.")
            txts.append("Pay attention! When the video starts you cannot pause or restart it.")
    else:
        txts.append("Het experiment gaat nu beginnen.")
        txts.append(
            "Je bent een astronaut die naar een onbekende planeet is gestuurd. Het is jouw taak de planeet te verkennen. Je loopt zo een route door een bos waar je verschillende voorwerpen tegenkomt. Je krijgt een video te zien  van deze verkenningstocht.")
        txts.append(
            "Het is jouw missie om zo veel mogelijk informatie over de omgeving te onthouden. Je krijgt hier later vragen over.")
        txts.append("Let op! Wanneer de video begint kun je niet meer pauzeren of herstarten.")

    DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0,250], "Continue")

    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])

