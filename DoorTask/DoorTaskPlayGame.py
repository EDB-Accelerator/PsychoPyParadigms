# Python3-based package
"""
DoorTaskPlayGame.py

DoorTask Game Main Driver File.

Created on Fri July 24 15:04:19 2020

@author: Kyunghun Lee
- Created July/24/20 by KL
- Updated 09/3/2020 Tue by KL (Trigger)
- Updated 09/15/2020 Tue by KL (Major Updates)
- Save result when exit 10/26/2020 Mon by KL
"""

import datetime
import pandas as pd
from psychopy import visual,core,event
from Helper import fadeInOutImage, Questionplay,DoorGamePlay,PracticeGamePlay,VASplay,waitUserSpace
from Helper import InstructionPlay,userInputPlay,waitUserInput, waitAnyKeys,ResolutionIntialization
from psychopy import parallel
from psychopy import prefs

def shutdown_key():
    core.quit()

# Receive User input from User input window.
userInputBank = userInputPlay()

# Audio library configuration.
prefs.hardware['audioLib'] = ['pygame', 'pyo', 'sounddevice', 'PTB']

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
    'JoyStickSupport' : True, # Check if joystick option is checked or not.
    'triggerSupport': userInputBank[6],  # Check if joystick option is checked or not.
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
if userInputBank[3]!= 1:
    params['imageDir'] = './img/doors2/'

## Setup Section.
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
# win = visual.Window(monitor="testMonitor",color="black",winType='pyglet')

# Trigger Initialization
port = 0
if params['triggerSupport']:
    port = parallel.ParallelPort(address=params['portAddress'])
    port.setData(0) # initialize to all zeros

# Display NIMH logo.
# fadeInOutImage(win,"./img/nimh.png",0.5,(300,300))

# ====================== #
# ==== Title Screen ==== #
# ====================== #
img1 = visual.ImageStim(win=win,image="./img/title.jpg",units="pix",size=params['screenSize'],opacity=1) #
win.mouseVisible = False
img1.draw();win.flip();
# waitUserInput(Df,img1,win,params)
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
# ======== VAS ========= #
# ====================== #
win.mouseVisible = True
Df = VASplay(Df,win,params,"VAS1")
win.mouseVisible = False
# ====================== #
# ===== Instruction ==== #
# ====================== #
win.close()
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
Df = InstructionPlay(Df,win,params)

# ========================================== #
# ==== Screen Resolution Initialization ==== #
# ========================================== #

ResolutionIntialization(params,size_diff=1/65)

# ====================== #
# ===== Practice ======= #
# ====================== #
# Get the DOOR image file list.
win.close()
win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='glfw')
win.mouseVisible = False
Df = PracticeGamePlay(Df,win,params,params['numPractice'],port,"Practice")

# ====================== #
# ===== TaskRun1 ======= #
# ====================== #
Df = DoorGamePlay(Df,win,params,params['numTaskRun1'],port,"TaskRun1")

# ====================== #
# ======== VAS2 ========= #
# ====================== #
win.mouseVisible = True
win.close()
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
message = visual.TextStim(win, text="Let’s take a quick break and do some ratings.", units='norm', wrapWidth=3)
message.draw();win.flip();
waitUserSpace(Df,params)
Df = VASplay(Df,win,params,"VAS2")
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
win.close()
win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='glfw')
win.mouseVisible = False
Df = DoorGamePlay(Df,win,params,params['numTaskRun2'],port,"TaskRun2")

# ====================== #
# ======== VAS3 ========= #
# ====================== #
win.close()
win.mouseVisible = True
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
Df = VASplay(Df,win,params,"VAS3")
win.mouseVisible = False
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
