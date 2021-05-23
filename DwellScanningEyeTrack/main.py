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
DwellTask.py

DwellTask Psychopy3 Main Driver File.

Created on Thu Jan 28 15:20:30 EST 2021
Updated on Thu May  6 14:11:14 EDT 2021 (ITI: always 2 sec. Included rest screen)

@author: Kyunghun Lee
- Created on Thu Jan 28 15:20:30 EST 2021 by KL
"""


# Import standard python libraries
import datetime,sys,random
import pandas as pd
from psychopy import visual,prefs,core,event
from glob import glob
import os
import pylink
import asyncio,threading

# Import developer-defined functions
sys.path.insert(1, './src')
from UserInputPlay import UserInputPlay
from DictInitialize import DictInitialize
from DisplayFixationCross import DisplayFixationCross
from DisplayMatrix import DisplayMatrix
from DisplayBlank import DisplayBlank
from DisplayRest import DisplayRest
from EyeTrackerIntialization import EyeTrackerIntialization
from EyeTrackerCalibration import EyeTrackerCalibration
from psychopy.iohub import launchHubServer
from MusicControl import PauseMusic,UnpauseMusic,StopMusic
from DisplayFolderSelection import DisplayFolderSelection
from GetAngryLabels import GetAngryLabels
from MakeAOI import MakeAOI
import psychopy.iohub.client


# End Music if exist.
StopMusic()

def waitUserSpace():
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()


# Make empty output directory if it does not exist.
directory = './result'
if not os.path.exists(directory):
    os.makedirs(directory)

# Audio library configuration.
# prefs.hardware['audioLib'] = ['pygame', 'pyo', 'sounddevice', 'PTB']

# Pandas configuration (debugging options)
pd.set_option('display.max_columns', None)

# Receive User input from Window.
UserInputBank = UserInputPlay()

# Output Summary Header Initialization
Header = ["Section Start Time","Section End Time","expName","subjectID","Session","Section","TrialCount","Section",
          "Image Displayed","Button Pressed","Button Correct/Incorrect","Button Response Time"]

# Output Raw Header Initialization
HeaderRaw = ["TimeStamp","expName","subjectID","Session","Event"]

# Declare primary task parameters.
params = {
    'expName' : 'DwellTask', # The name of the experiment
    'subjectID' : UserInputBank[0],      # Subject ID
    'Session' : UserInputBank[1], # Session ID
    'Version': UserInputBank[2],  # Version
    'BlockNum' : 3, # The number of blocks
    'RunNum' : 2, # The number of Runs
    'numTrial': UserInputBank[3],  # The number of Trials.
    'fullscr': UserInputBank[4],  # The resolution of Psychopy Window
    'screenSize': UserInputBank[5],  # The resolution of Psychopy Window
    'eyeSelection' : UserInputBank[6],  # Which eye will be used for eyetracking
    'circle' : UserInputBank[7],
    'faceMatrixDuration': UserInputBank[8],
    'eyeIdx' : 0,
}

# Full screen support
prefs.general['fullscr'] = params['fullscr']

# Parameter Configuration based on the version.
if params['Version'] == 2:
    params['blankTime'] = [0,2,4]
    params['musicMode'] = 'off'
elif params['Version'] == 3:
    params['blankTime'] = [2]
    params['musicMode'] = 'allTheTime'
elif params['Version'] == 4:
    params['blankTime'] = [2]
    params['musicMode'] = 'onlyWhenStareAt'

    # Music Selection
if params['musicMode'] != 'off':
    # Folder Selection
    params['musicList'] = DisplayFolderSelection(params)
    dfLabel = {}
    labelList = ['6N-10A','6N-10D','8N-8A','8N-8D','10N-6A','10N-6D']
    for label in labelList:
        dfLabel[label] = pd.read_csv('label/' + label + '.csv')

# Decide the name of output files.
timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
params['outFile'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
          timeLabel + ".csv"
params['outFileRaw'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
          timeLabel + "_raw.csv"
params["edfFile"] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
          timeLabel + "_"

# Instance result initialization
dict,dictRaw = DictInitialize(params)

# Generate AOI locations for face matrix.
MakeAOI(params)

# Construct pandas dataframe structure.
df = pd.DataFrame(columns=Header)
dfRaw = pd.DataFrame(columns=HeaderRaw)

# Make Empty output files.
df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)
dfRaw.to_csv(params['outFileRaw'], sep=',', encoding='utf-8', index=False)

# Open Window.
# win = visual.Window(params['screenSize'],monitor="testMonitor",color="white",winType='pyglet')

# Make image list.
RunList = glob('./img/*')
random.shuffle(RunList)
idx = 0
ImgList = []
for run in RunList:
    BlockList = glob(run + '/*')
    random.shuffle(BlockList)

    for block in BlockList:
        params["Block"] = block.split('/')[-1]

        # Get Image list of each block and Shuffle.
        ImgList = ImgList + glob(block + '/*.jpeg')
        idx += 1

# Shuffle Images.
random.shuffle(ImgList)

# Eyetracker Initialization
# win,tracker = EyeTrackerIntialization(params)

# Hide mouse cursor.
# win.mouseVisible = False

# Music
if params['musicMode'] != 'off':
    import subprocess, sys

    p = subprocess.Popen([sys.executable, 'src/StartMusic.py'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    # PauseMusic()

# Run the main task.
for section in range(3):
    params["Section"] = section # This block is different from original block.

    # Eyetracker Calibration.
    win,io,tracker = EyeTrackerIntialization(params)
    win,tracker = EyeTrackerCalibration(params, tracker,block,win)

    # Start recording
    tracker.setRecordingState(True)

    # Pause Music
    if section == 0:
        UnpauseMusic()

    for trial in range(params['numTrial']):
        # win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
        # win.mouseVisible = False
        params["TrialCount"] = trial
        img = ImgList[trial+section*params['numTrial']]

        if params['musicMode'] != 'off':
            labels = GetAngryLabels(dfLabel,img)

        # Fixation cross section
        DisplayFixationCross(df=df,dfRaw=dfRaw,params=params,dict=dict,dictRaw=dictRaw,win=win,tracker=tracker)
        DisplayMatrix(df=df,dfRaw=dfRaw,img=img,params=params,dict=dict,dictRaw=dictRaw,win=win,tracker=tracker,
                      labels=labels)
        DisplayBlank(df=df,dfRaw=dfRaw,params=params,dict=dict,dictRaw=dictRaw,win=win,tracker=tracker)

    # Stop Recording
    tracker.setRecordingState(False)

    # # Stop music
    # t.end()

    # Import the result (from eyetracker)
    trackerIO = pylink.EyeLink('100.1.1.1')
    trackerIO.receiveDataFile("et_data.EDF", params["edfFile"] + "section" + str(section) +".edf")

    # Stop the ioHub Server
    io.quit()
    trackerIO.close()
    if section != 2:
        # End Music
        # PauseMusic()
        # Rest between each section.
        DisplayRest(df, dfRaw, params, dict, dictRaw, win)

PauseMusic()

# Close the psychopy window.
win.close()
p.terminate()
