import glob,re,random,time
import pandas as pd
from psychopy import core, visual, event, sound,gui
from psychopy.hardware import joystick
from Helper import fadeInOutImage, Questionplay,DoorGamePlay,VASplay,InstructionPlay,userInputPlay
import datetime

# Receive User Input
userInputBank = userInputPlay()

# Declare primary task parameters.
params = {
# Declare stimulus and response parameters
    'expName' : userInputBank[0], # The name of the experiment
    # 'nTrials': 5,            # number of trials in this session
    'subjectID' : userInputBank[1],      # Subject ID
    'DistanceStart' : 50,
    'DistanceLockWaitTime' : 10, # Distance lock wait time.
    'Session' : userInputBank[2],
    'Version' : userInputBank[3],
    'imageDir': './img/doors/',    # directory containing DOOR image stimluli
    'imageSuffix': '*.jpg',   # DOOR image extension.
# declare output file location
    'outFolder': './output', # the location of output file.
# declare display parameters
#     'fullScreen': True,       # run in full screen mode?
    'screenSize' : (1200,800),
#     'screenToShow': 0,        # display on primary screen (0) or secondary (1)?
#     'fixCrossSize': 0.1,       # size of cross, in height units
#     'fixCrossPos': [0,0],     # (x,y) pos of fixation cross displayed before each stimulus (for gaze drift correction)
#     'screenColor':(128,128,128) # in rgb255 space: (r,g,b) all between 0 and 255
}


## Setup Section.
win = visual.Window(params['screenSize'], monitor="testMonitor")

# Display NIMH logo.
fadeInOutImage(win,"./img/nimh.png",0.5,(600,600))

# ====================== #
# ==== Title Screen ==== #
# ====================== #
img1 = visual.ImageStim(win=win,image="./img/title.jpg",units="pix",size=params['screenSize'],opacity=1) #
img1.draw();win.flip();event.waitKeys()

# ======================== #
# Dataframe Initialization #
# ======================== #
Header = ["ExperimentName","SessionStartDateTime","Subject","Session","Version","Section","Subtrial",
          "DistanceFromDoor_SubTrial","Distance_lock","Distance_start","Distance_min","Distance_max",
          "Door_anticipation_time","Door_opened","Door_outcome","Reward_magnitude","Punishment_magnitude",
          "DoorAction_RT","ITI_duration","Total_coins","VAS_type","VAS_score","VAS_RT","Q_type","Q_score","Q_RT"]

Df = pd.DataFrame(columns=Header)
# Dict = {}
# Dict["ExperimentName"] = 1234
# Dict["Subject"] = "Jimmy"

# ====================== #
# ======== VAS ========= #
# ====================== #
Df = VASplay(Df,win,params,"VAS1")

# ====================== #
# ===== Instruction ==== #
# ====================== #
InstructionPlay(Df,win,params)

# ====================== #
# ===== Practice ======= #
# ====================== #
# Get the DOOR image file list.
Df = DoorGamePlay(Df,win,params,1,"Practice")

# ====================== #
# ===== TaskRun1 ======= #
# ====================== #
Df = DoorGamePlay(Df,win,params,2,"TaskRun1")

# ====================== #
# ======== VAS2 ========= #
# ====================== #
Df = VASplay(Df,win,params,"VAS2")

# ====================== #
# ===== TaskRun2 ======= #
# ====================== #
Df = DoorGamePlay(Df,win,params,3,"TaskRun2")

# ====================== #
# ======== VAS3 ========= #
# ====================== #
Df = VASplay(Df,win,params,"VAS3")

# ====================== #
# ======== Question ========= #
# ====================== #
Df = Questionplay(Df, win, params, "Question")

# Write the output file.
Df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)

# Close the psychopy window.
win.close()
