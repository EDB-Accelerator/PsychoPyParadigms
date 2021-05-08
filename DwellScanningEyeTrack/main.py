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

# Import developer-defined functions
sys.path.insert(1, './src')
from UserInputPlay import UserInputPlay
from DictInitialize import DictInitialize
from DisplayFixationCross import DisplayFixationCross
from DisplayMatrix import DisplayMatrix
from DisplayBlank import DisplayBlank
from DisplayRest import DisplayRest
from EyeTrackerCalibration import EyeTrackerCalibration
from psychopy.iohub import launchHubServer

def waitUserSpaceAndC():
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space' and c[0] != 'c'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q'] or c == ['Esc']:
            print('Q or ESC pressed. Forced Exit.')
            core.quit()
    return c[0]

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

# Full screen support
prefs.general['fullscr'] = UserInputBank[3]

# Output Summary Header Initialization
Header = ["Section Start Time","Section End Time","expName","subjectID","Session","Block","TrialCount","Section",
          "Image Displayed","Button Pressed","Button Correct/Incorrect","Button Response Time"]

# Output Raw Header Initialization
HeaderRaw = ["TimeStamp","expName","subjectID","Session","Event"]

# Declare primary task parameters.
params = {
    'expName' : 'DwellTask', # The name of the experiment
    'subjectID' : UserInputBank[0],      # Subject ID
    'Session' : UserInputBank[1], # Session ID
    'BlockNum' : 3, # The number of blocks
    'RunNum' : 2, # The number of Runs

    'numTrial': UserInputBank[2],  # The number of Trials.
    # 'screenSize': (900, 900),  # The resolution of Psychopy Window
    'screenSize': UserInputBank[4],  # The resolution of Psychopy Window
}

# Decide the name of output files.
params['outFile'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
          datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + ".csv"
params['outFileRaw'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
          datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + "_raw.csv"

# Instance result initialization
dict,dictRaw = DictInitialize(params)

# Construct pandas dataframe structure.
df = pd.DataFrame(columns=Header)
dfRaw = pd.DataFrame(columns=HeaderRaw)

# Make Empty output files.
df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)
dfRaw.to_csv(params['outFileRaw'], sep=',', encoding='utf-8', index=False)

# Open Window.
# win = visual.Window(params['screenSize'],monitor="testMonitor",color="white",winType='pyglet')

# Disable mouse cursor.
# win.mouseVisible = False

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

# if params['EyeTrackerSupport']:
win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')

message = visual.TextStim(win,
                          text="Eyetracker Calibration will start.  \n\nPress the spacebar when you are ready.",
                          units='norm', wrapWidth=2,color="black")
message.draw();
win.flip();
waitUserSpace()

iohub_config = {'eyetracker.hw.sr_research.eyelink.EyeTracker':
                    {'name': 'tracker',
                     'model_name': 'EYELINK 1000 DESKTOP',
                     'runtime_settings': {'sampling_rate': 500,
                                          'track_eyes': 'RIGHT'}
                     }
                }
# Start new ioHub server.
import psychopy.iohub.client

try:
    io = launchHubServer(**iohub_config)
except:
    q = psychopy.iohub.client.ioHubConnection.getActiveConnection().quit()
    io = launchHubServer(**iohub_config)
# Get the eye tracker device.
tracker = io.devices.tracker

tracker.sendCommand("screen_pixel_coords = 0 0 %d %d" % (params['screenSize'][0] - 1, params['screenSize'][1] - 1))

# save screen resolution in EDF data, so Data Viewer can correctly load experimental graphics
# see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
tracker.sendMessage("DISPLAY_COORDS = 0 0 %d %d" % (params['screenSize'][0] - 1, params['screenSize'][1] - 1))

# Eyetracker Calibration.
c = 'c'
while c != 'space':
    tracker = EyeTrackerCalibration(tracker)
    win.close()
    win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
    message = visual.TextStim(win,
                              text="Calibration is completed.  Press the spacebar when you are ready to keep playing.\n Press 'c' to do calibration again.",
                              units='norm', wrapWidth=2,color="black")
    message.draw();
    win.flip();
    c = waitUserSpaceAndC()
win.close()


# # Run the main task.
# for block in range(3):
#     params["Block"] = block
#
#     # if params['EyeTrackerSupport'] and block>=1:
#
#     # win.close()
#     win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
#     message = visual.TextStim(win,
#                               text="Eyetracker Calibration will start.  \n\nPress the spacebar when you are ready.",
#                               units='norm', wrapWidth=2,color='black')
#     message.draw();
#     win.flip();
#     waitUserSpace()
#     # win.close()
#     tracker = EyeTrackerCalibration(tracker)
#
#     # Eyetracker Calibration.
#     c = 'c'
#     while c != 'space':
#         win.close()
#         win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
#         message = visual.TextStim(win,
#                                   text="Calibration is completed.\n\nPress the spacebar when you are ready to keep playing.\n\n Press 'c' to do calibration again.",
#                                   units='norm', wrapWidth=2,color='black')
#         message.draw();
#         win.flip();
#         c = waitUserSpaceAndC()
#         if c != 'space':
#             break
#     # win.close()
#
#     for trial in range(params['numTrial']):
#         win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
#         params["TrialCount"] = trial
#         img = ImgList[trial+block*params['numTrial']]
#
#
#         # Fixation cross section
#         DisplayFixationCross(df=df,dfRaw=dfRaw,params=params,dict=dict,dictRaw=dictRaw,win=win)
#         DisplayMatrix(df=df,dfRaw=dfRaw,img=img,params=params,dict=dict,dictRaw=dictRaw,win=win)
#         DisplayBlank(df=df,dfRaw=dfRaw,params=params,dict=dict,dictRaw=dictRaw,win=win)
#
#     if block != 2:
#         # Rest between each block.
#         DisplayRest(df, dfRaw, params, dict, dictRaw, win)
#
# # Close the psychopy window.
# win.close()
