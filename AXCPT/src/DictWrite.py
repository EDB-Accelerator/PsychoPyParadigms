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

import pandas as pd
import datetime

def DictWriteRaw(dfRaw,dictRaw,params):
    # Move data in Dict into Df.
    dictRaw["TimeStamp"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4] # Record Timestamp.
    dictRaw["Version"] = params["Version"]
    dfRaw = dfRaw.append(dictRaw, ignore_index=True)
    dfRaw.to_csv(params['outFileRaw'],mode='a',sep=',',encoding='utf-8',index=False,header=False)
    # dfRaw = dfRaw[:-1] # Drop the last row.

def DataWrite(params,startTime,endTime,trialCount,trialType,event,timingFile,userResponse,rightAnswer,userResponseTime,userResponseOffset):

    dict = {}
    Header = ["expName", "subjectID", "Session", "TrialCount", "Trial Type", "Event", "Start Time", "End Time",
              "Duration (sec)",
              'Timing File', "User Response", "Right Answer", "Correct or Incorrect", "User Response TimeStamp",
              "User Response Time (the amount of time that passes from time the letter was shown)"]

    # Basic information extraction from params
    dict["expName"] = params["expName"]
    dict["subjectID"] = params["subjectID"]
    dict["Session"] = params["Session"]

    # Get information from arguments
    dict["TrialCount"] = trialCount
    dict["Trial Type"] = trialType
    dict["Event"] = event
    # startTime = datetime.datetime.now()
    # endTime = datetime.datetime.now()
    dict["Start Time"] = startTime.strftime("%m/%d/%Y %H:%M:%S.%f")[:-4] # startTime.strftime("%m/%d/%Y %H:%M:%S.%f")[:-4]
    dict["End Time"] = endTime.strftime("%m/%d/%Y %H:%M:%S.%f")[:-4]
    dict["Duration (sec)"] = (endTime - startTime).total_seconds()

    dict["Timing File"] = timingFile
    try:
        dict["User Response"] = userResponse[0] if userResponse != "space bar" and userResponse != "No response" else userResponse
    except:
        dict["User Response"] = userResponse
    dict["Right Answer"] = rightAnswer

    if dict["Right Answer"] == "":
        dict["Correct or Incorrect"] = ""
    else:
        dict["Correct or Incorrect"] = "Correct" if dict["User Response"].upper() == dict["Right Answer"].upper() else "Incorrect"

    if userResponseTime == "No response" or dict["User Response"] == "No response":
        dict["User Response TimeStamp"] = "No response"
        dict["User Response"] = "No response"
        dict["User Response Time (the amount of time that passes from time the letter was shown)"] = "No response"
    elif userResponse == "Already answered":
        dict["User Response TimeStamp"] = "Already answered"
        dict["User Response"] = "Already answered"
        dict["User Response Time (the amount of time that passes from time the letter was shown)"] = "Already answered"
    elif userResponseTime == "":
        dict["User Response TimeStamp"] = ""
        dict["User Response Time (the amount of time that passes from time the letter was shown)"] = ""
    else:
        dict["User Response TimeStamp"] = userResponseTime.strftime("%m/%d/%Y %H:%M:%S.%f")[:-4]
        dict["User Response Time (the amount of time that passes from time the letter was shown)"] = \
            (userResponseTime - startTime).total_seconds() + userResponseOffset

    dict["User Response"] = dict["User Response"].upper() if len(dict["User Response"])==1 else dict["User Response"]

    df = pd.DataFrame(columns=Header)
    df = df.append(dict,ignore_index=True)
    df.to_csv(params['outFile'],mode='a',sep=',',encoding='utf-8',index=False,header = False)
