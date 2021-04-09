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

def PlayScale(df,dfRaw,params,dict,dictRaw,win):

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
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "I can usually remember a new route after taking it once.")
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "I'm afraid of getting lost in a strange city.")
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "I can estimate how long it would take a route in an unknown "
                    "city if I see the route on a map (with legend and scale).")
    else:
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "Ik kan me meestal een nieuwe route herinneren nadat ik hem één keer heb afgelegd.")
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "Ik ben bang te verdwalen in een vreemde stad.")
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "Ik kan goed schatten hoe lang ik over een route in een onbekende stad zou doen als ik de route op"
                    " een kaart (met legenda en schaal) zie.")

