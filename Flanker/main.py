# Python3-based package
"""
MIT License

Copyright (c) 2022 NIMH

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
Flanker Psychopy Game (Conversion from E-prime)
Base: Python3, Psychopy3

- Created Wed Mar 16 08:58:05 EDT 2022 by Kyunghun Lee
"""

# Import standard python libraries
from psychopy import visual,core, event
import numpy as np
import os, datetime,sys
import pandas as pd
import random
sys.path.insert(1, './src')
from DictInitialize import DictInitialize
from InstructionPlay import InstructionPlay
from Helper import WaitSeconds,WaitAndGetUserInput
from FlankerPlay import FlankerPlay
from UserInputPlay import UserInputPlay
from FixationPlay import FixationPlay
from ReadyPlay import ReadyPlay
from BlankPlay import BlankPlay

# Make empty output directory if it does not exist.
directory = './result'
if not os.path.exists(directory):
    os.makedirs(directory)

# Pandas configuration (debugging options)
pd.set_option('display.max_columns', None)

# header = ["expName","Version","subjectID","Session Number","Section","Start Time","End Time","Duration","Trial Count",
#           "Image Displayed","Flanker","Direction","Correct Answer","Cell Number","User Response","Correct or Incorrect",
#           "User Response TimeStamp","User Response Time"]
# headerRaw = ["TimeStamp", "expName", "Version", "subjectID", "Session", "Event"]

# Get input from a user window and setup the name of output files.
params = UserInputPlay()
timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
params['outFile'] = ''.join(["./result/",params["expName"],"_",str(params["subjectID"]),"_",str(params["Session"]),
                            timeLabel,".csv"])
params['outFileRaw'] = ''.join(["./result/",params["expName"],"_",str(params["subjectID"]),"_",str(params["Session"]),
                            timeLabel,"_raw.csv"])

# Output Summary header Initialization
params["header"] = ["expName","Version","subjectID","Session Number","Section","Start Time","End Time","Duration",
                    "Block Count",
                    "Trial Count","Image Displayed","Flanker","Direction","Correct Answer","Cell Number",
                    "User Response","Correct or Incorrect","User Response TimeStamp","User Response Time"]

# Dictionary and dataframe Initialization
dict = DictInitialize(params)
df = pd.DataFrame(columns=params["header"])
# dfRaw = pd.DataFrame(columns=headerRaw)

# Make empty output file frames.
df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)

# Load a Timing File.
timingFile = "timing/iti.csv"
dfTiming = pd.read_csv(timingFile,header=None,names=['ITI'])
ITIs = np.array(dfTiming['ITI'])

# Instruction Section
win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
df,dict = InstructionPlay(df,dict,win,params)
# df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)

for blockCount in range(params['nBlocks']):
    # Waiting for scanner (press 5) and display Get Ready screen.
    df,dict = ReadyPlay(df,dict,win,params,blockCount)

    # Random order generations
    orderMat = [0,1,2,3] * 9
    random.shuffle(orderMat)
    random.shuffle(ITIs)
    for trialCount in range(params['nTrials']):

        # Fixation Screen
        df, dict = FixationPlay(df, dict, win, params,blockCount,trialCount)

        # Present Flanker
        n = orderMat[trialCount]
        if n == 0:
            df,dict = FlankerPlay(df,dict,"CL",win,params,blockCount,trialCount)
        elif n == 1:
            df,dict = FlankerPlay(df,dict,"CR",win,params,blockCount,trialCount)
        elif n == 2:
            df,dict = FlankerPlay(df,dict,"IR",win,params,blockCount,trialCount)
        elif n == 3:
            df,dict = FlankerPlay(df,dict,"IL",win,params,blockCount,trialCount)

        # Blank Screen
        df, dict = BlankPlay(df,ITIs[trialCount]/1000,dict, win, params,blockCount,trialCount)

    # Save the result.
    df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)


win.close()
