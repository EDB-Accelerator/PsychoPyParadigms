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
- Updated Fri, Oct  8, 2021  1:42:55 PM by KL (Reward/punishment score display on AOIs)
- Updated Fri, Mar 11, 2022  4:13:50 PM by KL (Instruction updated)
- Save result when exit 10/26/2020 Mon by KL
- Dynamic AOI updated Tue, Apr 12, 2022  3:21:26 PM by Lucrezia
- Fortune Wheel updated Tue, May 31, 2022 11:29:44 AM by Kyunghun
- Heatpain Sensor update, Mon Mar 31 07:19:44 EDT 2025 by Kyunghun
"""

# Import developer-defined functions
import sys,os
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
from FortuneGamePlay import FortuneGamePlay
from psychopy import parallel
from psychopy import prefs
import subprocess as subp

def shutdown_key():
    core.quit()

# Receive User input from User input window.
userInputBank = userInputPlay()

# Declare primary task parameters.
params = {
# Declare stimulus and response parameters
    'expName' : "Doors_heatpain.py", # The name of the experiment
    'subjectID' : userInputBank[0],      # Subject ID
    'DistanceStart' : 50,
    'DistanceLockWaitTime' : 10, # Distance lock wait time.
    'Session' : userInputBank[1], # Session ID
    'Version' : userInputBank[2], # Version
    'numPractice' : userInputBank[3], # The number of Trials in Practice.
    'numTaskRun1': userInputBank[4],  # The number of Trials in TaskRun1.
    'numTaskRun2': userInputBank[5],  # The number of Trials in TaskRun2.
    'numTaskRun3': userInputBank[6],  # The number of Trials in TaskRun2.
    'JoyStickSupport' : True if userInputBank[8]<=2 else False, # Check if joystick option is checked or not.
    # 'triggerSupport': userInputBank[7],  # Check if joystick option is checked or not.
    # 'EyeTrackerSupport': userInputBank[8],
    'triggerSupport': False,  # Check if joystick option is checked or not.
    'EyeTrackerSupport': False,
    'FullScreen': userInputBank[7],
    'sensitivity': userInputBank[8],
    'soundMode' : userInputBank[9],
    'HeatSupport': userInputBank[10],
    # 'eyeTrackCircle': userInputBank[11],
    'eyeTrackCircle': True,
    'portAddress': int("0xE050", 16), # Port Address
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
    'codeFixation': 143,
    'convExcel': 'tempConv.xlsx',
}
# Assign Heat1 to Heat7 dynamically from userInputBank[13] to userInputBank[19]
for i in range(7):
    params[f'Heat{i+1}'] = userInputBank[11 + i]

# Audio library configuration.
if params['soundMode'] == 'PTB':
    prefs.hardware['audioLib'] = ['PTB']
else:
    prefs.hardware['audioLib'] = ['pygame', 'pyo', 'sounddevice', 'PTB']

# params['virtualMode'] = False if params['JoyStickSupport'] else True

# Define Output file names.
timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
params['outFile'] = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + ".csv"
params['outFile_tmp'] = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
          str(params['Version']) + '_' +  timeLabel + "_aborted.csv"



prefs.general['fullscr'] = params['FullScreen']

# Global Exit
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

# if userInputBank[3]!= 1:
#     params['imageDir'] = './img/doors2/'
params['imageDir'] = f"./img/doors{params['Version']}/"

## Setup Psychopy Window.
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
img = visual.ImageStim(win=win, image="./img/ITI_fixation.jpg", units="pix", opacity=1, size=(params[ 'screenSize'][0], params['screenSize'][1]))

# # Trigger Initialization
port = 0
if params['triggerSupport']:
    port = parallel.ParallelPort(address=params['portAddress'])
    port.setData(0) # initialize to all zeroscv
# Heatpain Initialization
my_pathway = None
excelTemps = None
if params['HeatSupport']:
    # if params['sendPortEvents']:
    #     from psychopy import parallel
    #
    #     port = parallel.ParallelPort(address=params['portAddress'])
    #     port.setData(0)  # initialize to all zeros
    # else:
    #     print("Parallel port not used.")

    import sys
    sys.path.append('libs')
    from pymedoc.devices import Pathway

    # ip and port number from medoc application
    my_pathway = Pathway(ip='10.150.254.8', port_number=20121)

    # Check status of medoc connection
    response = my_pathway.status()
    print(response)

    # excel in the folder to convert from Celsius temp to binary code for the medoc machine
    excelTemps = pd.read_excel(params['convExcel'])


    # use color, size, and block to calculate data for SetPortData
    # expInfo = {
    # 'LHeat': 36.0,
    # 'MHeat': 41.0,
    # 'HHeat': 46.0,
    # }
    # # Send parallel port event
    # # def SetPortData(data):
    # #     if params['painSupport'] and params['sendPortEvents']:
    # #         # logging.log(level=logging.EXP, msg='set port %s to %d' % (format(params['portAddress'], '#04x'), data))
    # #         port.setData(data)
    # #         print(data)
    # #     else:
    # #         if params['painSupport']:
    # #             print('Port event: %d' % data)
    # def SetPort(color, size):
    #     # SetPortData((color - 1) * 6 ** 2 + (size - 1) * 6 + (block))
    #     if size == 1:
    #         if color == 1:
    #             code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['LHeat']))]
    #             # logging.log(level=logging.EXP, msg='set medoc %s' % (code.iat[0, 1]))
    #         elif color == 2:
    #             code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['MHeat']))]
    #             # logging.log(level=logging.EXP, msg='set medoc %s' % (code.iat[0, 1]))
    #         elif color == 3:
    #             code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['HHeat']))]
    #             # logging.log(level=logging.EXP, msg='set medoc %s' % (code.iat[0, 1]))
    #         # elif color == 4:
    #         #     if randBlack[randBlackCount] == 2:
    #         #         code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['HHeat']))]
    #         #         # logging.log(level=logging.EXP, msg='set medoc %s' % (code.iat[0, 1]))
    #         #         randBlackCount += 1
    #         #     elif randBlack[randBlackCount] == 1:
    #         #         code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['MHeat']))]
    #         #         # logging.log(level=logging.EXP, msg='set medoc %s' % (code.iat[0, 1]))
    #         #         randBlackCount += 1
    #         #     elif randBlack[randBlackCount] == 0:
    #         #         code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['LHeat']))]
    #         #         # logging.log(level=logging.EXP, msg='set medoc %s' % (code.iat[0, 1]))
    #         #         randBlackCount += 1
    #     if params['painSupport']:
    #         response = my_pathway.program(code.iat[0, 1])
    #         my_pathway.start()
    #         my_pathway.trigger()
else:
    # excel in the folder to convert from Celsius temp to binary code for the medoc machine
    excelTemps = pd.read_excel(params['convExcel'])
# ====================== #
# ==== Title Screen ==== #
# ====================== #
img1 = visual.ImageStim(win=win,image="./img/title.jpg",units="pix",size=params['screenSize'],opacity=1) #
win.mouseVisible = False
img1.draw();win.flip();
waitAnyKeys()

# # ======================== #
# # Dataframe Initialization #
# # ======================== #
params['Header'] = ["ExperimentName","SessionStartDateTime","Subject","Session","Version","Section","Subtrial",
          "DistanceFromDoor_SubTrial","Distance_lock","Distance_start","Distance_min","Distance_max",
          "Door_anticipation_time","Door_opened","Door_outcome","Reward_magnitude","Punishment_magnitude",
          "DoorAction_RT","ITI_duration","Total_coins","VAS_type","VAS_score","VAS_RT","Q_type","Q_score","Q_RT"]
params['HeaderTR'] = ["Index", "subjectID", "Session", "Version", "Section", "Subtrial", "Event", "Reward", "Punishment",
            "Duration(ms)"]

# Getting Image List
import glob
imgList = glob.glob("img/img_03312025/task_visual_7X7/*.jpg")
imgList += glob.glob("img/img_03312025/task_visual_5X7/*.jpg")
import random
random.shuffle(imgList)
# print("1st block")
# for i in range(25):
#     print(imgList.pop())
# print("2nd block")
# for i in range(25):
#     print(imgList.pop())
# print("3rd block")
# for i in range(24):
#     print(imgList.pop())
#

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
win.mouseVisible = False
iterNum = params['numPractice']
SectionName = "Practice"

Df,DfTR,win = PracticeGamePlay(Df, DfTR,win, params, iterNum, port,SectionName)
win.mouseVisible = False



# ====================== #
# ===Fortune Wheel1 ==== #
# ====================== #
# win.close()

import platform
if platform.system() == 'Windows':
    Df,win = FortuneGamePlay(Df, win,params,"Fortune Wheel 1",18)

# ====================== #
# ===== TaskRun1 ======= #
# ====================== #
win.mouseVisible = False
Df,DfTR,win,imgList = DoorGamePlay(Df,DfTR,win,params,params['numTaskRun1'],port,"TaskRun1",excelTemps,my_pathway,imgList)
win.mouseVisible = True

# ====================== #
# ======== VAS 1 ========= #
# ====================== #
win.mouseVisible = True
message = visual.TextStim(win, text="Let's rest for a bit.  Press the spacebar when you are ready to keep playing.", units='norm', wrapWidth=2)
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

# # ====================== #
# # ===Fortune Wheel2 ==== #
# # ====================== #
# # win.close()

if platform.system() == 'Windows':
    Df,win = FortuneGamePlay(Df, win,params,"Fortune Wheel 2",16)

# ====================== #
# ===== TaskRun2 ======= #
# ====================== #
Df,DfTR,win,imgList = DoorGamePlay(Df,DfTR,win,params,params['numTaskRun2'],port,"TaskRun2",excelTemps,my_pathway,imgList)

# ====================== #
# ======== VAS mid ========= #
# ====================== #
win.mouseVisible = True
message = visual.TextStim(win, text="Let's rest for a bit.  Press the spacebar when you are ready to keep playing.", units='norm', wrapWidth=2)
message.draw();win.flip();
waitUserSpace(Df,params)
Df = VASplay(Df,win,params,"VAS mid")
win.mouseVisible = False

# ====================== #
# ======== Text Slide ========= #
# ====================== #
img1 = visual.ImageStim(win=win,image="./img/after_VAS2.jpg",units="pix",size=params['screenSize'],opacity=1) #
waitUserInput(Df,img1, win, params,'pyglet')
win.flip();

# ====================== #
# ===Fortune Wheel3 ==== #
# ====================== #
# win.close()
if platform.system() == 'Windows':
    Df, win = FortuneGamePlay(Df, win, params, "Fortune Wheel 3", 16)
# win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')


# ====================== #
# ===== TaskRun3 ======= #
# ====================== #
win.mouseVisible = False
Df,DfTR,win,imgList = DoorGamePlay(Df,DfTR,win,params,params['numTaskRun3'],port,"TaskRun3",excelTemps,my_pathway,imgList)
win.mouseVisible = True

# ====================== #
# ======== VAS post ========= #
# ====================== #
win.mouseVisible = True
# message = visual.TextStim(win, text="Let's rest for a bit.  when you are ready to keep playing.", units='norm', wrapWidth=2)
message = visual.TextStim(win, text="Let's rest for a bit.  Press the spacebar when you are ready to keep playing.", units='norm', wrapWidth=2)
message.draw();win.flip();
waitUserSpace(Df,params)
Df = VASplay(Df,win,params,"VAS post")
win.mouseVisible = False

# ====================== #
# ======== Question ========= #
# ====================== #
win.mouseVisible = True
Df = Questionplay(Df, win, params, "Question")

Df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)
import os
file_path = params['outFile_tmp']
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Temp Deleted: {file_path}")
else:
    print(f"File does not exist: {file_path}")

# waitUserSpace(Df, params)
message = visual.TextStim(win,
                          text="Great job! You collected a lot of coins.\n\nYou're going home with $57.00!\n\nThanks for playing!",
                          units='norm', wrapWidth=2)
message.draw();
win.flip();
# waitUserSpace(Df, params)
waitUserSpace(Df,params)
message.draw();

# Close the psychopy window.
win.close()
