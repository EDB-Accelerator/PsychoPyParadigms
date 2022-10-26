# Python3-based package
"""
DoorTaskPlayGame.py

DoorTask Game Main Driver File.

Created on Fri July 24 15:04:19 2020

Bug: not working with AMD Radeon GPU devices. (worked with NVIDA)

@author: Kyunghun Lee
- Created Wed, Oct 12, 2022 11:00:46 AM   by KL
"""

# Import developer-defined functions
import sys,os
sys.path.append('libs')
sys.path.insert(1, './src')
import datetime
import pandas as pd
from psychopy import visual,core,event
from psychopy.hardware import keyboard
from Helper import Questionplay,waitUserSpace
from Helper import waitAnyKeys,ResolutionIntialization

from userInputPlay import userInputPlay
from VASplay import VASplay
from InstructionPlay import InstructionPlay
from PracticeGamePlay import PracticeGamePlay
from DoorGamePlay import DoorGamePlay
from FortuneGamePlay import FortuneGamePlay
# from psychopy import parallel
from psychopy import prefs
# import subprocess as subp


def shutdown_key():
    core.quit()

# Receive User input from User input window.
userInputBank = userInputPlay()

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
    'FullScreen': userInputBank[7],
    # 'soundMode' : userInputBank[8],
    'imageDir': './img/doors1/',    # directory containing DOOR image stimuli (default value)
    'imageSuffix': '*.jpg',   # DOOR image extension.
    'totalRewardThreshold' : 20, # The total number of coin to get Extra $10 reward.

# declare output file location
    'outFolder': './output', # the location of output file.

# declare display parameters
    'screenSize' : (1024,768),
    'volume' : 0.8,
    'resolutionMode' : True,
    'subTrialCounter': 0,
    'idxTR': 0,
    'idxImg': 0,
}

# Audio library configuration.
# if params['soundMode'] == 'PTB':
#     prefs.hardware['audioLib'] = ['PTB']
# else:
#     prefs.hardware['audioLib'] = ['pygame', 'pyo', 'sounddevice', 'PTB']

# Define Output file names.
timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
params['outFile'] = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + ".csv"
params['outFileTrackerLog'] = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "TR.csv"
params['Practice'] =  params['outFolder'] + '/' +str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "PR.EDF"
params['TaskRun1'] = params['outFolder'] + '/' +str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "TR1.EDF"
params['TaskRun2'] = params['outFolder'] + '/' +str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "TR2.EDF"
params['TaskRun3'] = params['outFolder'] + '/' +str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "TR3.EDF"

prefs.general['fullscr'] = params['FullScreen']

# Global Exit
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

if userInputBank[3]!= 1:
    params['imageDir'] = './img/doors2/'

## Setup Psychopy Window.
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
img = visual.ImageStim(win=win, image="./img/ITI_fixation.jpg", units="pix", opacity=1, size=(params[ 'screenSize'][0], params['screenSize'][1]))

# ====================== #
# ==== Title Screen ==== #
# ====================== #
img1 = visual.ImageStim(win=win,image="./img/title.jpg",units="pix",size=params['screenSize'],opacity=1) #
win.mouseVisible = False
img1.draw();win.flip();
waitAnyKeys()