# Python3-based package
"""
DoorTaskPlayGame.py

DoorTask Game Main Driver File.

Created on Fri July 24 15:04:19 2020

Known issue:

 Does not work with AMD Radeon GPU devices. (worked with NVIDA).
 Only works on Windows 10.
 Resolution: 1024x768.

@author: Kyunghun Lee
- Created July/24/20 by KL
- Updated 09/3/2020 Tue by KL (Trigger)
- Updated 09/15/2020 Tue by KL (Major Updates)
- Save result when exit 10/26/2020 Mon by KL
- Updated 4/21/2021 Wed by KL (Eyetracker update - major updates)
- Major update and bug fixed 6/3/2021 by KL

"""

# Import developer-defined functions
import sys
sys.path.insert(1, './src')
import datetime
import pandas as pd
from psychopy import visual,core
from Helper import waitUserSpace
from Helper import waitUserInput, waitAnyKeys,ResolutionIntialization

from userInputPlay import userInputPlay
from VASplay import VASplay
from InstructionPlay import InstructionPlay
from PracticeGamePlay import PracticeGamePlay
from DoorGamePlay import DoorGamePlay
from QuestionPlay import QuestionPlay
from psychopy import parallel
from psychopy import prefs

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
    'FullScreen': userInputBank[9],
    'sensitivity': userInputBank[10],
    # 'eyeTrackCircle': userInputBank[11],
    'eyeTrackCircle': True,
    'portAddress': int("0xE050", 16), # Port Address
    'imageDir': './img/doors1/',    # directory containing DOOR image stimluli (default value)
    'imageSuffix': '*.jpg',   # DOOR image extension.
    'totalRewardThreshold' : 20, # The total number of coin to get Extra $10 reward.

# declare output file location
    'outFolder': './output', # the location of output file.

# declare display parameters
#     'screenSize' : (userInputBank[11][0],userInputBank[11][1]),
    'screenSize' : (1024,768),
    'volume' : 0.8,
    'resolutionMode' : True,
    'subTrialCounter': 0,
    'idxTR': 0,
    'idxImg': 0,
}

# Define Output file names.
timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
params['outFile'] = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + ".csv"
params['outFileTrackerLog'] = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "TrackerLog.csv"
params['Practice'] =  params['outFolder'] + '/' +str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "Practice.EDF"
params['TaskRun1'] = params['outFolder'] + '/' +str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "TaskRun1.EDF"
params['TaskRun2'] = params['outFolder'] + '/' +str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "TaskRun2.EDF"
params['TaskRun3'] = params['outFolder'] + '/' +str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "TaskRun3.EDF"

prefs.general['fullscr'] = params['FullScreen']

if userInputBank[3]!= 1:
    params['imageDir'] = './img/doors2/'

## Setup Psychopy Window.
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
img = visual.ImageStim(win=win, image="./img/ITI_fixation.jpg", units="pix", opacity=1, size=(params[ 'screenSize'][0], params['screenSize'][1]))

# Trigger Initialization
port = 0
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
params['Header'] = ["ExperimentName","SessionStartDateTime","Subject","Session","Version","Section","Subtrial",
          "DistanceFromDoor_SubTrial","Distance_lock","Distance_start","Distance_min","Distance_max",
          "Door_anticipation_time","Door_opened","Door_outcome","Reward_magnitude","Punishment_magnitude",
          "DoorAction_RT","ITI_duration","Total_coins","VAS_type","VAS_score","VAS_RT","Q_type","Q_score","Q_RT"]
params['HeaderTR'] = ["Index", "subjectID", "Session", "Version", "Section", "Subtrial", "Event", "Reward", "Punishment",
            "Duration(ms)"]

# Pandas dataframe Initialization
Df = pd.DataFrame(columns=params['Header'])
if params['EyeTrackerSupport']:
    DfTR = pd.DataFrame(columns=params['HeaderTR'])
else:
    DfTR = ""

# Make Empty output files.
Df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)
if params['EyeTrackerSupport']:
    DfTR.to_csv(params['outFileTrackerLog'], sep=',', encoding='utf-8', index=False)

# ====================== #
# ======== VAS pre ========= #
# ====================== #
win.mouseVisible = True
VASplay(Df,win,params,"VAS pre")
win.mouseVisible = False

# ====================== #
# ===== Instruction ==== #
# ====================== #
InstructionPlay(Df,win,params)

# ========================================== #
# ==== Screen Resolution Initialization ==== #
# ========================================== #
ResolutionIntialization(params,size_diff=1/65)

# ====================== #
# ===== Practice ======= #
# ====================== #
win.mouseVisible = False
iterNum = params['numPractice']
SectionName = "Practice"

# Df,DfTR,win = PracticeGamePlay(Df,DfTR,win,params,params['numPractice'],port,"Practice")
win = PracticeGamePlay(Df, DfTR,win, params, iterNum, port,SectionName)
win.mouseVisible = True

# ====================== #
# ===== TaskRun1 ======= #
# ====================== #
win.mouseVisible = False
win = DoorGamePlay(Df,DfTR,win,params,params['numTaskRun1'],port,"TaskRun1")
win.mouseVisible = True

# ====================== #
# ======== VAS 1 ========= #
# ====================== #
win.mouseVisible = True
message = visual.TextStim(win, text="Let's rest for a bit.  Press the spacebar when you are ready to keep playing.", units='norm', wrapWidth=2)
message.draw();win.flip();
waitUserSpace(Df,params)
VASplay(Df,win,params,"VAS 1")
win.mouseVisible = False

# ====================== #
# ======== Text Slide ========= #
# ====================== #
win.mouseVisible = False
img1 = visual.ImageStim(win=win,image="./img/after_VAS2.jpg",units="pix",size=params['screenSize'],opacity=1) #
waitUserInput(Df,img1, win, params,'pyglet')
win.flip();

# ====================== #
# ===== TaskRun2 ======= #
# ====================== #
win = DoorGamePlay(Df,DfTR,win,params,params['numTaskRun2'],port,"TaskRun2")

# ====================== #
# ======== VAS mid ========= #
# ====================== #
win.mouseVisible = True
message = visual.TextStim(win, text="Let's rest for a bit.  Press the spacebar when you are ready to keep playing.", units='norm', wrapWidth=2)
message.draw();win.flip();
waitUserSpace(Df,params)
VASplay(Df,win,params,"VAS mid")
win.mouseVisible = False

# ====================== #
# ======== Text Slide ========= #
# ====================== #
img1 = visual.ImageStim(win=win,image="./img/after_VAS2.jpg",units="pix",size=params['screenSize'],opacity=1) #
waitUserInput(Df,img1, win, params,'pyglet')
win.flip();

# ====================== #
# ===== TaskRun3 ======= #
# ====================== #
win.mouseVisible = False
win = DoorGamePlay(Df,DfTR,win,params,params['numTaskRun3'],port,"TaskRun3")
win.mouseVisible = True

# ====================== #
# ======== VAS post ========= #
# ====================== #
win.mouseVisible = True
message = visual.TextStim(win, text="Let's rest for a bit.  Press the spacebar when you are ready to keep playing.", units='norm', wrapWidth=2)
message.draw();win.flip();
waitUserSpace(Df,params)
VASplay(Df,win,params,"VAS post")
win.mouseVisible = False

# ====================== #
# ======== Question ========= #
# ====================== #
win.mouseVisible = True
QuestionPlay(Df, win, params, "Question")

# Close the psychopy window.
win.close()
