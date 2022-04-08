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

import time,re
import datetime,os
import pandas as pd

Header = ["Start Time", "End Time", "Duration", "Accumulated Time","expName", "Version", "subjectID", 'timingFile',"Session", "Event",
          "Sound Type"]

HeaderRaw = ["TimeStamp", "expName", "Version", "subjectID", "Session", "Event"]

def DictWriteRaw(dfRaw,params,event):
    print(event)
    dictRaw = {}
    dictRaw["TimeStamp"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    dictRaw["expName"] = params['expName']
    dictRaw["Version"] = params['Version']
    dictRaw["subjectID"] = params['subjectID']
    dictRaw["Session"] = params["Session"]
    dictRaw["Event"] = event
    dfRaw = dfRaw.append(dictRaw, ignore_index=True)
    # if not os.path.isfile(params['outFileRaw']):
    #     dfRaw.to_csv(params['outFileRaw'],sep=',',encoding='utf-8',index=False,header=HeaderRaw)
    # else:  # else it exists so append without writing the header
    #     dfRaw.to_csv(params['outFileRaw'],mode='a',sep=',',encoding='utf-8',index=False,header=False)

    return dfRaw

def DictWriteStart(params):
    params["Start Time"] = datetime.datetime.now()

def DictWriteEnd(df,params,event):
    params["End Time"] = datetime.datetime.now()

    dict = {}
    dict["Start Time"] = params["Start Time"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    dict["End Time"] = params["End Time"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    dict["Duration"] = (params["End Time"] - params["Start Time"]).total_seconds()
    dict["Accumulated Time"] = (params["End Time"] - params['gameStartTime']).total_seconds()

    dict["expName"] = params['expName']
    dict["Version"] = params['Version']
    dict["subjectID"] = params['subjectID']
    dict['timingFile'] = 'timing/' + str(params['TimingFile'])+ '.csv'
    dict["Session"] = params["Session"]
    dict["Event"] = event

    if "PO500HZ.WAV" in event:
        dict["Sound Type"] = 'Standard'
    elif 'PN650HZ.WAV' in event:
        dict["Sound Type"] = 'Deviant'
    elif 'No sound' in event or 'Interval' in event:
        dict["Sound Type"] = 'None'
    else:
        dict["Sound Type"] = 'Novel'

    df = df.append(dict, ignore_index=True)

    # if not os.path.isfile(params['outFile']):
    #     df.to_csv(params['outFile'],sep=',',encoding='utf-8',index=False,header=Header)
    # else:  # else it exists so append without writing the header
    #     df.to_csv(params['outFile'],mode='a',sep=',',encoding='utf-8',index=False,header=False)

    return df