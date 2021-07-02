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
import pandas as pd
import datetime

def DictWriteRaw(dfRaw,dictRaw,params):
    # Move data in Dict into Df.
    dictRaw["TimeStamp"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4] # Record Timestamp.
    dictRaw["Version"] = params["Version"]
    dfRaw = dfRaw.append(dictRaw, ignore_index=True)
    dfRaw.to_csv(params['outFileRaw'],mode='a',sep=',',encoding='utf-8',index=False,header=False)
    # dfRaw = dfRaw[:-1] # Drop the last row.

def DictWrite(df,params,dict):
    # Move data in Dict into Df.
    dict["Section"] = params["Section"]
    dict["Version"] = params["Version"]
    dict["TrialCount"] = params["TrialCount"]
    if 'timingFile' in params:
        dict["timingFile"] = params['timingFile']
    df = df.append(dict,ignore_index=True)
    df.to_csv(params['outFile'],mode='a',sep=',',encoding='utf-8',index=False,header = False)
    # df = df[:-1] # Drop the last row.
