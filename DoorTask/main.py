# Python3-based package
"""
DoorTaskPlayGame.py

DoorTask Game Main Driver File.

Created on Fri July 24 15:04:19 2020

Bug: not working with AMD Radeon GPU devices. (worked with NVIDA)

@author: Kyunghun Lee
- Created July/24/20 by KL
- Updated 09/3/2020 Tue by KL (Trigger)
- Updated 09/15/2020 Tue by KL (Major Updates)
- Updated 4/21/2021 Wed by KL (Eyetracker update - major updates)
- Save result when exit 10/26/2020 Mon by KL
"""

# Import developer-defined functions
import sys
sys.path.insert(1, './src')
import datetime
import pandas as pd
from psychopy import visual,core,event
from Helper import Questionplay,waitUserSpace
from Helper import waitUserInput, waitAnyKeys,ResolutionIntialization

from userInputPlay import userInputPlay
from VASplay import VASplay
from InstructionPlay import InstructionPlay
from PracticeGamePlay import PracticeGamePlay
from DoorGamePlay import DoorGamePlay
from EyeTrackerCalibration import EyeTrackerCalibration
from EyeTrackerInitialization import EyeTrackerInitialization

from psychopy import parallel
from psychopy import prefs
from sys import platform
import time

def shutdown_key():
    core.quit()

# Receive User input from User input window.
userInputBank = userInputPlay()

# Audio library configuration.
# prefs.hardware['audioLib'] = ['PTB']
# prefs.hardware['audioLib'] = ['pygame', 'pyo', 'sounddevice', 'PTB']

# Declare primary task parameters.
params = {
# Declare stimulus and response parameters
    'expName' : "Doors_AA_v8.py", # The name of the experiment
    'subjectID' : userInputBank[0],      # Subject ID
    'DistanceStart' : 50,
    'DistanceLockWaitTime' : 10, # Distance lock wait time.
    'Session' : userInputBank[1], # Session ID
    'Version' : userInputBank[2], # Version
    'numPractice' : userInputBank[3], # The number of Trials in Practice.
    'numTaskRun1': userInputBank[4],  # The number of Trials in TaskRun1.
    'numTaskRun2': userInputBank[5],  # The number of Trials in TaskRun2.
    'numTaskRun3': userInputBank[6],  # The number of Trials in TaskRun2.
    'JoyStickSupport' : True, # Check if joystick option is checked or not.
    'triggerSupport': userInputBank[7],  # Check if joystick option is checked or not.
    'EyeTrackerSupport': userInputBank[8],
    'FullScreen': False,
    'portAddress': int("0xE050", 16), # Port Address
    'imageDir': './img/doors1/',    # directory containing DOOR image stimluli (default value)
    'imageSuffix': '*.jpg',   # DOOR image extension.
    'totalRewardThreshold' : 20, # The total number of coin to get Extra $10 reward.
# declare output file location
    'outFolder': './output', # the location of output file.
# declare display parameters
    'screenSize' : (1024,780),
    'volume' : 0.8,
    'resolutionMode' : True,
    'subTrialCounter': 0,
}

prefs.general['fullscr'] = params['FullScreen']

if userInputBank[3]!= 1:
    params['imageDir'] = './img/doors2/'


## Setup Psychopy Window.
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
img = visual.ImageStim(win=win, image="./img/ITI_fixation.jpg", units="pix", opacity=1, size=(params[ 'screenSize'][0], params['screenSize'][1]))


# Trigger Initialization
port = 0

if platform == "darwin":
    params['triggerSupport'] = False
if params['triggerSupport']:
    port = parallel.ParallelPort(address=params['portAddress'])
    port.setData(0) # initialize to all zeroscv

# ====================== #
# ==== Title Screen ==== #
# ====================== #
img1 = visual.ImageStim(win=win,image="./img/title.jpg",units="pix",size=params['screenSize'],opacity=1) #
win.mouseVisible = False
img1.draw();win.flip();
waitAnyKeys()

# ======================== #
# Dataframe Initialization #
# ======================== #
Header = ["ExperimentName","SessionStartDateTime","Subject","Session","Version","Section","Subtrial",
          "DistanceFromDoor_SubTrial","Distance_lock","Distance_start","Distance_min","Distance_max",
          "Door_anticipation_time","Door_opened","Door_outcome","Reward_magnitude","Punishment_magnitude",
          "DoorAction_RT","ITI_duration","Total_coins","VAS_type","VAS_score","VAS_RT","Q_type","Q_score","Q_RT"]

Df = pd.DataFrame(columns=Header)

# ====================== #
# ======== VAS pre ========= #
# ====================== #
win.mouseVisible = True
Df = VASplay(Df,win,params,"VAS pre")
win.mouseVisible = False

# ====================== #
# ===== Instruction ==== #
# ====================== #
Df = InstructionPlay(Df,win,params)

# ========================================== #
# ==== Screen Resolution Initialization ==== #
# ========================================== #
ResolutionIntialization(params,size_diff=1/65)

# ====================== #
# ===== Practice ======= #
# ====================== #
if params['EyeTrackerSupport']:
    # Eyetracker Initialization
    tracker = EyeTrackerInitialization()

    # Eyetracker Calibration and start recording.
    tracker = EyeTrackerCalibration(tracker)

Df = PracticeGamePlay(Df,win,params,params['numPractice'],port,tracker,"Practice")

# Stop recording
if params['EyeTrackerSupport']:
    tracker.setRecordingState(False)

# ====================== #
# ===== TaskRun1 ======= #
# ====================== #
if params['EyeTrackerSupport']:
    # Eyetracker Calibration and start recording.
    tracker = EyeTrackerCalibration(tracker)

Df = DoorGamePlay(Df,win,params,params['numTaskRun1'],port,tracker,"TaskRun1")

# Stop recording
if params['EyeTrackerSupport']:
    tracker.setRecordingState(False)

# ====================== #
# ======== VAS 1 ========= #
# ====================== #
win.mouseVisible = True
message = visual.TextStim(win, text="Let's rest for a bit. Click when you are ready to keep playing.", units='norm', wrapWidth=2)
message.draw();win.flip();
waitUserSpace(Df,params)
Df = VASplay(Df,win,params,"VAS 1")
win.mouseVisible = False

# ====================== #
# ======== Text Slide ========= #
# ====================== #
# message = visual.TextStim(win, text="Click when you are ready to continue the game.", units='norm', wrapWidth=3)
# message.draw();
win.mouseVisible = False
img1 = visual.ImageStim(win=win,image="./img/after_VAS2.jpg",units="pix",size=params['screenSize'],opacity=1) #
waitUserInput(Df,img1, win, params,'pyglet')
win.flip();

# ====================== #
# ===== TaskRun2 ======= #
# ====================== #
if params['EyeTrackerSupport']:
    # Eyetracker Calibration and start recording.
    tracker = EyeTrackerCalibration(tracker)

Df = DoorGamePlay(Df,win,params,params['numTaskRun2'],port,tracker,"TaskRun2")

# Stop recording
if params['EyeTrackerSupport']:
    tracker.setRecordingState(False)

# ====================== #
# ======== VAS mid ========= #
# ====================== #
win.mouseVisible = True
if platform != "darwin":
    win.close()
    win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet',units="pix")
message = visual.TextStim(win, text="Let's rest for a bit. Click when you are ready to keep playing.", units='norm', wrapWidth=2)
message.draw();win.flip();
waitUserSpace(Df,params)
Df = VASplay(Df,win,params,"VAS mid")
win.mouseVisible = False

# ====================== #
# ======== Text Slide ========= #
# ====================== #
# message = visual.TextStim(win, text="Click when you are ready to continue the game.", units='norm', wrapWidth=3)
# message.draw();
# win.mouseVisible = False
img1 = visual.ImageStim(win=win,image="./img/after_VAS2.jpg",units="pix",size=params['screenSize'],opacity=1) #
waitUserInput(Df,img1, win, params,'pyglet')
win.flip();


# ====================== #
# ===== TaskRun3 ======= #
# ====================== #
if params['EyeTrackerSupport']:
    # Eyetracker Calibration and start recording.
    tracker = EyeTrackerCalibration(tracker)

Df = DoorGamePlay(Df,win,params,params['numTaskRun3'],port,tracker,"TaskRun3")

# Stop recording
if params['EyeTrackerSupport']:
    tracker.setRecordingState(False)

# ====================== #
# ======== VAS post ========= #
# ====================== #
win.mouseVisible = True
if platform != "darwin":
    win.close()
    win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet',units="pix")
message = visual.TextStim(win, text="Let's rest for a bit. Click when you are ready to keep playing.", units='norm', wrapWidth=2)
message.draw();win.flip();
waitUserSpace(Df,params)
Df = VASplay(Df,win,params,"VAS post")
win.mouseVisible = False

# ====================== #
# ======== Text Slide ========= #
# ====================== #
# message = visual.TextStim(win, text="Click when you are ready to continue the game.", units='norm', wrapWidth=3)
# message.draw();
win.mouseVisible = False
img1 = visual.ImageStim(win=win,image="./img/after_VAS2.jpg",units="pix",size=params['screenSize'],opacity=1) #
waitUserInput(Df,img1, win, params,'pyglet')
win.flip();

# ====================== #
# ======== Question ========= #
# ====================== #
Df = Questionplay(Df, win, params, "Question")

# Write the output file.
outFile = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + ".csv"

Df.to_csv(outFile, sep=',', encoding='utf-8', index=False)

# Close the psychopy window.
win.close()
