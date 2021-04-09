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

from DictWrite import SectionStart,SectionEnd
from DrawButton import DrawButton
from SelectScale import SelectScale
from SelectFourOption import SelectFourOption

def PlayScale1(df,dfRaw,params,dict,dictRaw,win):

    if dict["Language"] == "English":
        question = "How often do you go to a place you've never been before?"
        answerOption = ["never","several times a year","several times a month","weekly or more often"]
    else:
        question = "Hoe vaak ga je naar een plek waar je nog nooit eerder geweest bent?"
        answerOption = ["nooit", "meedere keren per jaar", "meerdere keren per maand", "wekelijks of vaker"]

    SelectFourOption(df, dfRaw, params, dict, dictRaw, win, question, answerOption)

    # Initialization
    dict["Section"] = "PlayScale Introduction"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    stims = []
    txts = []
    if dict["Language"] == "English":
        txts.append("Please indicate to what extent the following statements apply to you (on a scale from 1 to 7).")
    else:
        txts.append("Geef aan op in hoeverre de volgende uitspraken op jouw van toepassing zijn"
                    "(op een schaal van 1 tot 7).")

    DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0,150], "Continue")
    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])

    if dict["Language"] == "English":
        labels = ["Does not apply to me at all","Fully applicable to me"]
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "I can usually remember a new route after taking it once.",labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "I'm afraid of getting lost in a strange city.",labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "I can estimate how long it would take a route in an unknown "
                    "city if I see the route on a map (with legend and scale).",labels)
    else:
        labels = ["Helemaal niet op mij van toepassing", "Volledig op mij van toepassing"]
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "Ik kan me meestal een nieuwe route herinneren nadat ik hem één keer heb afgelegd.",labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "Ik ben bang te verdwalen in een vreemde stad.",labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "Ik kan goed schatten hoe lang ik over een route in een onbekende stad zou doen als ik de route op"
                    " een kaart (met legenda en schaal) zie.",labels)

