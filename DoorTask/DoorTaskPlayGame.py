# Python3-based package
"""
DoorTaskPlayGame.py

DoorTask Game Main Driver File.

Created on Fri July 24 15:04:19 2020

@author: Kyunghun Lee
- Created July/24/20 by KL
- Updated 09/3/2020 Tue by KL (Trigger)
- Updated 09/15/2020 Tue by KL (Major Updates)
"""

import datetime
import pandas as pd
from psychopy import visual,core,event
from Helper import fadeInOutImage, Questionplay,DoorGamePlay,PracticeGamePlay,VASplay,InstructionPlay,userInputPlay,waitUserInput, waitUserSpace,waitAnyKeys
from psychopy import parallel

# Receive User Input
userInputBank = userInputPlay()

# Declare primary task parameters.
params = {
# Declare stimulus and response parameters
    'expName' : userInputBank[0], # The name of the experiment
    'subjectID' : userInputBank[1],      # Subject ID
    'DistanceStart' : 50,
    'DistanceLockWaitTime' : 10, # Distance lock wait time.
    'Session' : userInputBank[2], # Session ID
    'Version' : userInputBank[3], # Version
    'numPractice' : userInputBank[4], # The number of Trials in Practice.
    'numTaskRun1': userInputBank[5],  # The number of Trials in TaskRun1.
    'numTaskRun2': userInputBank[6],  # The number of Trials in TaskRun2.
    'JoyStickSupport' : userInputBank[7], # Check if joystick option is checked or not.
    'triggerSupport': userInputBank[8],  # Check if joystick option is checked or not.
    'portAddress': int(userInputBank[9], 16), # Port Address
    'imageDir': './img/doors1/',    # directory containing DOOR image stimluli (default value)
    'imageSuffix': '*.jpg',   # DOOR image extension.
    'totalRewardThreshold' : 20, # The total number of coin to get Extra $10 reward.
# declare output file location
    'outFolder': './output', # the location of output file.
# declare display parameters
#     'screenSize' : (1200,800),
    'subTrialCounter': 0,
}
if userInputBank[3]!= 1:
    params['imageDir'] = './img/doors2/'

## Setup Section.
# win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
win = visual.Window(monitor="testMonitor",color="black",winType='pyglet')

# Detect Screen size.
params['screenSize'] = (win.monitor.getSizePix()[0],win.monitor.getSizePix()[1])

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
# waitUserInput(img1,win,params)
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
Df = InstructionPlay(Df,win,params)

# ====================== #
# ===== Practice ======= #
# ====================== #
# Get the DOOR image file list.
Df = PracticeGamePlay(Df,win,params,params['numPractice'],port,"Practice")

# ====================== #
# ===== TaskRun1 ======= #
# ====================== #
Df = DoorGamePlay(Df,win,params,params['numTaskRun1'],port,"TaskRun1")

# ====================== #
# ======== VAS2 ========= #
# ====================== #
win.mouseVisible = True
Df = VASplay(Df,win,params,"VAS2")
win.mouseVisible = False
# ====================== #
# ===== TaskRun2 ======= #
# ====================== #
Df = DoorGamePlay(Df,win,params,params['numTaskRun2'],port,"TaskRun2")

# ====================== #
# ======== VAS3 ========= #
# ====================== #
win.mouseVisible = True
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
