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
DisplayFixationCross.py

DwellTask Psychopy3 Sub function.

This function is for writing Table.

Created on Wed Feb  3 13:49:20 EST 2021

@author: Kyunghun Lee
- Created on Wed Feb  3 13:34:46 EST 2021 by KL
"""
import datetime,time,re

Header = ["SubjectID","expName","Session","Language","Section","Section Start Time","Section End Time","Section Time",
          "Response Time","User Answer","User Answer Correctness"]
def DictWriteRaw(dfRaw,dictRaw,params,event):
    # Move data in Dict into Df.
    dictRaw["Event"] = event
    dictRaw["TimeStamp"] = time.strftime('%m-%d-%Y %H:%M:%S')
    dfRaw = dfRaw.append(dictRaw, ignore_index=True)
    dfRaw.to_csv(params['outFileRaw'],mode='a',sep=',',encoding='utf-8',index=False,header=False)

def SectionStart(df,dfRaw,params,dict,dictRaw,sectionName):
    dict["Section Start Time"] = time.strftime('%m-%d-%Y %H:%M:%S')
    params["StartTime"] = time.time()
    DictWriteRaw(dfRaw, dictRaw, params, sectionName + " started")

def ResponseRecord(params,dict,userAnswer,Answer):
    dict["Response Time"] = time.time() - params["StartTime"]
    dict["User Answer"] = userAnswer
    if userAnswer != "" and userAnswer != "Continue Clicked" and "Language selected" not in userAnswer:
        dict["User Answer Correctness"] = "Correct" if userAnswer == Answer else "Incorrect"

def SectionEnd(df,dfRaw,params,dict,dictRaw,sectionName):
    dict["Section End Time"] = time.strftime('%m-%d-%Y %H:%M:%S')
    dict["Section Time"] = time.time() - params["StartTime"]
    if "Response Time" not in dict:
        dict["Response Time"] = ""

    # Move data in Dict into Df.
    for key in Header:
        if key not in dict.keys():
            dict[key] = ""

    df = df.append(dict,ignore_index=True)
    df.to_csv(params['outFile'],mode='a',sep=',',encoding='utf-8',index=False,header = False)
    del dict["Response Time"]

    if "User Answer" or "User Answer Correctness":
        del dict["User Answer"]

    # Section Ended.
    DictWriteRaw(dfRaw, dictRaw, params, sectionName+ " ended")
