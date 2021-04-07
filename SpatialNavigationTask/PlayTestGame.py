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
PlayTestGame.py

MemoryParadigm Psychopy3 Test Driver File.

Created on Mon Feb 22 12:49:15 EST 2021

@author: Kyunghun Lee
- Created on Tue Mon Feb 22 12:49:15 EST 2021 by KL
"""

# Import standard python libraries
import datetime,sys
import pandas as pd
from psychopy import visual,prefs

# Import developer-defined functions
sys.path.insert(1, './src')
from UserInputPlay import UserInputPlay
from DictInitialize import DictInitialize
from SelectLanguage import SelectLanguage
from PlayInstruction import PlayInstruction
from PlayVideo import PlayVideo
from PlaySubTask1 import PlaySubTask1
from SelectTwoOption import SelectTwoOption
import os

# Make empty output directory if there is not.
if not os.path.exists('./result'):
    os.makedirs('./result')

# Pandas configuration (debugging options)
pd.set_option('display.max_columns', None)

# Receive User input from Window.
UserInputBank = UserInputPlay()

# Output Summary Header Initialization
Header = ["SubjectID","expName","Session","Language","Section","Section Start Time","Section End Time","Section Time",
          "Response Time","User Answer","Right Answer","User Answer Correctness","Image Shown"]

# Output Raw Header Initialization
HeaderRaw = ["TimeStamp","expName","SubjectID","Session","Event"]

# Declare primary task parameters.
params = {
    'expName' : 'SpatialNavigation', # The name of the experiment
    'SubjectID' : UserInputBank[0],      # Subject ID
    'Session' : UserInputBank[1], # Session ID
    'screenSize' : (1100,800), # The resolution of Psychopy Window
}

# Decide the name of output files.
params['outFile'] = "./result/test_" + params["expName"] + "_" + str(params["SubjectID"]) + "_" + str(params["Session"]) +\
          datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + ".csv"
params['outFileRaw'] = "./result/test_" + params["expName"] + "_" + str(params["SubjectID"]) + "_" + str(params["Session"]) +\
          datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + "_raw.csv"

# Instance result initialization
dict,dictRaw = DictInitialize(params)

# Open Psychopy Window.
win = visual.Window(params['screenSize'],monitor="testMonitor",color="white",winType='pyglet')

# Construct pandas dataframe structure.
df = pd.DataFrame(columns=Header)
dfRaw = pd.DataFrame(columns=HeaderRaw)

# Make Empty output files.
df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)
dfRaw.to_csv(params['outFileRaw'], sep=',', encoding='utf-8', index=False)

# Select Language.
SelectLanguage(df,dfRaw,params,dict,dictRaw,win)

# Play Instruction
PlayInstruction(df,dfRaw,params,dict,dictRaw,win)

# Play Video
PlayVideo(df,dfRaw,params,dict,dictRaw,win)

# Play Subtask1
PlaySubTask1(df,dfRaw,params,dict,dictRaw,win)

#
# img = "./img/Version1/Tasks/AllocentricLocation/Q1.png"
# SelectTwoOption(df,dfRaw,params,dict,dictRaw,win,img)

# Close the psychopy window.
# win.close()
